from django.urls import path, include
from rest_framework import routers
from movierater.api import views
from movierater.api.views import CustomObtainAuthToken

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('movies', views.MovieViewSet)
router.register('rating', views.RatingViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('authenticate/', CustomObtainAuthToken.as_view()),
]
