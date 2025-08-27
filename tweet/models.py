from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=280)
    picture = models.ImageField(upload_to='tweet_pics/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Tweet by {self.user.username} at {self.created_at}"