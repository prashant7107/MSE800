import hashlib


class SecurityHelper:
    # class for hashing password.

    @staticmethod
    def hash_data(data: str) -> str:
        # Hash plain text using SHA-256 for security.
        return hashlib.sha256(data.encode()).hexdigest()