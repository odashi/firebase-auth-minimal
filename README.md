# Firebase Auth Minimal App

This example contains a minimal example Web application working with Firebase
Authentication and/or Google Identity Platform.

The app consists of following servers:

- Frontend (`localhost:8080`): Written in bare Javascript, JQuery, and Firebase
  utilities.
- Backend (`localhost:8081`): Written in Python/FastAPI, protected by CORS and
  authentication.

## Getting Started

### Prerequisites

You need to install Docker or a container runtime compatible with Docker before trying
the steps below.

### Prepare Identity Platform

1. Prepare a Google Cloud project.
1. Enable Identity Platform from the marketplace.
1. Add an Email provider.

### Set up the backend

1. Open `backend/main.py` and replace `audience` config with the value corresponding to
   your project.
1. Open a shell.
1. On `backend/`, run `docker build -t backend .`
1. Run `docker run -it --rm -p 8081:8081 backend`

### Set up the frontend

1. Open `frontend/static/main.js` and replace `apiKey` and `authDomain` configs with the
   values corresponding to your project.
1. Open another shell.
1. On `frontend/`, run `docker build -t frontend .`
1. Run `docker run -it --rm -p 8080:8080 frontend`

### How the app works

1. Open `http://localhost:8080/` on your browser.
1. You may be requested to log into the service with an E-mail address.
   If you turned the "Enable create (sign-up)" option on, the sign-in form also works to
   sign-up a new user.
1. After logging into the service, you may see two buttons: "Fetch backend" and "Sign
   out". "Fetch backend" invokes the backend server with the obtained ID token, and
   returns a user-specific data: the name of the user.
