from django.db import models

# Create your models here.
class CowsText(models.Model):
    text = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.text
