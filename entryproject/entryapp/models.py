from django.db import models

# Create your models here.


class EntryModel(models.Model):
    title = models.CharField(max_length=50)
    entry_text = models.CharField(max_length=500)
