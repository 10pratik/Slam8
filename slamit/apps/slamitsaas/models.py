from django.db import models

# Create your models here.
class GlobalUsers(models.Model):

    gus_user_id = models.AutoField(primary_key=True)
    gus_username = models.CharField(max_length=20)
    gus_age = models.IntegerField()
    gus_address = models.CharField(max_length=100, blank=True)
    gus_phone = models.IntegerField()
    gus_createdon = models.DateTimeField(auto_now_add=True)
    gus_createdby = models.CharField(max_length=30)
    gus_modifiedon = models.DateTimeField()
    gus_modifiedby = models.CharField(max_length=30)
    gus_isused = models.IntegerField(default=0)
    gus_sex = models.CharField(max_length=6)
    gus_password = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'global_users'

