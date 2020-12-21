import pytest
from app.models.signup import SignupFormRequest
from app.models.responses.signup import SignupResponse, SignupErrorResponse

def _signup_post(
    client, name: str="name",
    email: str="e@mail.com", honeypot: bool=False,
) -> SignupResponse:
    """Do a POST with correct data to signup form.

    returns: SignupResponse
    """
    res = client.post(
        "/v1/signup",
        json={
            "name": name,
            "email": email,
            "honeypot": honeypot
        }
    )
    data = res.get_json()
    req = SignupFormRequest(**data.pop("request", {}))
    error = SignupErrorResponse(**data.pop("error", {}))
    return SignupResponse(**data, error=error, request=req), res

def _build_signup_response(
    name: str="name", email: str="e@mail.com",
    honeypot: bool=False, message: str="Successfully signed up",
    error_message: str=None, error_field: str=None
) -> SignupResponse:
    """Builds a signup response.

    :param bool error: Should the response have an error or not.
    
    returns: SignupResponse
    """
    err = SignupErrorResponse()
    success = True

    if error_message and error_field:
        err = SignupErrorResponse(message=error_message, field_name=error_field)
        success = False

    req = SignupFormRequest(name=name, email=email, honeypot=honeypot)
    return SignupResponse(
        message=message, success=success, request=req, error=err
    )


def test_signup_form(client):
    """Success signup test.

    GIVEN correct form data
    WHEN submitting a POST
    THEN a success response is returned.
    """
    name="Juan Pérez"
    email="jperez@congolomo.com"
    honeypot=False
    actual, res = _signup_post(client, name, email, honeypot)

    expected = _build_signup_response(
        name=name, email=email, honeypot=honeypot
    )
    assert actual == expected
    assert res.status_code == 200


def test_signup_form_error(client):
    """Form error signup test.

    GIVEN missing or malformed request data
    WHEN submitting a POST
    THEN an error response is returned.
    """
    name="Juan Pérez"
    email="not an email"
    honeypot=False
    actual, res = _signup_post(client, name, email, honeypot)

    expected = _build_signup_response(
        name=name, email=email, honeypot=honeypot,
        message="Signup form error.",
        error_message="Not a valid email address.",
        error_field="email"
    )
    assert actual == expected
    assert res.status_code == 400

def test_signup_form_honeypot(client):
    """Form honeypot test.

    GIVEN honeypot value in data
    WHEN submitting a POST
    THEN a successfull response with an error field is returned.
    """
    name="Juan Pérez"
    email="jperez@congolomo.com"
    honeypot=True
    actual, res = _signup_post(client, name, email, honeypot)

    expected = _build_signup_response(
        name=name, email=email, honeypot=honeypot,
        message="Signup form error.",
        error_field="honeypot",
        error_message="Cannot be True."
    )

    assert actual == expected
    assert res.status_code == 400
