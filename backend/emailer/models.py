from core.models import BaseModel
from django.db import models


class Newsletter(BaseModel):
    email = models.EmailField(db_index=True)

    def __str__(self):
        return self.email
