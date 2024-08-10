from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Story, Contribution

@login_required
def story_list(request):
    stories = Story.objects.all()
    return render(request, 'core/story_list.html', {'stories': stories})

@login_required
def story_detail(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    return render(request, 'core/story_detail.html', {'story': story})

@csrf_exempt
@login_required
def add_contribution(request, story_id):
    if request.method == 'POST':
        story = get_object_or_404(Story, id=story_id)
        contribution_text = request.POST.get('text')
        Contribution.objects.create(story=story, text=contribution_text, contributed_by=request.user)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

@login_required
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('story_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('story_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('story_list')
