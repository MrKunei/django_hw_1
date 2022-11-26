from django.db.models import Count, Q
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, \
    RetrieveAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from user.models import Location, User
from user.serializers import (
    LocationSerializer,
    UserListSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    UserAdSerializer
)


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer



class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserAdDetailView(ListAPIView):
    queryset = User.objects.annotate(total_ads=Count('ad', filter=Q(ad__is_published=True)))
    serializer_class = UserAdSerializer


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
