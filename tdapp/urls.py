from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'tdapp'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),

    path('teacher_details/<int:id>/',views.Teacher_details.as_view(),name='teacher_details'),
    path('filter_directory/',views.Filter_directory.as_view(),name='filter_directory'),
]
