from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='todos'
    )

    def __str__(self) -> str:
        return self.name
