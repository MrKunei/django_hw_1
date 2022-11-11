from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from ads import views


urlpatterns = [
    path("", views.index),

    path('ad/', views.AdListView.as_view()),
    path('ad/create/', views.AdCreateView.as_view()),
    path('ad/<int:pk>', views.AdDetailView.as_view()),
    path('ad/<int:pk>/add_image/', views.AdImageView.as_view()),
    path('ad/<int:pk>/update/', views.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', views.AdDeleteView.as_view()),

    path('cat/', views.CategoryListView.as_view()),
    path('cat/create/', views.CategoryCreateView.as_view()),
    path('cat/<int:pk>', views.CategoryDetailView.as_view()),
    path('cat/<int:pk>/update/', views.CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', views.CategoryDeleteView.as_view()),

    path('user/', views.UserListView.as_view()),
    path('user/Z/', views.UserAdDetailView.as_view()),
    path('user/create/', views.UserCreateView.as_view()),
    path('user/<int:pk>', views.UserDetailView.as_view()),
    path('user/<int:pk>/update/', views.UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', views.UserDeleteView.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)