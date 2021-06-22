from django.db import models

from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.urls import reverse

from users.models import User
# Create your models here.




# class User(AbstractUser):
#     is_moderator= models.BooleanField(null=True, verbose_name="Is moderator")

#     class Meta:
#         db_table = "User"


class Category(models.Model):
    name = models.CharField(max_length=65, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "Category"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})


class Post(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE, related_name='post_user', verbose_name='Пользователь')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to="post_images/%Y/%m/%d/", blank=True, verbose_name='Изображение')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    moderation = models.BooleanField(default=True, verbose_name='Модерация')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_category',verbose_name='Категория')

    class Meta:
        db_table = "Post"


    def __str__(self):
        return f'{self.title} | {self.category.name}'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Comment(models.Model):
    post = ForeignKey(Post, on_delete=models.CASCADE, related_name='comments_post')
    user = ForeignKey(User, on_delete=models.CASCADE, related_name='comments_user')
    text = models.TextField()
    created = models.DateTimeField()
    # comments = models.TextField()

    class Meta:
        db_table = "Comment"


class Like(models.Model):
    user = ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')
    post = ForeignKey(Post, on_delete=models.CASCADE, related_name='like_post')

    class Meta:
        db_table = "Like"


# class img(models.Model):
#     user = ForeignKey(AbstractUser, on_delete=models.CASCADE)
#     name_file = models.CharField(max_length=100)
#     created = models.DateTimeField()
