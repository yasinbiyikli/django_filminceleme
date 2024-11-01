from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),  # Ana sayfa, film listesi
    path('movie/<int:id>/', views.movie_detail, name='movie_detail'),  # Film detay sayfası
    path('movie/<int:id>/add_review/', views.add_review, name='add_review'),  # İnceleme ekleme
    path('movie/<int:id>/add_comment/', views.add_comment_to_movie, name='add_comment_to_movie'),  # Filme yorum ekleme
    path('review/<int:id>/add_comment/', views.add_comment_to_review, name='add_comment_to_review'),
    # İncelemeye yorum ekleme

    # Kullanıcı kayıt, giriş ve çıkış
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='movies/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='movie_list'), name='logout'),

    # Profil sayfası
    path('profile/<str:username>/', views.profile, name='profile'),
]
