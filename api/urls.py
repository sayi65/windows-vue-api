from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api.views.user import UserListView, UserDetailView
from api.views.worktime import WorkTimeListView, WorkTimeDetailView
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'^users/$', UserListView.as_view(), base_name='user-list')
# router.register(r'^worktime/$', WorkTimeListView.as_view(), base_name='worktime-list')
# urlpatterns = [
# ]
# urlpatterns += router.urls
urlpatterns = [
    url(r'^users/$', UserListView.as_view(),name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailView.as_view(),name='user-detail'),
    url(r'^worktime/$', WorkTimeListView.as_view(),name='worktime-list'),
    url(r'^worktime/(?P<pk>[0-9]+)/$', WorkTimeDetailView.as_view(),name='worktime-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)