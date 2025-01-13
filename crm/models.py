import uuid
from django.db import models

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.BigIntegerField()
    address = models.CharField(max_length=25, blank=True)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        super().save(*args, **kwargs) 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"