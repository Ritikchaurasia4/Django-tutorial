from django.urls import path
# Here . means current directory
from . import views
urlpatterns = [
    path('feesdj/', views.fees_django),
    path('feespy/',views.fees_python),
]
