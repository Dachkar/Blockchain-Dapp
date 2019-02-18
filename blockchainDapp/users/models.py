from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    money = models.DecimalField(max_digits=8, decimal_places=2, default=500)

    def __str__(self):
        return f'{self.user.username} Profile'



class Store(models.Model):
    sellerId = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name} item'
