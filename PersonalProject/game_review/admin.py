from django.contrib import admin
from .models import GameReview

# Register your models here.

# List view, filters and search bar for columns
@admin.register(GameReview)
class GameReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'reviewer', 'rating', 'submission', 'created')
    list_filter = ('rating', 'submission', 'created')
    search_fields = ('title', 'reviewer', 'review_text')
    ordering = ('-created',)
    readonly_fields = ('created', 'updated', 'submission')