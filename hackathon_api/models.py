from django.db import models

# Create your models here.
class Hackathon(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    background_image = models.ImageField(upload_to='hackathon_backgrounds/')
    hackathon_image = models.ImageField(upload_to='hackathon_images/')
    submission_types = [
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link'),
    ]
    submission_type = models.CharField(max_length=10, choices=submission_types)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.DecimalField(max_digits=10, decimal_places=2)