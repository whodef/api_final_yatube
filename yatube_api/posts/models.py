from django.contrib.auth import get_user_model
from django.db import models
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

User = get_user_model()


class Post(models.Model):
    """Для Post доступны методы GET, POST, PUT, PATCH, DELETE."""

    ALLOWED_NUMBER_OF_CHAR_TEXT = 1024

    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        'Group', on_delete=models.SET_NULL,
        related_name='posts', null=True, blank=True)

    def __str__(self):
        return self.text[:self.ALLOWED_NUMBER_OF_CHAR_TEXT]


class Comment(models.Model):
    """Для Comment доступны методы GET, POST, PUT, PATCH, DELETE."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model, GenericViewSet, CreateModelMixin, ListModelMixin):
    """Для Follow доступны только методы GET и POST."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'], name='unique_name')
        ]


class Group(models.Model):
    """Для Group доступен только метод GET."""

    title = models.CharField(max_length=42)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title
