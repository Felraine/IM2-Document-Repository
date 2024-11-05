from django.shortcuts import redirect, render
from register_app.models import Members
from .models import Event

def dashboard_view(request):
    print(f"User is authenticated: {'member_id' in request.session}")

    context = {
        'fname': 'Guest',
        'lname': '',
        'user_role': None,
        'events': Event.objects.all() #display events
    }

    if 'member_id' in request.session:
        member_id = request.session['member_id']
        try:
            member = Members.objects.get(id=member_id)
            print(f"Member found: {member}") 
            context['fname'] = member.fname
            context['lname'] = member.lname
            context['user_role'] = member.user_role
        except Members.DoesNotExist:
            print("Member does not exist")

    return render(request, './dashboard.html', context)

def addEvent(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        date_time = request.POST.get('date_time')

        Event.objects.create(
            title=title,
            description=description,
            location=location,
            dateTime=date_time
        )
        return redirect(dashboard_view) 
    

    return render(request, 'dashboard.html')
        