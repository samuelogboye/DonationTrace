from core.models import BaseModel
from django.db import models


class ContactUs(BaseModel):
    email = models.EmailField(db_index=True)
    full_name = models.CharField(max_length=255)
    message = models.TextField()
    enquiry_type = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)

    def __str__(self):
        return self.email
