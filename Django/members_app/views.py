from django.shortcuts import render, redirect
from register_app.models import Members

def members_view(request):
    print(f"User is authenticated: {'member_id' in request.session}")

    context = {
        'fname': 'Guest',
        'lname': '',
        'user_role': None,
        'members': [],
        'member_count': 0,
    }

    if 'member_id' in request.session:
        member_id = request.session['member_id']
        try:
            member = Members.objects.get(id=member_id)
            print(f"Member found: {member.fname} {member.lname}")
            context['fname'] = member.fname
            context['lname'] = member.lname
            context['user_role'] = member.user_role

            context['members'] = Members.objects.all()
            context['member_count'] = context['members'].count()
        except Members.DoesNotExist:
            print("Member not found.")
#adding new member
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = '123456'
        user_role = 0

        new_member = Members(
            fname=fname,
            lname=lname,
            email=email,
            password=password,
            user_role=user_role
        )
        new_member.save()

        return redirect('members')

    return render(request, 'members.html', context)
