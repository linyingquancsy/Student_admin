from django.conf.urls import url
from index.views import TeacherLC, TeacherRUD, StudentLC, StudentRUD

urlpatterns = [
    url(r'^tl/$', TeacherLC.as_view(), name='teacher-list'),
    url(r'^tl/(?P<pk>[0-9]+)/$', TeacherRUD.as_view(), name='teacher-detail'),
    url(r'^sl/$', StudentLC.as_view(), name='student-list'),
    url(r'^sl/(?P<pk>[0-9]+)/$', StudentRUD.as_view(), name='student-detail'),
]
