from django.conf.urls import url
from rest_framework  import routers
# from rest_framework.urlpatterns import format_suffix_patterns
from api.views.user import UserListViewSet

router = routers.DefaultRouter()
router.register(r'users', UserListViewSet)