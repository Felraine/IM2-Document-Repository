from django.shortcuts import get_object_or_404, redirect, render
from register_app.models import Members
from django.http import JsonResponse
from .models import Event

#DISPLAY
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

#CREATE
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

#DELETE
def deleteEvent(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(Event, id = event_id)
        event.delete()
        return redirect('dashboard')
    
#UPDATE
def updateEvent(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        date_time = request.POST.get('date_time')

        event = get_object_or_404(Event, id=event_id)
        event.title = title
        event.description = description
        event.location = location
        event.dateTime = date_time
        event.save()

        return redirect('dashboard')
    
    return render(request, 'dashboard.html')
        
def get_events(request):
    events = Event.objects.all()
    event_data = []
    for event in events:
        event_data.append({
            'title': event.title,
            'start': event.dateTime.isoformat(),  
            'description': event.description,
        })
    return JsonResponse(event_data, safe=False)