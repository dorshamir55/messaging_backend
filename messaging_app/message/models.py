from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=255, null=False)
    recipient = models.CharField(max_length=255, null=False)
    message = models.TextField(max_length=2000)

    class Meta:
        db_table = "message"