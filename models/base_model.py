#!/usr/bin/python3
"""

"""

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """

        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """

        """
        pass


if __name__ == "__main__":
    my_model = BaseModel()
    my_model_name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
