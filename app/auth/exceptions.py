class UserDoesntExists(Exception):
	"""Raised when a requested user does not exist."""
	...


class UserAlreadyExists(Exception):
	"""Raised when a user with the same email already exists."""
	...


class PasswordIncorrect(Exception):
	"""Raised when a supplied password is incorrect."""
	...
