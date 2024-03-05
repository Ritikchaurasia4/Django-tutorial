from django.urls import path
# . means current directory
from . import views
urlpatterns = [
    path('learndj/',views.learn_django),
    path('learnpy/',views.learn_python),
]
