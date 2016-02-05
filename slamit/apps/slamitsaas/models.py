from django.db import models

# Create your models here.
class GlobalUsers(models.Model):

    gus_user_id = models.AutoField(primary_key=True)
    gus_username = models.CharField(max_length=20)
    gus_email = models.CharField(max_length=100, blank=True, null=True)
    gus_age = models.IntegerField(null=True, blank= True)
    gus_address = models.CharField(max_length=100, blank=True)
    gus_phone = models.IntegerField(null=True)
    gus_createdon = models.DateTimeField(blank=True, null=True, auto_now_add = True)
    gus_createdby = models.CharField(max_length=30)
    gus_modifiedon = models.DateTimeField(blank=True)
    gus_modifiedby = models.CharField(blank=True,max_length=30)
    gus_isused = models.IntegerField(default=0)
    gus_sex = models.CharField(max_length=6)
    gus_password = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'global_users'

