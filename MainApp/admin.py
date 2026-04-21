from django.contrib import admin

from .models import BookingRequest, Review, Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'category', 'availability_status', 'created_at')
    list_filter = ('category', 'availability_status')
    search_fields = ('title', 'description', 'owner__username')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('skill', 'reviewer', 'rating', 'created_at')
    search_fields = ('skill__title', 'reviewer__username', 'comment')


@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ('skill', 'requester', 'status', 'requested_date', 'created_at')
    list_filter = ('status',)
    search_fields = ('skill__title', 'requester__username', 'message')
