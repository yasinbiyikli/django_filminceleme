from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.utils import timezone
from .models import Movie, Review, Comment

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    reviews = movie.reviews.all()
    return render(request, 'movies/movie_detail.html', {'movie': movie, 'reviews': reviews})

@login_required
def add_review(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'POST':
        review_text = request.POST.get('review_text')
        rating = request.POST.get('rating')
        if review_text and rating:
            Review.objects.create(
                movie=movie,
                user=request.user,
                review_text=review_text,
                rating=int(rating),
                created_at=timezone.now()
            )
            return redirect('movie_detail', id=movie.id)
    return render(request, 'movies/add_review.html', {'movie': movie})

@login_required
def add_comment_to_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Comment.objects.create(user=request.user, movie=movie, content=content)
            return redirect('movie_detail', id=movie.id)
    return render(request, 'movies/add_comment.html', {'movie': movie})

@login_required
def add_comment_to_review(request, id):
    review = get_object_or_404(Review, id=id)
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Comment.objects.create(user=request.user, review=review, content=content)
            return redirect('movie_detail', id=review.movie.id)
    return render(request, 'movies/add_comment.html', {'review': review})

def profile(request, username):
    user = get_object_or_404(User, username=username)
    reviews = Review.objects.filter(user=user)
    return render(request, 'movies/profile.html', {'user': user, 'reviews': reviews})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                login(request, user)  # Kayıt olduktan sonra otomatik giriş yap
                messages.success(request, "Kayıt başarılı!")
                return redirect('movie_list')
            except:
                messages.error(request, "Bu kullanıcı adı zaten alınmış.")
        else:
            messages.error(request, "Şifreler eşleşmiyor.")
    return render(request, 'movies/register.html')