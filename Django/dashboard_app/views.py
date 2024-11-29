from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from register_app.models import Members
from django.http import JsonResponse
from .models import Event,Task, Meeting

#DISPLAY
def dashboard_view(request):
    print(f"User is authenticated: {'member_id' in request.session}")

    context = {
        'fname': 'Guest',
        'lname': '',
        'user_role': None,
        'events': Event.objects.all(), #display events
        'tasks': Task.objects.all(), #display tasks
        'meetings': Meeting.objects.all(),
        'members': Members.objects.all()
    }

    if 'member_id' in request.session:
        member_id = request.session['member_id']
        try:
            member = Members.objects.get(id=member_id)
            print(f"Member found: {member}") 
            context['fname'] = member.fname
            context['lname'] = member.lname
            context['user_role'] = member.user_role
            context['member'] = member
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

def getTask(request):
    tasks = Task.objects.all()
    task_data = []
    for task in tasks:
        task_data.append({
        'dateAssigned': task.dateAssigned,
        'taskTitle': task.taskTitle,
        'taskDescription': task.taskDescription,
        'dueDate': task.dueDate,
        })
    return JsonResponse(task_data, safe =False)

def addTasks(request):
     if request.method == 'POST':
        member_id = request.POST.get('member_id')
        dateAssigned = timezone.now().date()
        taskTitle = request.POST.get('taskTitle')
        taskDescription = request.POST.get('taskDescription')
        dueDate = request.POST.get('dueDate')
        member_id = request.POST.get('member_id')  # Get selected member ID 

        if not member_id:
            return render(request, 'dashboard/add_task.html', {'error': "Please select a member."})


        member = get_object_or_404(Members, id=member_id)

        Task.objects.create(
            dateAssigned=dateAssigned,
            taskTitle=taskTitle,
            taskDescription=taskDescription,
            dueDate=dueDate,
            assignTo =member
        )
        return redirect(dashboard_view) 
     
     members = Members.objects.all() 
     return render(request, 'dashboard.html',{'members': members})

# Create a new meeting
def addMeeting(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        date_time = request.POST.get('date_time')

        Meeting.objects.create(
            title=title,
            description=description,
            location=location,
            dateTime=date_time
        )
        return redirect(dashboard_view)  # Redirect back to the dashboard
    
    return render(request, 'dashboard.html')

# Delete a meeting
def deleteMeeting(request, meeting_id):
    if request.method == 'POST':
        meeting = get_object_or_404(Meeting, id=meeting_id)
        meeting.delete()
        return redirect('dashboard')
    
def get_meeting(request):
    meetings = Meeting.objects.all()  # Corrected: Use the Meeting model
    meeting_data = []
    for meeting in meetings:
        meeting_data.append({
            'title': meeting.title,
            'start': meeting.dateTime.isoformat(),  
            'description': meeting.description,
        })
    return JsonResponse(meeting_data, safe=False)  # Moved outside of the loop

# Update an existing meeting
def updateMeeting(request):
    if request.method == 'POST':
        meeting_id = request.POST.get('meeting_id')
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        date_time = request.POST.get('date_time')

        meeting = get_object_or_404(Meeting, id=meeting_id)
        meeting.title = title
        meeting.description = description
        meeting.location = location
        meeting.dateTime = date_time
        meeting.save()

        return redirect('dashboard')

    return render(request, 'dashboard.html')




     