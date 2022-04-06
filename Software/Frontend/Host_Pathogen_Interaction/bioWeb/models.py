from fileinput import filename
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    class Meta:
        app_label = "bioWeb"

    dob = models.DateField(
        blank=True,
        null=True,
        verbose_name="Day of birth",
    )

    thumb = models.ImageField(
        blank=True,
        upload_to="faces",
        verbose_name="Profile picture",
        help_text="extensions .png, .jpeg and .jpg will be accepted.",
    )

    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    address = models.CharField(max_length=100, blank=True)


class Collection(models.Model):
    collectionName = models.CharField(max_length=30, unique=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)


class CSVFile(models.Model):
    collectionId = models.ForeignKey(Collection, on_delete=models.CASCADE)
    fileName = models.CharField(max_length=30)
    csvFile = models.FileField(upload_to="bioWeb/csvFiles")
    fileType = models.CharField(max_length=20)
