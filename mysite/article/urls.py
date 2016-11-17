from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import article_list,ArticleCreateView

urlpatterns=[
    url(r'^list/(?P<block_id>\d+)',article_list),
    url(r'^create/(?P<block_id>\d+)',login_required(ArticleCreateView.as_view())),
]
