from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    money = models.BigIntegerField(blank=True, default=0)

class Logs(models.Model):
    id = models.BigAutoField(primary_key=True)
    logger = models.ForeignKey(User, on_delete=models.CASCADE)
    log = models.TextField(max_length=100, null=True)
    madeAt = models.DateTimeField(default=timezone.now)