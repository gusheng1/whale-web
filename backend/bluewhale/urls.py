"""bluewhale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib.auth import get_user_model
from rest_framework import routers
from rest_auth.views import LogoutView
from core.views_auth import BluewhaleLoginView, get_user_info, send_verification_mail,\
   add_user_info,select_user_info,del_user_info, verify_verification_token,\
    register,add_articles,delete_articles,select_articles
from blog.views import ArticleListCreateView, ArticleDetailView
from rest_framework import routers


api_prefix = 'api/v1'

router = routers.DefaultRouter()

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(f'{api_prefix}/login', BluewhaleLoginView.as_view(), name='rest_login'),
    path(f'{api_prefix}/logout', LogoutView.as_view(), name='rest_logout'),
    path(f'{api_prefix}/send-verification', send_verification_mail, name='send verification mail'),
    path(f'{api_prefix}/verify/<token>', verify_verification_token, name='verify verification token'),
    path(f'{api_prefix}/register', register, name='register'),
    path(f'{api_prefix}/me', get_user_info, name='user profile'),

    path(f'{api_prefix}/me/add', add_user_info, name='add user'),
    path(f'{api_prefix}/me/delete', del_user_info, name='delete user'),
    path(f'{api_prefix}/me/select', select_user_info, name='select user'),

    path(f'{api_prefix}/articles', ArticleListCreateView.as_view(), name='articles'),
    path(f'{api_prefix}/articles/<pk>', ArticleDetailView.as_view(), name='article'),
    path(f'{api_prefix}/', include(router.urls)),

    path(f'{api_prefix}/articles/add', add_articles, name='add articles'),
    path(f'{api_prefix}/articles/del', delete_articles, name='delete articles'),
    path(f'{api_prefix}/articles/select', select_articles, name='select articles'),



]
