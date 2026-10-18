🎓 Mewar Campus IQ — AI-Powered Smart Learning

«An AI-powered study companion designed to help students interact with their study materials, ask questions, and practice quizzes in one place.»

🌐 Live Demo: https://mewar-campus-iq.onrender.com

📦 GitHub Repository: https://github.com/MDSalman22415/mewar-campus-iq

---

🚀 About the Project

Mewar Campus IQ is an AI-powered educational web application developed around the theme “The Smart Campus” for MU Hackathon 2026 at Mewar University.

The project aims to make learning more interactive by bringing study-material uploads, AI-assisted question answering, and quiz practice together in one platform.

As a member of the Mewar University student community and Founder of Mewar Innovators Hub, I believe technology can help students access learning resources more effectively and turn ideas into practical solutions.

🎯 Problem Statement

Students often manage notes, PDFs, assignments, and revision resources across different platforms. Finding relevant information and understanding difficult concepts can take time.

Mewar Campus IQ aims to simplify this learning process through a centralized, student-focused platform.

💡 Key Features

- AI-Assisted Study Chat — Ask questions and receive AI-generated explanations.
- PDF Study Material Upload — Upload supported PDFs for text extraction and study workflows.
- Quiz Practice — Access quiz-related features and submit answers.
- Student Authentication — Login and registration interfaces.
- Web-Based Interface — Access the application through a browser.
- Cloud Deployment — A publicly hosted prototype available online.

Feature availability depends on the current deployed implementation and service configuration.

🛠️ Technology Stack

- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- AI Integration: Google Gemini API
- PDF Processing: PyMuPDF and/or pypdf
- Database: PostgreSQL via Supabase
- Deployment: Render
- Containerization: Docker
- Version Control: Git and GitHub

🔄 How It Works

1. Open the web application.
2. Access the available study features.
3. Upload a supported PDF when using the document workflow.
4. Ask questions through the AI-assisted study interface.
5. Explore the available quiz functionality.

AI-generated responses should be checked against reliable academic sources.

🌐 Live Application

Try the project here:

https://mewar-campus-iq.onrender.com

The application is a deployed prototype. Availability and certain features may depend on hosting, database connectivity, and AI-provider limits.

💻 Run Locally

1. Clone the repository

git clone https://github.com/MDSalman22415/mewar-campus-iq.git
cd mewar-campus-iq

2. Create a virtual environment

python -m venv venv

Activate it on Windows:

.\venv\Scripts\Activate.ps1

On macOS/Linux:

source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Configure environment variables

Configure the API key and database settings required by the application. Use the variable names expected by the source code.

Never commit API keys, passwords, database credentials, or ".env" files.

5. Run the application

python app.py

Open the local URL shown in the terminal.

🔐 Security Notes

- Keep API keys and database credentials private.
- Use environment variables for sensitive configuration.
- Avoid uploading personal or confidential student information.
- Verify AI-generated explanations before relying on them academically.

🚀 Future Improvements

Potential improvements for future versions include:

- Better personalization of study resources.
- Improved quiz generation and progress tracking.
- OCR support for scanned PDFs.
- Enhanced student dashboards.
- More campus-focused learning tools.
- Improved accessibility and multilingual support.

These are possible future enhancements, not claims about features already implemented.

👥 Team & Acknowledgements

Developed as a student innovation project for the MU Hackathon 2026 — The Smart Campus theme at Mewar University.

Project leadership and community initiative: Sujit Kumar
Community: Mewar Innovators Hub

The project was built collaboratively. Contributors and their specific responsibilities should be credited according to their actual contributions.

🏆 Vision

At Mewar Innovators Hub, we believe every student deserves an environment where ideas can grow into practical solutions.

Mewar Campus IQ represents the spirit of student innovation, collaboration, and technology-driven learning.

Mewar Innovators Hub
Building for the Isolated Builders.

📄 License

A license has not been specified here. Add a license only after confirming the project's ownership and the team's permission to publish the code under that license.F upload flow accepts PDF documents and extracts machine-readable
text. The current implementation includes validation for PDF uploads and
may reject unsupported, encrypted, oversized, or text-empty documents.

**Important:** A PDF containing scanned pages may not contain
extractable text. OCR would be needed to reliably process that type of
document.

### AI requests

The AI question-answering feature sends a request to the configured
Gemini model. A valid API key and an available model are required. Model
availability, rate limits, quota, service outages, and network
conditions can affect responses.

Do not place API keys in frontend JavaScript or expose them in
responses. Configure credentials on the server through environment
variables.

------------------------------------------------------------------------

## Local Setup

### Prerequisites

Install the following before running the project locally:

-   Python compatible with the dependencies in `requirements.txt`.
-   Git.
-   A Google Gemini API key if you want to use the AI features.
-   Supabase/PostgreSQL connection details if the current configuration
    requires the database.
-   Docker Desktop only if you want to build and run the container
    locally.

### 1. Clone the repository

``` bash
git clone https://github.com/MDSalman22415/mewar-campus-iq.git
cd mewar-campus-iq
```

### 2. Create a virtual environment

**Windows PowerShell:**

``` powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use the Python executable inside the
environment directly or follow your organization's PowerShell
execution-policy guidance.

**macOS / Linux:**

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

``` bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If installation fails, check that your Python version is compatible with
the pinned package versions. Use the Python version supported by the
project dependencies rather than upgrading packages blindly.

### 4. Configure environment variables

Create a local `.env` file if the application uses one. Start from
`.env.example` if it exists. Add your own credentials locally; never
commit `.env`.

Example names only --- confirm the exact names used by `app.py` and
`config.py` before configuring:

``` dotenv
GEMINI_API_KEY=your_gemini_api_key
# Add the database connection variables required by this repository.
# Example only:
DATABASE_URL=your_postgresql_connection_string
```

The database variable name above is illustrative. Use the exact variable
names read by the current application code. Do not include real
credentials in the README or in Git.

### 5. Start the application

If the project uses `app.py` as its Flask entry point, run:

``` bash
python app.py
```

Open the local URL printed by Flask in your terminal (commonly
`http://127.0.0.1:5000`).

If the repository defines a different start command, use the command
documented in its deployment configuration.

------------------------------------------------------------------------

## Environment Variables

The application may rely on environment variables for external services
and runtime settings.

  -----------------------------------------------------------------------
  Variable                Purpose                 Required?
  ----------------------- ----------------------- -----------------------
  `GEMINI_API_KEY`        Authenticates requests  Required for Gemini
                          to Google Gemini, if    features
                          this is the variable    
                          used by the code        

  Database connection     Connects to             Required for features
  variable(s)             Supabase/PostgreSQL     that use the database

  `PORT`                  Port supplied by the    Platform-dependent
                          hosting platform, if    
                          consumed by the         
                          app/start command       

  Flask secret/session    Protects                Required if session
  key                     session-related         features depend on it
                          functionality, if used  
  -----------------------------------------------------------------------

**Verify variable names against the current source code.** This table
documents configuration categories and does not guarantee that every
listed name is used by the current version.

On Render, add secrets through the service's **Environment** settings.
Keep private values out of source code, screenshots, logs, commits, and
public documentation.

## API Endpoints

The table below lists routes identified in the current project
implementation. It describes their general purpose; inspect `app.py` for
exact methods, authentication requirements, request schemas, and
response formats.

  Endpoint                    Purpose
  --------------------------- --------------------------------------
  `GET /login`                Render the login interface
  `POST /login`               Process login form submission
  `GET /signup`               Render the sign-up interface
  `POST /signup`              Process registration form submission
  `GET /topic-quiz`           Serve quiz-related page
  `POST /api/quiz/generate`   Quiz-related API operation
  `POST /api/quiz/submit`     Submit quiz answers
  `POST /api/ask`             Send a question to the AI flow
  `POST /api/pdf/upload`      Upload and process a PDF
  `GET /api/health`           Health-check response

The exact HTTP method for an API route should be verified in its
`@app.route(...)` decorator. If an endpoint returns `404`, check the
route name, deployment status, and URL spelling before assuming the
service is down.

## Database

The deployed application has been configured to connect to **Supabase
PostgreSQL**.

Database responsibilities depend on the current implementation and may
include application records or other persistent data. To work on the
database locally:

1.  Create or select a Supabase project.
2.  Obtain the appropriate PostgreSQL connection details.
3.  Add the connection information to the environment variables expected
    by the code.
4.  Keep database credentials private.
5.  Confirm that network access and SSL settings match the database
    provider's requirements.

Never put a production database password in the README, source code, or
a public issue. Use a separate development database where possible.

## Deployment

The application is publicly hosted on Render:

**Live URL:** https://mewar-campus-iq.onrender.com

The repository includes Docker-related deployment files. A typical
deployment workflow is:

1.  Push the tested code to the GitHub repository.
2.  Connect the repository to a Render web service, or update the
    existing service.
3.  Configure the build and start commands to match the Dockerfile /
    project setup.
4.  Add required environment variables in Render's dashboard.
5.  Deploy and wait for the build and startup to complete.
6.  Review Render logs for startup errors and external-service
    connection failures.
7.  Test the live page, static assets, upload flow, and
    AI/database-dependent features.

### Deployment checklist

-   [ ] Latest changes are pushed to the intended branch.
-   [ ] Render is deploying the intended commit.
-   [ ] Required environment variables are configured.
-   [ ] The application starts successfully.
-   [ ] `/api/health` responds as expected.
-   [ ] Login and sign-up pages load.
-   [ ] CSS and JavaScript assets load successfully.
-   [ ] PDF upload works for a valid text-based PDF.
-   [ ] AI requests work with the configured API key and available
    model.
-   [ ] Database-dependent features work.
-   [ ] No secret values appear in GitHub or public logs.

### Case-sensitive file paths

Render uses a Linux environment where file and directory names are
case-sensitive. For example, `static/js/auth.js` and `static/JS/auth.js`
are different paths on Linux. Keep the capitalization in template
references identical to the names tracked in Git.

## Testing and Troubleshooting

### Application does not start

-   Read the complete Render build and runtime logs.
-   Confirm the configured Python packages are in `requirements.txt`.
-   Verify the start command and entry point.
-   Check for syntax errors and missing environment variables.

### CSS or JavaScript is missing

-   Open the relevant asset URL directly in a browser.
-   Check browser developer tools for `404` responses.
-   Confirm the template path and tracked filename use exactly the same
    capitalization.
-   Hard-refresh the page after a successful deployment (`Ctrl + F5` on
    Windows).

### Sign-up or login does not work

-   Confirm the browser is visiting the correct route (`/signup` for
    registration in the current implementation).
-   Check the form's `action` and `method`.
-   Inspect Render logs for backend exceptions.
-   Verify database connectivity and the current authentication
    implementation.

### AI requests fail

Possible causes include:

-   Missing or invalid API key.
-   Incorrect or unavailable Gemini model name.
-   Quota or rate-limit restrictions.
-   Temporary provider overload or outage.
-   Incorrect request payload or server-side exception.

Check the provider's current model documentation and service status. Do
not publish API keys or paste them into public bug reports.

### PDF upload fails

-   Confirm that the selected file is a PDF.
-   Try a small PDF containing selectable text.
-   Check whether the PDF is encrypted or exceeds the application's
    configured limits.
-   Try a text-based PDF if a scanned document fails; scanned PDFs may
    need OCR.

### Database connection fails

-   Verify the connection string and credentials.
-   Check Supabase project status and database access settings.
-   Confirm required SSL options.
-   Make sure secrets are configured in the correct Render service
    environment.

## Security Notes

-   **Never commit `.env` files, API keys, database passwords, or
    session secrets.**
-   Keep `.env` ignored by Git and use `.env.example` for safe
    placeholders.
-   Rotate any credential that has accidentally been shared publicly.
-   Validate uploaded files on the server and set sensible upload
    limits.
-   Avoid logging authentication secrets, API keys, or private student
    data.
-   Use HTTPS for the deployed site.
-   Apply appropriate authentication and authorization checks to
    protected routes.
-   Before production use with real student data, review session
    security, password handling, database permissions, upload storage,
    rate limiting, and privacy requirements.

This project is an educational prototype; do not treat this README as a
security audit or a guarantee that every production hardening measure is
implemented.

## Limitations

-   AI answers may be incomplete or inaccurate; verify important
    information.
-   AI functionality depends on external API availability, model access,
    and quotas.
-   Text extraction is not the same as OCR; image-only or scanned PDFs
    may not be processed.
-   The live instance may experience cold starts or temporary
    unavailability depending on hosting configuration.
-   Features that depend on environment variables or external services
    may not work in a local setup until those services are configured.
-   The current implementation should be reviewed before handling
    sensitive or large-scale institutional data.

## Future Improvements

Potential next steps for the project include:

-   Retrieval-augmented generation (RAG) grounded in the student's
    uploaded material.
-   Persistent document library with subject, semester, and year tags.
-   Better search across uploaded notes and previous-year questions.
-   OCR support for handwritten or scanned notes.
-   Automatic summaries, flashcards, and structured revision plans.
-   More complete quiz generation, scoring, history, and progress
    analytics.
-   Improved file management, storage limits, and deletion controls.
-   More comprehensive automated tests and CI checks.
-   Role-based access for students, faculty, and administrators.
-   Better observability, error handling, and production security
    hardening.
-   Accessibility and responsive-design improvements.

These are ideas for future development and should not be interpreted as
features that are already complete.

## Contributing

Contributions, bug reports, and improvement ideas are welcome.

1.  Fork the repository.
2.  Create a feature branch.
3.  Make a focused change.
4.  Test the relevant flow locally.
5.  Confirm that no secrets or private files are included.
6.  Commit your changes with a clear message.
7.  Open a pull request describing the change and how it was tested.

For bug reports, include the route or feature affected, reproduction
steps, expected behavior, actual behavior, and relevant sanitized error
messages. Never include passwords, API keys, or private student
information.

## Team and Credits

Mewar Campus IQ was developed as a student-focused Smart Campus / AI
learning project.

-   **Project:** Mewar Campus IQ
-   **Repository owner:**
    [MDSalman22415](https://github.com/MDSalman22415)
-   **Source code:** [GitHub
    repository](https://github.com/MDSalman22415/mewar-campus-iq)
-   **Live application:**
    [mewar-campus-iq.onrender.com](https://mewar-campus-iq.onrender.com)

Add the names and contributions of all team members here before
submitting the repository as a formal team project. Credit third-party
libraries and services according to their applicable licenses and terms.

## License

No license has been specified in this README. Unless a license file is
added to the repository, do not assume that the source code is available
for unrestricted reuse, redistribution, or modification.

To make the project open source, choose a license appropriate to the
project and add a corresponding `LICENSE` file. For example, the MIT
License is a common permissive option, but the project owner should make
that decision explicitly.

------------------------------------------------------------------------

## Quick Links

-   **Live Demo:** https://mewar-campus-iq.onrender.com
-   **GitHub Repository:**
    https://github.com/MDSalman22415/mewar-campus-iq

*Built to make campus learning more interactive, accessible, and
AI-assisted.* 🎓
