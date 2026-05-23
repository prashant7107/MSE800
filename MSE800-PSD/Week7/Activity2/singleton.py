# SINGLETON PATTERN BASE
class Singleton:
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance