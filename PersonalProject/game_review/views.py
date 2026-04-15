from django.shortcuts import render, redirect
from django.db.models import Prefetch
from .models import GameReview, ReviewLike
from .forms import GameReviewForm, UserRegistrationForm
from .serializers import GameReviewSerializer
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from rest_framework import viewsets

# Adding decorators for user login
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def home(request):
    viewed_ids = request.session.get('viewed_reviews', [])
    recently_viewed = GameReview.objects.filter(id__in=viewed_ids)
    return render(request, "review/home.html", {
        "recently_viewed": recently_viewed
    })

@login_required
def logged_out(request):
    logged_out(request)
    return render(request, "registration/logged_out.html")

# Breaking down functions to easier to follow functions
def get_reviews_with_likes():
    like_qs = ReviewLike.objects.select_related('user')
    return GameReview.objects.all().prefetch_related(
        Prefetch('likes', queryset=like_qs)
    ).order_by('-submission')

# Pagination view
def paginate_queryset(request, queryset, per_page=5):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)

# Reworked current_user view 
def attach_current_user(page_obj, user):
    for review in page_obj:
        review.current_user = user
    return page_obj

# Reworked review_list view
def review_list(request):
    reviews = get_reviews_with_likes()
    page_obj = paginate_queryset(request, reviews)
    page_obj = attach_current_user(page_obj, request.user)
    return render(request, "review/review_list.html", {"page_obj": page_obj})

# ----- Changing the view to meet the first goal by breaking down complex functions into a managable function
# Combined version to prefetch likes and keeps ordering and pagination
# def review_list(request):
#     like_qs = ReviewLike.objects.select_related('user')

#     reviews = GameReview.objects.all().prefetch_related(
#         Prefetch('likes', queryset=like_qs)
#     ).order_by('-submission')

#     paginator = Paginator(reviews, 5)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     # Attach current user to each review
#     for review in page_obj:
#         review.current_user = request.user

#     return render(request, "review/review_list.html", {"page_obj": page_obj})

# Make login required for add_review page
@login_required
def add_review(request):
    last_rating = request.COOKIES.get('last_rating')

    if request.method == "POST":
        form = GameReviewForm(request.POST)
        if form.is_valid():
            review = form.save()

            response = redirect("review_result", pk=review.pk)

            # Save rating submission in a cookie for 5 days
            response.set_cookie(
                'last_rating',
                review.rating,
                max_age=60*60*24*5
            )

            return response
    else:
        form = GameReviewForm(initial={'rating': last_rating})

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
    review = get_object_or_404(GameReview, id=review_id)
    #Track recently viewed reviews
    viewed = request.session.get('viewed_reviews', [])

    if review_id not in viewed:
        viewed.append(review_id)

    request.session['viewed_reviews'] = viewed

    # --- Cache Logic ---
    key = f"review:{review_id}:like_count"
    like_count = cache.get(key)

    if like_count is None:
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

# View for APIs
class GameReviewSets(viewsets.ModelViewSet):
    queryset = GameReview.objects.all()
    serializer_class = GameReviewSerializer