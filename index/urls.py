from django.urls import path
from . import views


urlpatterns = [
    path('cat/<str:page>', views.get_page, name='page'),
    path('courses/<str:course>', views.courses, name='courses'),
    # path('teachers', views.teachers, name='teachers'),
    path('', views.home, name='home')
]
