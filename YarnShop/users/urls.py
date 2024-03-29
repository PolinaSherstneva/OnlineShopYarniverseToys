from django.urls import path, include

from YarnShop import settings
from users.views import SignUpView, LoginUser, change_username
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registration/', SignUpView.as_view(), name='registrations'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('changeinf/', change_username, name='changeinf')

]
