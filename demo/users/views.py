from django.shortcuts import render

# Create your views here.

def users_register(request):
    return render(request, 'users/register.html')