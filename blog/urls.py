from django.contrib.auth.views import LogoutView,LoginView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path,include
from blog import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('login/', LoginView.as_view(template_name='posts/login.html'), name='login'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('category/<str:category_name>/', views.category_posts, name='category_posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('accounts/profile/password-change/', PasswordChangeView.as_view(template_name='posts/password_change.html'), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(template_name='posts/password_change_done.html'),
         name='password_change_done'),
    path('search/',views.search,name='search'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)