from django.contrib.auth.models import User
from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contribution(models.Model):
    story = models.ForeignKey(Story, related_name='contributions', on_delete=models.CASCADE)
    text = models.TextField()
    contributed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    contributed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.contributed_by.username}: {self.text[:30]}...'
