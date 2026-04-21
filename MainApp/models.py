from django.contrib.auth.models import User
from django.db import models


class Skill(models.Model):
    """A skill or service post offered by a student."""

    CATEGORY_CHOICES = [
        ('Tutoring', 'Tutoring'),
        ('Design', 'Design'),
        ('Programming', 'Programming'),
        ('Writing', 'Writing'),
        ('Other', 'Other'),
    ]

    CONTACT_CHOICES = [
        ('Email', 'Email'),
        ('Phone', 'Phone'),
        ('Message', 'In-App Message'),
    ]

    AVAILABILITY_CHOICES = [
        ('Available', 'Available'),
        ('Busy', 'Busy'),
        ('Closed', 'Closed'),
    ]

    title = models.CharField(max_length=120)
    description = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='Other')
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    is_free = models.BooleanField(default=False)
    contact_preference = models.CharField(max_length=20, choices=CONTACT_CHOICES, default='Email')
    availability_status = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='Available')
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} ({self.owner.username})'

    def price_display(self):
        """Return a human-friendly price label."""
        if self.is_free:
            return 'Free'
        return f'${self.price:.2f}' if self.price is not None else 'Contact for price'


class Review(models.Model):
    """A review left by a student for a skill."""

    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.rating}/5 by {self.reviewer.username}'


class BookingRequest(models.Model):
    """A booking request for a skill session."""

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    ]

    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='requests')
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_requests')
    message = models.TextField(blank=True)
    requested_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Request by {self.requester.username} for {self.skill.title}'
