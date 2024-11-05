from django.shortcuts import render, redirect
from register_app.models import Members

def members_view(request):
    print(f"User is authenticated: {'member_id' in request.session}")

    # Initialize attributes for the html
    context = {
        'fname': 'Guest',
        'lname': '',
        'user_role': None,
        'members': [],
        'member_count': 0,
        'user_role_display': "Member"
    }

    # Read the info from the table
    if 'member_id' in request.session:
        member_id = request.session['member_id']
        try:
            member = Members.objects.get(id=member_id)
            print(f"Member found: {member.fname} {member.lname}")
            context['fname'] = member.fname
            context['lname'] = member.lname
            context['user_role'] = member.user_role
            context['user_role_display'] = "Admin" if member.user_role == 1 else "Member"
            context['members'] = Members.objects.all()
            context['member_count'] = context['members'].count()
        except Members.DoesNotExist:
            print("Member not found.")

    # Edit role
    if request.method == 'POST' and 'change_role' in request.POST:
        if context['user_role'] == 1:
            member_id_to_change = request.POST.get('member_id')
            new_role = request.POST.get('new_role')
            
            try:
                member_to_change = Members.objects.get(id=member_id_to_change)
                member_to_change.user_role = int(new_role)
                member_to_change.save()
                print(f"Changed role for {member_to_change.fname} {member_to_change.lname} to {'Admin' if member_to_change.user_role == 1 else 'Member'}")
                return redirect('members')  
            except Members.DoesNotExist:
                print("Member to change not found.")
        else:
            print("Non-admin user attempted to change role.")

    # Adding new member
    if request.method == 'POST' and 'add_member' in request.POST:
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

    # Edit member details
    if request.method == 'POST' and 'edit_member' in request.POST:
        member_id_to_edit = request.POST.get('member_id')
        new_email = request.POST.get('email')
        new_password = request.POST.get('password')

        try:
            member_to_edit = Members.objects.get(id=member_id_to_edit)

            if context['user_role'] == 1 or member_to_edit.id == member_id:
                member_to_edit.email = new_email
                member_to_edit.password = new_password
                member_to_edit.save()
                print(f"Updated {member_to_edit.fname}'s details.")
                return redirect('members')
            else:
                print("Non-admin user attempted to edit another user's details.")
        except Members.DoesNotExist:
            print("Member to edit not found.")

    # Delete member
    if request.method == 'POST' and 'delete_member' in request.POST:
        member_id_to_delete = request.POST.get('member_id')
        try:
            member_to_delete = Members.objects.get(id=member_id_to_delete)
            member_to_delete.delete()
            print(f"Member deleted: {member_to_delete.fname} {member_to_delete.lname}")
        except Members.DoesNotExist:
            print("Member to delete not found.")

        return redirect('members')

    return render(request, 'members.html', context)
