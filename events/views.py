from rest_framework import viewsets, permissions
from .models import Event, EventRegistration
from .serializers import EventSerializer, EventRegistrationSerializer, UserRegistrationSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.core.mail import send_mail
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.views import ObtainAuthToken


class IsOrganizerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.organizer == request.user


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOrganizerOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['location', 'date']
    search_fields = ['title', 'description']

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        registration = serializer.save(user=self.request.user)
        event = registration.event
        user = self.request.user

        if user.email:
            send_mail(
                subject=f'Registration Confirmed: {event.title}',
                message=f'Hi {user.username}!\n\nYou have successfully registered for the event "{event.title}".\nDate: {event.date}\nLocation: {event.location}\n\nSee you there!',
                from_email=None,
                recipient_list=[user.email],
                fail_silently=True,
            )



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegistrationSerializer

class CustomObtainAuthToken(ObtainAuthToken):
    parser_classes = [JSONParser]