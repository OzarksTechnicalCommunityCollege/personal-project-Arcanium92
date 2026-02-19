from django.shortcuts import render, redirect
from .models import GameReview
from .forms import GameReviewForm, UserRegistrationForm
from django.core.paginator import Paginator

# Adding decorators for user login
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "review/home.html")


def review_list(request):
    reviews = GameReview.objects.all().order_by('-submission')

    paginator = Paginator(reviews, 3)  # 3 reviews per page
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

            # Create new user object
            new_user = user_form.save(commit=False)

            # Set Password
            new_user.set_password(
                user_form.cleaned_data['password']
            )

            # Save user
            new_user.save()

            # Automatically log the user in after registration
            user = authenticate(
                username=new_user.username,
                password=user_form.cleaned_data['password']
            )
            login(request, user)

            # Redirect to review after account creation
            return redirect('home.html')

    else:
        user_form = UserRegistrationForm()

    # Render registration page
    return render(request, 'account/register.html', {'user_form': user_form})


def review_result(request, pk):
    review = GameReview.objects.get(pk=pk)
    return render(request, "review/review_result.html", {"review": review})