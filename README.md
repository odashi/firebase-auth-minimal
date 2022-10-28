# Firebase Auth Minimal App

This example contains a minimal example Web application working with Firebase
Authentication and/or Google Identity Platform.

## Getting Started

1. Prepare a Google Cloud project.
1. Enable Identity Platform from the marketplace.
1. Add an Email provider.
1. Open `frontend/static/main.js` and replace `apiKey` and `authDomain` configs with
   values on your project.
1. On `frontend/`, run `docker build -t frontend .`
1. Run `docker run -it --rm -p 8080:8080 frontend`
1. Open `https://localhost:8080` on your browser and check if the page works.
