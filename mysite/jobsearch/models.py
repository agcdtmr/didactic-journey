from django.db import models

# Create your models here.
class JobsSearchDB(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# class JobsItem(models.Model):
#     jobsDB = models.ForeignKey(JobsSearchDB, on_delete=models.CASCADE)
#     text = models.CharField(max_length=300)
#     complete = models.BooleanField()
#
#     def __str__(self):
#         return self.text


class Users(models.Model):
    # jobsDB = models.ForeignKey(JobsSearchDB, on_delete=models.CASCADE)
    user_ID = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    first_name = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class SavedJobs(models.Model):
    jobsDB = models.ForeignKey(JobsSearchDB, on_delete=models.CASCADE)
    saved_job_ID = models.AutoField(primary_key=True, unique=True)
    Saved_user_ID = models.ForeignKey(Users, on_delete=models.CASCADE)
    employerID = models.IntegerField(default=0)
    employerName = models.CharField(max_length=200)
    expirationDate = models.CharField(max_length=200)
    jobDescription = models.CharField(max_length=20000)
    jobID = models.IntegerField(default=0)
    jobTitle = models.CharField(max_length=200)
    jobURL = models.URLField()
    locationName = models.CharField(max_length=100)
    maximumSalary = models.IntegerField(default=0)
    minimumSalary = models.IntegerField(default=0)
    applied_for_job = models.CharField(max_length=4)

    def __str__(self):
        return self.jobTitle
