from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookingRequestForm, ReviewForm, SkillForm, UserRegisterForm
from .models import BookingRequest, Review, Skill


def home(request):
    """Show the marketplace with search and all skill posts."""
    query = request.GET.get('q', '')
    skills = Skill.objects.all()

    if query:
        skills = skills.filter(
            Q(title__icontains=query) |
            Q(category__icontains=query)
        )
        messages.info(request, f'Searching for "{query}"')

    return render(request, 'MainApp/home.html', {
        'skills': skills,
        'query': query,
    })


def register(request):
    """Allow a new user to sign up."""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registration complete. You are now logged in.')
            return redirect('dashboard')
    else:
        form = UserRegisterForm()

    return render(request, 'MainApp/register.html', {'form': form})


def login_view(request):
    """Handle user login with username and password."""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, 'You are logged in.')
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'MainApp/login.html', {'form': form})


def logout_view(request):
    """Log a user out of the site."""
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


def skill_detail(request, pk):
    """Show details for one skill post, plus reviews and booking options."""
    skill = get_object_or_404(Skill, pk=pk)
    review_form = ReviewForm()
    request_form = BookingRequestForm()

    return render(request, 'MainApp/skill_detail.html', {
        'skill': skill,
        'review_form': review_form,
        'request_form': request_form,
    })


@login_required
def add_review(request, pk):
    """Save a review for a skill post."""
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.skill = skill
            review.reviewer = request.user
            review.save()
            messages.success(request, 'Thank you for your review.')
        else:
            messages.error(request, 'Please fix the review form errors.')
    return redirect('skill_detail', pk=pk)


@login_required
def send_booking_request(request, pk):
    """Create a booking/request for a skill session."""
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == 'POST':
        form = BookingRequestForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.skill = skill
            booking.requester = request.user
            booking.save()
            messages.success(request, 'Your request has been sent.')
        else:
            messages.error(request, 'Please fix the request form errors.')
    return redirect('skill_detail', pk=pk)


@login_required
def create_skill(request):
    """Allow a logged-in user to create a new skill post."""
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = request.user
            skill.save()
            messages.success(request, 'Skill post created successfully.')
            return redirect('skill_detail', pk=skill.pk)
    else:
        form = SkillForm()

    return render(request, 'MainApp/skill_form.html', {
        'form': form,
        'title': 'Create a Skill Post',
    })


@login_required
def update_skill(request, pk):
    """Allow the owner to edit a skill post."""
    skill = get_object_or_404(Skill, pk=pk)
    if skill.owner != request.user:
        messages.error(request, 'You cannot edit a skill you do not own.')
        return redirect('skill_detail', pk=pk)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill post updated successfully.')
            return redirect('skill_detail', pk=pk)
    else:
        form = SkillForm(instance=skill)

    return render(request, 'MainApp/skill_form.html', {
        'form': form,
        'title': 'Edit Skill Post',
    })


@login_required
def delete_skill(request, pk):
    """Allow the owner to delete a skill post."""
    skill = get_object_or_404(Skill, pk=pk)
    if skill.owner != request.user:
        messages.error(request, 'You cannot delete a skill you do not own.')
        return redirect('skill_detail', pk=pk)

    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill post deleted.')
        return redirect('dashboard')

    return render(request, 'MainApp/skill_confirm_delete.html', {'skill': skill})


@login_required
def dashboard(request):
    """Show the logged-in user's skills, requests, and reviews."""
    skills = request.user.skills.all()
    bookings = request.user.booking_requests.all()
    received_requests = BookingRequest.objects.filter(skill__owner=request.user)

    return render(request, 'MainApp/dashboard.html', {
        'skills': skills,
        'bookings': bookings,
        'received_requests': received_requests,
    })
