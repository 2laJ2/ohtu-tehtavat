import re
from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")
        
        if len(username) >= 3:
            if not(re.match("^[a-zA-Z]+$", username)):
                raise AuthenticationError("Username contains invalid characters")

        else:
            raise AuthenticationError("Username minimum length 3 characters")

        if username == self._user_repository.find_by_username(username):
            raise AuthenticationError("Username already taken")

        if len(password) >= 8:
            if (re.match("^[a-zA-Z]+$", password)):
                raise AuthenticationError("Password must not contain letters only")

        else:
            raise AuthenticationError("Password minimum length 8 characters")

        if password != password_confirmation:
            raise AuthenticationError("Passwords do not match")

user_service = UserService()
