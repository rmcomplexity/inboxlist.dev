import logging
from dataclasses import asdict
from flask import Blueprint, request
from app.models.signup import SignupFormRequest
from app.models.responses.signup import SignupResponse, SignupErrorResponse
from exceptions.validation import ValidationError

LOG = logging.getLogger(__name__)

__all__ = ["signup"]

signup = Blueprint('signup', __name__, url_prefix="/v1/signup")

def _error_response(sfr: SignupFormRequest, exc: ValidationError) -> SignupResponse:
    """Returns correct error response.

    If the validation error is on the honeypot field then we return a successfull message
    with an error to tell the front-end to show a successful message but the signup
    did not actually go through.

    sfr (SignupFormRequest): Form data instance.

    returns: SignupResponse
    """
    error = SignupErrorResponse(
        field_name=exc.field_name, message=exc.message
    )

    response = SignupResponse(
        success=False,
        error=error,
        message="Signup form error.",
        request=sfr
    )
    return response

def _success_response(sfr: SignupFormRequest) -> SignupResponse:
    """Returns success response.

    sfr (SignupFormRequest): Form data istance.

    returns: SignupResponse
    """
    return SignupResponse(
        success=True,
        error=SignupErrorResponse(),
        message="Successfully signed up",
        request=sfr
    )


@signup.route("", methods=["POST"])
def signup_form():
    """Handler for signup form."""
    sfr = SignupFormRequest(**request.get_json())
    try :
        sfr.validate()
    except ValidationError as exc:
        LOG.exception(exc)
        return asdict(_error_response(sfr, exc)), 400

    return asdict(_success_response(sfr)), 200
