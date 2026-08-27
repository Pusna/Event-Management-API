from rest_framework import serializers
from .models import Event, EventRegistration
from django.contrib.auth.models import User


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'organizer']

        read_only_fields = ['organizer']


class EventRegistrationSerializer(serializers.ModelSerializer):
    event_title = serializers.ReadOnlyField(source='event.title')
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = EventRegistration
        fields = ['id', 'user', 'user_name', 'event', 'event_title', 'registered_at']
        read_only_fields = ['user', 'registered_at']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user