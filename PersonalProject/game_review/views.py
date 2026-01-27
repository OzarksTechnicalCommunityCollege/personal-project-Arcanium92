from django.shortcuts import render, review
from .models import GameReview
from .forms import GameReviewForm

# Create your views here.
def review_list(request):
    reviews = GameReview.objects.all()
    return render(request, "review/home.html", {"reviews": reviews})

def add_review(request):
    if request.method == "POST":
        form = GameReviewForm(request.POST)
        if form.is_valid():
            form.save()
            
            return render(request, "review/review_result.html", {"review": review})
    else:
        form = GameReviewForm()
    return render(request, "add_review/add_review.html", {"form": form})