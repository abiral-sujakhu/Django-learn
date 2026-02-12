from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  #User is a pre-built Django model

class Post(models.Model):   # models.Model is the base class for all Django models 
                            # Without models.Model ❌ → Django won’t treat it as a database model.
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User, on_delete=models.CASCADE)  # author delete then post also delete,

    def __str__(self):
        return self.title