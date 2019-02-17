from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

"each class is its own table in DB"
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    "Foreign key --> One user has many posts, but each post only has one user"
    "Models cascade deletes the post if author User is deleted"
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title