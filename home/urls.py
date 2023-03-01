from django.urls import path,include
from home.views import CollegeViewSet,StudentViewSet
from rest_framework import routers





routers=routers.DefaultRouter()
routers.register(r'College',CollegeViewSet,)
routers.register(r'Student',StudentViewSet,)





urlpatterns = [
    path('',include(routers.urls))
]
