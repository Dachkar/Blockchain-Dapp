from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

"each class is its own table in DB"
class Post(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    "Foreign key --> One user has many posts, but each post only has one user"
    "Models cascade deletes the post if author User is deleted"
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} item'


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Transactions(models.Model):
    item = models.TextField()
    buyer = models.TextField()

