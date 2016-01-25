from django.shortcuts import render
from apps.slamitsaas.models import *
import datetime 

# Create your views here.
def login(request):
	# global_user =  GlobalUsers()
	# global_user.gus_username = 'Subham'
	# global_user.gus_age = 22
	# global_user.gus_address = 'chennai'
	# global_user.gus_phone = 949
	# global_user.gus_createdon = datetime.datetime.now()
	# global_user.gus_createdby = 'subham'
	# global_user.gus_modifiedon = datetime.datetime.now()
	# global_user.gus_modifiedby = datetime.datetime.now()
	# global_user.gus_isused = 0
	# global_user.gus_sex = "Male"
	# global_user.gus_password = 'admin'
	# global_user.save()
	return render (request, 'login/index.html')

