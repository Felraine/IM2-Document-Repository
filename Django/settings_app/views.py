from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def settings_view(request):
    # Logic to render your settings page
    dark_mode = request.session.get('dark_mode', False)  # Get dark mode status from session
    return render(request, 'settings.html', {'dark_mode': dark_mode})

@login_required
def toggle_dark_mode(request):
    if request.method == 'POST':
        user_settings, created = UserSettings.objects.get_or_create(user=request.user)
        user_settings.dark_mode = not user_settings.dark_mode
        user_settings.save()
    return redirect('settings')  # Redirect back to the settings page

