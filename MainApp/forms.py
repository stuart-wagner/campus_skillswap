from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import BookingRequest, Review, Skill


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='A valid email address helps with password recovery.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = [
            'title',
            'description',
            'category',
            'price',
            'is_free',
            'contact_preference',
            'availability_status',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
        }
        help_texts = {
            'is_free': 'Mark this skill as free if you are not charging money.',
        }

    def clean(self):
        cleaned = super().clean()
        is_free = cleaned.get('is_free')
        price = cleaned.get('price')

        if is_free:
            cleaned['price'] = 0

        if not is_free and not price:
            self.add_error('price', 'Enter a price or mark the skill as free.')

        return cleaned


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3}),
        }


class BookingRequestForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = ['message', 'requested_date']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3}),
            'requested_date': forms.DateInput(attrs={'type': 'date'}),
        }
