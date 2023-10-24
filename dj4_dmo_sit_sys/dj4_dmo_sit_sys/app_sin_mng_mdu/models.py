from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SigninLog(models.Model):
    user_id = models.ForeignKey(User, related_name="signin_log", on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    signin_datetime = models.DateTimeField(auto_now_add=True)

    # Metadata
    class Meta:
        db_table = "app_sin_mng_mdu_signin_log"
        ordering = ["user_id", "signin_datetime"]
