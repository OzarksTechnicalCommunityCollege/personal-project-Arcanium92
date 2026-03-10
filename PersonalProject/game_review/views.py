from django.shortcuts import render, redirect
from django.db.models import Prefetch
from .models import GameReview, ReviewLike
from .forms import GameReviewForm, UserRegistrationForm
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.core.cache import cache

# Adding decorators for user login
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "review/home.html")

def logged_out(request):
    return render(request, "registration/logged_out.html")

# Combined version to prefetch likes and keeps ordering and pagination
def review_list(request):
    like_qs = ReviewLike.objects.select_related('user')

    reviews = GameReview.objects.all().prefetch_related(
        Prefetch('likes', queryset=like_qs)
    ).order_by('-submission')

    paginator = Paginator(reviews, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "review/review_list.html", {"page_obj": page_obj})

# Make login required for add_review page
@login_required
def add_review(request):
    if request.method == "POST":
        form = GameReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect("review_result", pk=review.pk)
    else:
        form = GameReviewForm()
    return render(request, "add_review/add_review.html", {"form": form})


# Account registration function
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():

            # Creates new user object
            new_user = user_form.save(commit=False)

            # Set password
            new_user.set_password(user_form.cleaned_data['password'])

            # Save user
            new_user.save()

            user = authenticate(
                username=new_user.username,
                password=user_form.cleaned_data['password']
            )
            login(request, user)

            return redirect('home')

    else:
        user_form = UserRegistrationForm()

    return render(
        request,
        'registration/register.html',
        {'user_form': user_form}
    )

def review_result(request, pk):
    review = GameReview.objects.get(pk=pk)
    return render(request, "review/review_result.html", {"review": review})

# function to cache likes
def review_detail(request, review_id):
    key = f"review:{review_id}:like_count"
    like_count = cache.get(key)

    if like_count is None:
        review = GameReview.objects.get(id=review_id)
        like_count = review.like_count
        cache.set(key, like_count, 30)

    return render(request, "review/detail.html", {
        "review": review,
        "like_count": like_count
    })

# Toggle like/unlike view
@login_required
def toggle_like(request, review_id):
    review = get_object_or_404(GameReview, id= review_id)
    user = request.user
    existing_like = ReviewLike.objects.filter(user=user, review=review).first()
    
    if existing_like:
        existing_like.delete()
    else:
        ReviewLike.objects.create(user=user, review=review)
    return redirect('review_list')