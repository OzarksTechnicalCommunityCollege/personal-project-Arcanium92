from django.contrib import admin
from .models import GameReview, Game, Genre
from django.http import HttpResponse
import csv


@admin.action(description="Export selected reviews to CSV")
def export_review_csv(modeladmin, request, queryset):
    """ Custom admin action: Export selected objects as CSV file"""
    response = HttpResponse(content_type='text/csv')
    response ['Content-Disposition'] = 'attachment; filename="game_reviews.csv"'

    writer = csv.writer(response)
    writer.writerow(['Title', 'Reviewer', 'Rating', 'Submission Date'])

    for review in queryset:
        writer.writerow([
            review.title,
            review.reviewer,
            review.rating,
            review.submission
        ])
    return response

# List view, filters and search bar for columns
@admin.register(GameReview)
class GameReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'reviewer', 'rating', 'submission', 'created')
    list_filter = ('rating', 'submission', 'created')
    search_fields = ('title', 'reviewer', 'review_text')
    ordering = ('-created',)
    readonly_fields = ('created', 'updated', 'submission')

# Game admin model
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
# Genre admin model    
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
        'game',
        'price',
        'image_preview',
    )
    list_filter = ('game',)
    search_fields = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return obj.image.url
        return "No image"