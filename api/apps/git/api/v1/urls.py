from django.urls import path, include
from rest_framework_nested import routers

from .views import BranchViewSet, CommitViewSet, PullRequestViewSet

router = routers.SimpleRouter()
router.register(r'branches', BranchViewSet, basename="branches")
router.register(r'pullrequests', PullRequestViewSet, basename="pullrequests")
commit_router = routers.NestedSimpleRouter(router, r'branches', lookup='branch')
commit_router.register(r'commits', CommitViewSet, basename='branches-commit')


urlpatterns = [
    path("", include(router.urls)),
    path("", include(commit_router.urls)),
]
