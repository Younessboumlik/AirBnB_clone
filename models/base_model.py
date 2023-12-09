#!/usr/bin/python3
"""We will create the first class that we will use in the program."""
import uuid
import datetime

class BaseModel():
    """the basic class."""
    def __init__(self):
        self.id = id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    def save(self):
        self.updated_at = datetime.now()


