from django.contrib import admin
from .models import User, Collection, CSVFile

# Register your models here.
admin.site.register(User)
admin.site.register(Collection)
admin.site.register(CSVFile)
