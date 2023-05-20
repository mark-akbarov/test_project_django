from django.urls import path
from .views.login import LoginAPIView
from .views.signup import SignupView, CheckUsernameView
from .views.verification import VerifyUserAPIView, ReSendVerifyUserAPIView
from .views.forgot_password import SendForgotPasswordAPIView, CheckForgotPasswordCodeView, ForgotPasswordView


urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('check_username/', CheckUsernameView.as_view()),
    path('verify_user/', VerifyUserAPIView.as_view()),
    path('resend_verify_code/', ReSendVerifyUserAPIView.as_view()),
    path('send_forgot_password/', SendForgotPasswordAPIView.as_view()),
    path('check_forgot_password/', CheckForgotPasswordCodeView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),    
]
