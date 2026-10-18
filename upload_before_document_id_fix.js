
const uploadForm = document.getElementById("uploadForm");
const fileInput = document.getElementById("studyFile");
const selectedFile = document.getElementById("selectedFile");
const uploadStatus = document.getElementById("uploadStatus");
const uploadButton = document.getElementById("uploadButton");

const chatForm = document.getElementById("chatForm");
const chatInput = document.getElementById("chatInput");
const chatMessages = document.getElementById("chatMessages");
const sendButton = document.getElementById("sendButton");

const allowedExtensions = [".pdf", ".pptx", ".docx", ".md", ".txt"];
const MAX_FILE_SIZE = 14 * 1024 * 1024;
const MAX_TOTAL_SIZE = 50 * 1024 * 1024;
const MAX_FILES = 10;

let fileUploaded = false;

sendButton.disabled = true;
chatInput.disabled = true;

// Display and validate selected files
fileInput.addEventListener("change", () => {
    const files = Array.from(fileInput.files);

    fileUploaded = false;
    sendButton.disabled = true;
    chatInput.disabled = true;
    uploadStatus.textContent = "";

    if (files.length === 0) {
        selectedFile.textContent = "No files selected yet";
        return;
    }

    selectedFile.textContent = files
        .map(file =>
            `${file.name} (${(file.size / (1024 * 1024)).toFixed(2)} MB)`
        )
        .join(", ");

    if (files.length > MAX_FILES) {
        uploadStatus.textContent = `You can upload a maximum of ${MAX_FILES} files.`;
        fileInput.value = "";
        selectedFile.textContent = "No files selected yet";
        return;
    }

    const invalidFile = files.find(file =>
        !allowedExtensions.some(extension =>
            file.name.toLowerCase().endsWith(extension)
        )
    );

    if (invalidFile) {
        uploadStatus.textContent =
            `${invalidFile.name}: Only PDF, PPTX, DOCX, MD and TXT files are supported.`;
        fileInput.value = "";
        selectedFile.textContent = "No files selected yet";
        return;
    }

    const oversizedFile = files.find(file => file.size > MAX_FILE_SIZE);

    if (oversizedFile) {
        uploadStatus.textContent =
            `${oversizedFile.name}: Each file must be 14 MB or smaller.`;
        fileInput.value = "";
        selectedFile.textContent = "No files selected yet";
        return;
    }

    const totalSize = files.reduce((total, file) => total + file.size, 0);

    if (totalSize > MAX_TOTAL_SIZE) {
        uploadStatus.textContent = "Total upload size must be 50 MB or less.";
        fileInput.value = "";
        selectedFile.textContent = "No files selected yet";
    }
});

// Upload multiple files
uploadForm.addEventListener("submit", async event => {
    event.preventDefault();

    const files = Array.from(fileInput.files);

    if (files.length === 0) {
        uploadStatus.textContent = "Please select at least one file.";
        return;
    }

    const invalidFile = files.find(file =>
        !allowedExtensions.some(extension =>
            file.name.toLowerCase().endsWith(extension)
        )
    );

    if (invalidFile) {
        uploadStatus.textContent =
            `${invalidFile.name}: Unsupported file type.`;
        return;
    }

    if (files.some(file => file.size > MAX_FILE_SIZE)) {
        uploadStatus.textContent = "Each file must be 14 MB or smaller.";
        return;
    }

    const totalSize = files.reduce((total, file) => total + file.size, 0);

    if (files.length > MAX_FILES || totalSize > MAX_TOTAL_SIZE) {
        uploadStatus.textContent =
            "Maximum 10 files and 50 MB total upload size allowed.";
        return;
    }

    const formData = new FormData();

    files.forEach(file => {
        formData.append("files", file);
    });

    uploadButton.disabled = true;
    uploadButton.textContent = "Uploading...";
    uploadStatus.textContent = "Uploading and extracting document text...";

    try {
        const response = await fetch("/api/pdf/upload", {
            method: "POST",
            body: formData
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.error || "File upload failed.");
        }

        fileUploaded = true;
        sendButton.disabled = false;
        chatInput.disabled = false;

        uploadStatus.textContent =
            result.message || `${files.length} file(s) uploaded successfully.`;

        addMessage(
            "assistant",
            `Your study files have been processed: ${files.map(file => file.name).join(", ")}. You can now ask questions about your uploaded material.`
        );

    } catch (error) {
        fileUploaded = false;
        sendButton.disabled = true;
        chatInput.disabled = true;
        uploadStatus.textContent = error.message;
    } finally {
        uploadButton.disabled = false;
        uploadButton.textContent = "Upload & Analyze";
    }
});

// Add messages to chat
function addMessage(type, text) {
    const message = document.createElement("div");

    message.className = type === "user"
        ? "message user-message"
        : "message assistant-message";

    if (type === "assistant") {
        const heading = document.createElement("strong");
        heading.textContent = "Campus AI";
        message.appendChild(heading);
    }

    const paragraph = document.createElement("p");
    paragraph.textContent = text;
    message.appendChild(paragraph);

    chatMessages.appendChild(message);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    return message;
}

// Ask questions about uploaded documents
chatForm.addEventListener("submit", async event => {
    event.preventDefault();

    if (!fileUploaded) {
        addMessage("assistant", "Please upload your study material first.");
        return;
    }

    const question = chatInput.value.trim();

    if (!question) return;

    addMessage("user", question);
    chatInput.value = "";

    const waitingMessage = addMessage(
        "assistant",
        "Let me check your uploaded study material..."
    );

    sendButton.disabled = true;

    try {
        const response = await fetch("/api/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question })
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.error || "Could not get an answer.");
        }

        waitingMessage.querySelector("p").textContent = result.answer;

    } catch (error) {
        waitingMessage.querySelector("p").textContent = error.message;
    } finally {
        sendButton.disabled = !fileUploaded;
        chatInput.focus();
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
