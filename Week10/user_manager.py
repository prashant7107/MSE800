import sqlite3
from datetime import datetime
from database import DatabaseManager
from security import SecurityHelper


class UserManager:
    # Manage user account (Registration, Auth, Recovery).

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager


    def register_user(
        self, username, password, full_name, dob_str, sec_question, sec_answer
    ):
        # Registers a new user.
        if not self._validate_dob(dob_str):
            return False, "Invalid Date of Birth format. Use YYYY-MM-DD."

        password_hash = SecurityHelper.hash_data(password)
        answer_hash = SecurityHelper.hash_data(sec_answer.lower().strip())

        query = """
        INSERT INTO users (username, password_hash, full_name, dob, security_question, security_answer_hash)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        try:
            self.db.execute_query(
                query,
                (
                    username,
                    password_hash,
                    full_name,
                    dob_str,
                    sec_question,
                    answer_hash,
                ),
            )
            return True, "Registration successful!"
        except sqlite3.IntegrityError:
            return False, "Username already exists."

    def authenticate_user(self, username, password):
        # Verifiy user credentials for login.
        query = (
            "SELECT password_hash, full_name FROM users WHERE username = ?"
        )
        user = self.db.fetch_one(query, (username,))

        if user and user[0] == SecurityHelper.hash_data(password):
            # Return success state and user's Full Name
            return True, user[1]
        return False, "Invalid username or password."

    # Forgot Password Functionality

    def initiate_password_reset(self, username):
        # Retrieve the security question for a given username.
        query = "SELECT security_question FROM users WHERE username = ?"
        result = self.db.fetch_one(query, (username,))
        return result[0] if result else None

    def reset_password(self, username, security_answer, new_password):
        # Validate the security answer and updates the password.
        query = "SELECT security_answer_hash FROM users WHERE username = ?"
        result = self.db.fetch_one(query, (username,))

        if not result:
            return False, "User not found."

        provided_hash = SecurityHelper.hash_data(
            security_answer.lower().strip()
        )
        if result[0] != provided_hash:
            return False, "Incorrect security answer."

        # Update operation sub-step
        new_password_hash = SecurityHelper.hash_data(new_password)
        update_query = (
            "UPDATE users SET password_hash = ? WHERE username = ?"
        )
        self.db.execute_query(update_query, (new_password_hash, username))
        return True, "Password reset successfully!"


    def _validate_dob(self, dob_str):
        # sub-function to validate date formatting.
        try:
            datetime.strptime(dob_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False