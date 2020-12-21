from dataclasses import dataclass
from exceptions.validation import ValidationError

@dataclass(frozen=True)
class SignupFormRequest:
    """Singup Form Request."""
    name: str
    email: str
    honeypot: bool = False

    def validate(self) -> None:
        """Validate fields."""
        if not len(self.name):
            raise ValidationError("name", "Cannot be an empty string.")

        if "@" not in self.email:
            raise ValidationError("email", "Not a valid email address.")

        if self.honeypot:
            raise ValidationError("honeypot", "Cannot be True.")
