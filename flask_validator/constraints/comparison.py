from flask_validator import Validator


class BaseComparision(Validator):
    """ Base Comparision Class
    """
    value = None

    def __init__(self, field, value, throw_exception=False):
        self.value = value

        Validator.__init__(self, field, throw_exception)


class ValidateLessThan(BaseComparision):

    """ Validate Less Than X

    Check if the new value has a value less than x

    Args:
        field: SQLAlchemy column to validate
        value: Value to check
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    def check_value(self, value):
        return value < self.value


class ValidateLessThanOrEqual(BaseComparision):
    """ Validate Less Than X Or Equal

    Check if the new value has a value less than x or equal

    Args:
        field: SQLAlchemy column to validate
        value: Value to check
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    def check_value(self, value):
        return value <= self.value


class ValidateGreaterThan(BaseComparision):
    """ Validate Greater Than X

    Check if the new value has a value greater than x

    Args:
        field: SQLAlchemy column to validate
        value: Value to check
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    def check_value(self, value):
        return value > self.value


class ValidateGreaterThanOrEqual(BaseComparision):
    """ Validate Greater Than X Or Equal

    Check if the new value has a value greater than x

    Args:
        field: SQLAlchemy column to validate
        value: Value to check
        throw_exception: (bool) Throw a ValueError if the validation fails

    """

    def check_value(self, value):
        return value >= self.value
