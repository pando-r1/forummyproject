from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # is_moderator= models.BooleanField(null=True, verbose_name="Is moderator")
    images= models.ImageField(upload_to="user_images/", blank=True)

    class Meta:
        db_table = "User"
        verbose_name='Пользователь'
        verbose_name_plural='Пользователи'