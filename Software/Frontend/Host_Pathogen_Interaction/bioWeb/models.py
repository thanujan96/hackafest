from fileinput import filename
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Collection(models.Model):
    collectionName = models.CharField(max_length=30, unique=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)


class CSVFile(models.Model):
    collectionId = models.ForeignKey(Collection, on_delete=models.CASCADE)
    fileName = models.CharField(max_length=30)
    csvFile = models.FileField(upload_to="bioWeb/csvFiles")
