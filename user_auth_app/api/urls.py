from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token

from .views import UserProfileList, UserProfileDetail, RegistrationView, CustomLoginView

urlpatterns = [
    path('profiles/', UserProfileList.as_view(), name='userprofile-list'),
    path('profiles/<int:pk>/', UserProfileDetail.as_view(), name='userprofile-detail'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', CustomLoginView.as_view(), name='login')
    # path('login/', obtain_auth_token, name='login') # not necessary if using CustomLoginView
]
