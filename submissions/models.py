from django.contrib.auth import get_user_model
from django.db import models

from hackathon.models import Hackathon


class Submission(models.Model):
    name = models.CharField(max_length=255)
    summary = models.TextField()
    link = models.URLField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to='submissions/files/', blank=True, null=True)
    image = models.ImageField(upload_to='submissions/images/', blank=True, null=True)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE, related_name='submissions')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='submissions')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user}\'s submission for {self.hackathon.title}'
