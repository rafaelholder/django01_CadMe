from django.shortcuts import render
from .models import User

def home(request):
    return render(request, 'usuarios/home.html')

def users(request):
    #SAVING USER DATA
    new_user = User()
    new_user.user_name = request.POST.get('user_name')
    new_user.user_email = request.POST.get('user_email')
    new_user.user_birth_year = request.POST.get('user_birth_year')
    new_user.user_course = request.POST.get('user_course')
    new_user.save()

    #GET ALL USERS
    users = {
        'users': User.objects.all()
    }
    #RETURNING DATA
    return render(request, 'usuarios/users.html', users)
    