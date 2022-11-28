from django.contrib import admin
from .models import JobsSearchDB, Users, SavedJobs

# Register your models here.
admin.site.register(JobsSearchDB)
admin.site.register(Users)
admin.site.register(SavedJobs)
