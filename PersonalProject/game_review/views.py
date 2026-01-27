from django.shortcuts import render, redirect
from .models import GameReview
from .forms import GameReviewForm
from django.core.paginator import Paginator

def review_list(request):
    reviews = GameReview.objects.all().order_by('-submission')

    paginator = Paginator(reviews, 3)  # 3 reviews per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "review/home.html", {"page_obj": page_obj})

def add_review(request):
    if request.method == "POST":
        form = GameReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect("review_result", pk=review.pk)
    else:
        form = GameReviewForm()
    return render(request, "add_review/add_review.html", {"form": form})

def review_result(request, pk):
    review = GameReview.objects.get(pk=pk)
    return render(request, "review/review_result.html", {"review": review})