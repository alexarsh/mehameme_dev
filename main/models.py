from django.db import models
from django.contrib.auth.models import User

class Meme(models.Model):
    user = models.ForeignKey(User, related_name="memes")
    picture = models.ImageField(upload_to="/images")
