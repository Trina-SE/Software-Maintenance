"""
User Management Module - Refactored with improved naming and validation extraction.
"""

from typing import Dict, List, Optional


class UserValidator:

    MIN_NAME_LENGTH = 3
    MIN_PASSWORD_LENGTH = 6
    MIN_AGE = 18
    MAX_AGE = 120

    @staticmethod
    def validate_name(name: str) -> bool:
        return isinstance(name, str) and len(name) >= UserValidator.MIN_NAME_LENGTH

    @staticmethod
    def validate_email(email: str) -> bool:
        return isinstance(email, str) and "@" in email

    @staticmethod
    def validate_age(age: int) -> bool:
        return isinstance(age, int) and UserValidator.MIN_AGE <= age <= UserValidator.MAX_AGE

    @staticmethod
    def validate_password(password: str) -> bool:
        return isinstance(password, str) and len(password) >= UserValidator.MIN_PASSWORD_LENGTH

    @staticmethod
    def validate_user(name: str, email: str, age: int, password: str) -> bool:
        return (
            UserValidator.validate_name(name)
            and UserValidator.validate_email(email)
            and UserValidator.validate_age(age)
            and UserValidator.validate_password(password)
        )


class UserManager:

    MAX_USERS = 100

    def __init__(self):
        self.users: List[Dict[str, any]] = []

    def add_user(
        self, name: str, email: str, age: int, password: str
    ) -> bool:
        if len(self.users) >= self.MAX_USERS:
            return False

        if not UserValidator.validate_user(name, email, age, password):
            return False

        user = {
            "name": name,
            "email": email,
            "age": age,
            "password": password,
        }
        self.users.append(user)
        return True

    def remove_user(self, email: str) -> bool:
        user = self._find_user_by_email(email)
        if user:
            self.users.remove(user)
            return True
        return False

    def get_user(self, email: str) -> Optional[Dict]:
        return self._find_user_by_email(email)

    def update_user(self, email: str, name: str, age: int) -> bool:
        if not UserValidator.validate_name(name) or not UserValidator.validate_age(age):
            return False

        user = self._find_user_by_email(email)
        if user:
            user["name"] = name
            user["age"] = age
            return True
        return False

    def list_users(self) -> List[Dict]:
        return self.users.copy()

    def get_user_count(self) -> int:
        return len(self.users)

    def _find_user_by_email(self, email: str) -> Optional[Dict]:
        return next((u for u in self.users if u["email"] == email), None)
