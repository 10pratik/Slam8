from django.shortcuts import render
from apps.slamitsaas.models import GlobalUsers
from django.contrib.auth.hashers import PBKDF2PasswordHasher
import datetime 
from django.http import HttpResponse


# Create your views here.
def signup(request):
	if request.POST:
		hasher = PBKDF2PasswordHasher()
		signup_details = GlobalUsers()
		signup_details.gus_username= request.POST.get('first_name') +' '+ request.POST.get('last_name') 
		signup_details.gus_password = hasher.encode(password= request.POST.get('password'), salt='salt',iterations= 50000)
		signup_details.gus_email = request.POST.get('email')
		signup_details.gus_sex = request.POST.get('gender')
		signup_details.gus_createdon = datetime.datetime.now()
		signup_details.gus_createdby = request.POST.get('first_name')
		signup_details.gus_modifiedby = request.POST.get('first_name')
		signup_details.gus_isused = 0
		signup_details.save()

	return render(request,'login/index.html')


