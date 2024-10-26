from django.shortcuts import render, redirect
from .models import Members
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            member = Members.objects.get(email=email, password=password)
            request.session['member_id'] = member.id
            return redirect('calendar')  # successful login
        except Members.DoesNotExist:
            messages.error(request, 'Invalid email or password.')

    
    return render(request, "login.html") 
