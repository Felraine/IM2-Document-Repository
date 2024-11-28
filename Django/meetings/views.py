from django.shortcuts import render
from register_app.models import Members
from .models import RoomMember
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
import random
import time
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def lobby(request):
    print(f"User is authenticated: {'member_id' in request.session}")

    context = {
        'fname': 'Guest',
        'lname': '',
        'user_role': None,
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

            request.session['fname'] = member.fname
            request.session['lname'] = member.lname

        except Members.DoesNotExist:
            print("Member does not exist")

    return render(request, './lobby.html', context)

def room(request):
    return render(request, 'room.html')

def getToken(request):
    appId = 'fd6776f642cf4c4783a18c670407df19'
    appCertificate = '12aa3d529f884618b1e9dc31d5ebace5' 
    channelName = request.GET.get('channel')
    uid = random.randint(1,230)
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1
    
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    fname = request.session.get('fname', 'Guest')
    lname = request.session.get('lname', '')
    full_name = f"{fname} {lname}".strip()

    return JsonResponse({'token':token, 'uid':uid, 'name': full_name}, safe=False)

@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)