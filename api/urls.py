from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.user import UserListView, UserDetailView

# router = routers.DefaultRouter()
# router.register(r'^users/$', UserListViewSet.as_view(), base_name='user-list')

urlpatterns = [
    url(r'^users/$', UserListView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)