from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import EventViewSet, EventRegistrationViewSet, RegisterView

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'registrations', EventRegistrationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
]

