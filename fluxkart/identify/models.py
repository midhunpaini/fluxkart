from django.db import models

# Create your models here.
class Contact(models.Model):
    phoneNumber = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    linkedId = models.IntegerField(null=True)
    linkPrecedence = models.CharField(max_length=10)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField(null=True)

    def __str__(self):
        return f"Contact {self.id}"