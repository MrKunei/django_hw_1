from rest_framework import serializers
from .models import *



class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class UserListSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        slug_field='name',
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = "__all__"


class UserAdSerializer(serializers.ModelSerializer):
    total_ads = serializers.IntegerField()
    location = serializers.SlugRelatedField(
        slug_field='name',
        many=True,
        read_only=True
    )

    class Meta:
        model =User
        fields = "__all__"

class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        slug_field='name',
        many=True,
        required=False,
        queryset=Location.objects.all()
    )

    def is_valid(self, *, raise_exception=False):
        self._location = self.initial_data.pop('location')
        super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for loc in self._location:
            object, _ = Location.objects.get_or_create(name=loc)
            user.location.add(object)

        user.save()
        return user

    class Meta:
        model = User
        fields = "__all__"


class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        slug_field='name',
        many=True,
        required=False,
        queryset=User.objects.all()
    )

    def is_valid(self, *, raise_exception=False):
        self._location = self.initial_data.pop('location')
        super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        user = super().save()

        for loc in self._location:
            odject, _ = Location.objects.get_or_create(name=loc)
            user.location.add(odject)
        user.save()
        return user