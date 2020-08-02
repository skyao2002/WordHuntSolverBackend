from django.urls import path, include
from . import api
from .views import solve_this
from rest_framework import routers

router = routers.DefaultRouter()
router.register('solver', api.SolverViewSet)

urlpatterns = [
    #path('', include('count.urls'))
    #path('', include(router.urls)),
    path('solve_this/', solve_this)
]