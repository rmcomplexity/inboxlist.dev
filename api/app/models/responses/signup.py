from dataclasses import dataclass
from app.models.signup import SignupFormRequest


@dataclass(frozen=True)
class SignupErrorResponse:
    message: str = ""
    field_name: str = ""

@dataclass(frozen=True)
class SignupResponse:
    message: str
    success: bool
    request: SignupFormRequest
    error: SignupErrorResponse = SignupErrorResponse()
