from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Accounts(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	profile_picture = models.ImageField(upload_to='profile_pictures', default='profile_pictures/default.png')

	def __str__(self):
		return f'@{self.user.username}'
