class ValidationError(Exception):
    """Validation Error."""

    def __init__(self, field_name: str, message: str) -> None:
        self.field_name = field_name
        self.message = message

    def __str__(self) -> str:
        return f"ValidationError(field_name={self.field_name}, message={self.message})"

    def __repr__(Self) -> str:
        return self.__str__()
