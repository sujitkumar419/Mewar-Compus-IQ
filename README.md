# Mewar Campus IQ 🎓🤖

> **An AI-powered study companion for students** --- upload study
> material, ask questions about your learning content, practice quizzes,
> and keep academic resources in one place.

🌐 **Live Demo:** https://mewar-campus-iq.onrender.com\
📦 **GitHub Repository:**
https://github.com/MDSalman22415/mewar-campus-iq

------------------------------------------------------------------------

## Table of Contents

-   [Overview](#overview)
-   [Problem Statement](#problem-statement)
-   [Our Solution](#our-solution)
-   [Features](#features)
-   [User Workflow](#user-workflow)
-   [Technology Stack](#technology-stack)
-   [Architecture](#architecture)
-   [Project Structure](#project-structure)
-   [How It Works](#how-it-works)
-   [Local Setup](#local-setup)
-   [Environment Variables](#environment-variables)
-   [Run the Application](#run-the-application)
-   [API Endpoints](#api-endpoints)
-   [Database](#database)
-   [Deployment](#deployment)
-   [Testing and Troubleshooting](#testing-and-troubleshooting)
-   [Security Notes](#security-notes)
-   [Limitations](#limitations)
-   [Future Improvements](#future-improvements)
-   [Contributing](#contributing)
-   [Team and Credits](#team-and-credits)
-   [License](#license)

------------------------------------------------------------------------

## Overview

**Mewar Campus IQ** is a web-based AI study companion designed to help
students interact with their academic resources more effectively.
Instead of only storing notes and PDFs, the project brings together
study-material upload, AI-assisted learning, and quiz practice in one
web application.

The project was built as a Smart Campus / AI-for-education prototype and
deployed publicly so users can try the application online.

**Live application:** https://mewar-campus-iq.onrender.com

> **Project status:** Deployed prototype. Availability and AI response
> times may depend on the hosting platform, database configuration, and
> the availability/limits of the configured AI provider.

## Problem Statement

Students often keep notes, previous-year questions, assignments, and
other learning resources in separate folders or platforms. Finding the
right material, understanding a difficult topic, and revising
efficiently can take time.

Mewar Campus IQ aims to make the study workflow more convenient by
providing a single place to:

-   Access the application's study features.
-   Upload supported PDF study material.
-   Ask AI-assisted questions.
-   Practice quiz questions and submit answers.
-   Explore a foundation that can be extended into a broader campus
    learning platform.

## Our Solution

Mewar Campus IQ combines a Flask web application with a browser-based
interface, a database connection, PDF text extraction, and an AI-powered
question-answering flow. The goal is to make learning resources more
interactive and to provide a practical foundation for future
student-focused features.

## Features

### 1. Student authentication interface

-   Login and sign-up flows.
-   Server-side routes for login and account registration.
-   Form-based interaction through the web interface.

### 2. PDF study-material upload

-   Upload PDF files through the application.
-   Extract text from supported PDFs for further processing.
-   Validate basic upload requirements, including file type and
    size/page-related restrictions implemented by the application.
-   Scanned/image-only PDFs may not work when they contain no
    extractable text; OCR is a potential future enhancement.

### 3. AI-assisted study chat

-   Ask questions and receive AI-generated explanations.
-   Intended to help students understand concepts and study material.
-   The AI response depends on the configured Gemini API model,
    credentials, quota, and provider availability.
-   AI-generated answers should be checked against course material and
    trusted sources.

### 4. Quiz practice

-   Quiz-related routes support quiz interaction and answer submission.
-   The application includes a quiz submission API.
-   The exact question-generation and quiz experience may depend on the
    current implementation and configuration.

### 5. Student-facing web interface

-   HTML templates with CSS and JavaScript assets.
-   Separate styling files for authentication and other application
    views.
-   Static assets are served by Flask.
-   Asset paths use lowercase `static/css/` and `static/js/` paths to
    support case-sensitive deployment environments.

### 6. Database connectivity

-   Configured to connect to a PostgreSQL database through Supabase.
-   Database availability depends on correct environment variables and
    the database provider.
-   Never commit database passwords, API keys, or other private
    credentials to the repository.

### 7. Public deployment

-   Hosted on Render.
-   A Docker-based deployment configuration is included in the project.
-   The live app can be accessed at
    https://mewar-campus-iq.onrender.com.

------------------------------------------------------------------------

## User Workflow

A typical intended workflow is:

1.  Open the [live application](https://mewar-campus-iq.onrender.com).
2.  Use the login or sign-up interface.
3.  Open the relevant study feature.
4.  Upload a supported PDF if using the upload workflow.
5.  Ask a study question or use available quiz functionality.
6.  Review the response and verify important information against the
    original study material.

The precise screens and available actions reflect the current deployed
version.

## Technology Stack

  -----------------------------------------------------------------------
  Layer                   Technology              Purpose
  ----------------------- ----------------------- -----------------------
  Backend                 Python, Flask           Web server, routing,
                                                  request handling

  Frontend                HTML, CSS, JavaScript   Pages, styling, and
                                                  browser interactions

  AI integration          Google Gemini API       AI-assisted answers and
                                                  learning interactions

  PDF processing          PyMuPDF (`fitz`) and/or PDF text extraction and
                          `pypdf`                 upload processing

  Database                PostgreSQL via Supabase Persistent data storage
                                                  / database connectivity

  Hosting                 Render                  Public web deployment

  Containerization        Docker                  Reproducible
                                                  application packaging
                                                  and deployment

  Version control         Git and GitHub          Source control and
                                                  collaboration
  -----------------------------------------------------------------------

> Dependencies and exact versions are defined in the repository's
> dependency files. Check those files for the authoritative list of
> installed packages.

## Architecture

At a high level, the application follows this request flow:

``` text
Student's browser
       |
       | HTTP request / form submission
       v
Flask application (app.py)
       |
       +------> HTML templates
       |           |
       |           +---- CSS and JavaScript static assets
       |
       +------> PDF text extraction
       |
       +------> Gemini API (AI requests)
       |
       +------> Supabase PostgreSQL (database connection)
       |
       v
HTTP response rendered in the browser
```

The browser communicates with Flask routes. Flask renders templates or
returns API responses, and the relevant backend feature communicates
with the configured external service when required.

## Project Structure

The repository contains the following key paths. The exact contents may
evolve as features are added.

``` text
mewar-campus-iq/
├── app.py                  # Flask application and routes
├── config.py               # Application configuration (if used)
├── pdf_reader.py           # PDF-reading / text-extraction utility
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container build instructions
├── .dockerignore           # Files excluded from Docker build context
├── .env.example            # Example environment configuration, if present
├── .gitignore              # Files excluded from Git
├── campus_iq/              # Application package / supporting code
├── data/                   # Local data files, if used
├── docs/                   # Project documentation
├── instance/               # Instance-specific application files, if used
├── static/
│   ├── css/                # Stylesheets
│   ├── js/                 # Browser-side JavaScript
│   └── images/             # Images and visual assets
├── templates/              # Flask/Jinja HTML templates
├── tests/                  # Tests
└── uploads/                # Local upload directory, if used
```

Some folders may be empty or used only by particular development
workflows. For the definitive current structure, inspect the repository
itself.

## How It Works

### Flask routes

The Flask application defines routes for pages and application
functionality. Routes identified in the current implementation include:

-   `/login` --- login page and login handling.
-   `/signup` --- registration page and sign-up handling.
-   `/topic-quiz` --- quiz-related page.
-   `/api/quiz/generate` --- quiz-related API route.
-   `/api/quiz/submit` --- quiz answer submission.
-   `/api/ask` --- AI question-answering request.
-   `/api/pdf/upload` --- PDF upload and processing.
-   `/api/health` --- health-check endpoint.

Routes may require authentication or particular request formats. Refer
to `app.py` for the current implementation and validation logic.

### PDF processing

The PDF upload flow accepts PDF documents and extracts machine-readable
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
