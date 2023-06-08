from django.db import models
from django.conf import settings
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from hackathon_api.models import Hackathon

class Submission(models.Model):
    SUBMISSION_TYPES = [
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    summary = models.TextField()
    submission_type = models.CharField(choices=SUBMISSION_TYPES, max_length=10)
    submission_url = models.CharField(max_length=255, validators=[URLValidator()], blank=True, null=True)
    submission_file = models.FileField(upload_to='submissions/', blank=True, null=True)

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        


    def save(self, *args, **kwargs):
        
        if self.hackathon.submission_type != self.submission_type:
            raise ValidationError('Invalid submission type for the hackathon.')

        return super().save(*args, **kwargs)
