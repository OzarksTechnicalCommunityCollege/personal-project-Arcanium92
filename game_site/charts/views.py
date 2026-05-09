from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count, Max
from .models import ReviewRating

def chart_page(request):
    return render(request, 'dashboard.html')

def ratings_by_game_title(request):
    """Return top 5 titles as JSON response"""
    data = (
        ReviewRating.objects.values('gameName')
        .annotate(top_rating=Max('rating'))
        .order_by('gameName')
    )

    return JsonResponse({
        'labels': [row['gameName'] for row in data],
        'values': [row['top_rating'] for row in data],
    })

def totals_by_game_title(request):
    """Return total ratings as JSON response"""
    data = (
        ReviewRating.objects.values('gameName')
        .annotate(total_ratings = Count('rating'))
        .order_by('gameName')
    )

    return JsonResponse({
        'labels': [row['gameName'] for row in data],
        'values': [row['total_rating'] for row in data],
    })