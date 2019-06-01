from django.db import models


class Hitter(models.Model):
    email = models.EmailField(max_length=300)
