from .views import send_code_verification, invite_code_verification, ProfileUser
from django.urls import path

with open('verification_phone_api/q.txt', 'r') as file:
    description_text = file.read()
app_name = 'verification_phone_api'


urlpatterns = [
    path('send_code_verification', send_code_verification, name='code_verification_api'),
    path('invite_code_verification', invite_code_verification, name='invite_code_verification_api'),
    path('profile/<phone_number>', ProfileUser.as_view(), name='profile')
]

