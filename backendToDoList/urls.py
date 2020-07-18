"""backendToDoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from accounts.views import ForgetPassword
from todoList.views import ToDoList,update,updateStatus,ChangePassword
from accounts.views import user_create
from accounts import views
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_task/<str:email>',ToDoList.as_view(),name='add_task'),
    path('all_tasks/<str:email>',ToDoList.as_view()),
    path('delete-task/<str:pk>',ToDoList.as_view()),
    path('update-task/<int:pk>',update.as_view())
    ,path('user-add/',user_create.as_view()),
    path('tokens/',jwt_views.TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('update-status/<int:pk>',updateStatus.as_view()),
    path('jwt/refresh/',jwt_views.TokenRefreshView.as_view(),name='token_refresh'),
    path('forget-password',ForgetPassword.as_view()),
    path('change-password/<str:email>',ChangePassword.as_view())
]
