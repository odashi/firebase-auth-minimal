"""A backend server working with Firebase Authentication."""

from typing import Any, Mapping

from fastapi import FastAPI, HTTPException, Request, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

import google.auth.transport.requests
import google.oauth2.id_token

audience = "### GOOGLE CLOUD PROJECT NAME ###"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_headers=["Authorization"],
)

http_request = google.auth.transport.requests.Request()


def authorize(
    request: Request,
    authorization: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> Mapping[str, Any]:
    try:
        token = google.oauth2.id_token.verify_firebase_token(
            authorization.credentials,
            http_request,
            audience=audience,
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
        )
    return token


@app.get("/")
def get_root(token: Mapping[str, Any] = Depends(authorize)):
    return {"name": f"{token['name']}"}
