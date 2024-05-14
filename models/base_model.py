#!/usr/bin/env python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    This defines all common attributes or methods for other classes
    """
    def __init__(self):
        self.id = uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
