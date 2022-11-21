from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework import routers

from user import views

from user.views import LocationViewSet

router = routers.SimpleRouter()
router.register('location', LocationViewSet)

urlpatterns = [
    path('user/', views.UserListView.as_view()),
    # path('user/Z/', views.UserAdDetailView.as_view()),
    path('user/create/', views.UserCreateView.as_view()),
    path('user/<int:pk>', views.UserDetailView.as_view()),
    path('user/<int:pk>/update/', views.UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', views.UserDeleteView.as_view()),
]

urlpatterns += router.urls