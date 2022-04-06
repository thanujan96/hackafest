from fileinput import filename
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.core.files.base import ContentFile


class ResizeImageMixin:
    def resize(self, imageField: models.ImageField, size: tuple):
        im = Image.open(imageField)  # Catch original
        source_image = im.convert("RGB")
        source_image.thumbnail(size)  # Resize to size
        output = BytesIO()
        source_image.save(output, format="JPEG")  # Save resize image to bytes
        output.seek(0)

        content_file = ContentFile(
            output.read()
        )  # Read output and create ContentFile in memory
        file = File(content_file)

        random_name = f"{uuid.uuid4()}.jpeg"
        imageField.save(random_name, file, save=False)


# Create your models here.


class User(AbstractUser, ResizeImageMixin):
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

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.resize(self.thumb, (200, 200))
        super().save(*args, **kwargs)


class Collection(models.Model):
    collectionName = models.CharField(max_length=30, unique=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)


class CSVFile(models.Model):
    collectionId = models.ForeignKey(Collection, on_delete=models.CASCADE)
    fileName = models.CharField(max_length=30)
    csvFile = models.FileField(upload_to="bioWeb/csvFiles")
    fileType = models.CharField(max_length=20)
