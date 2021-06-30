from django.urls import path, include

# import main.views
import user.views

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('register/', user.views.RegisterView.as_view(), name='register'),
    path('<int:pk>/profile/update/', user.views.ProfileUpdateView.as_view(), name='profile_update'),
    path('<int:pk>/profile/detail/', user.views.ProfileDetailView.as_view(), name='profile_detail'),
]