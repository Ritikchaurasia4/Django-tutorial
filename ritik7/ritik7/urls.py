"""
URL configuration for ritik7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include

# This is the another way of or (syntax) to link or (include) the views function in the urls.py file inside the inner project folder

# first synatx has show in project folder ritik6

from course import views as cv
from fees import views as fs
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('cor/',include([
#         path('learndjango/',cv.learn_django),
#         path('learnpy/',cv.learn_python),
#     ])),
#     path('fee/',include([
#         path('feedjango/',fs.fees_django),
#         path('feepy/',fs.fees_python),
#     ])),
# ]

#         OR , 

# This is also another syntax

coursepatterns = [
    path('learndj/',cv.learn_django),
    path('learnpy/',cv.learn_python),
]

feespattern = [
     path('feedjango/',fs.fees_django),
        path('feepy/',fs.fees_python),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cor/',include(coursepatterns)),
    path('fee/',include(feespattern)),
]