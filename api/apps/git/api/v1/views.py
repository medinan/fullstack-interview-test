from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet

from ..mixins import GitMixin
from ..serializers import BranchSerializer, BranchDetailSerializer, CommitSerializer, PullRequestSerializer
from ...models import PullRequest
from ...wrapper import GitWrapper


class BranchViewSet(ViewSet, GitMixin):
    git_wrapper_class = GitWrapper
    serializer_class = BranchSerializer
    serializer_detail_class = BranchDetailSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.serializer_detail_class
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        return serializer_class(*args, **kwargs)

    def list(self, request, *args, **kwargs):
        git_manager = self.get_git_wrapper(self.get_repository_url())
        branches = git_manager.get_branches()
        serializer = self.get_serializer(branches, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        branch = pk.replace("_", "/")
        git_manager = self.get_git_wrapper(self.get_repository_url(), only_in_branch=branch)
        commits = git_manager.get_commits()
        data = {"name": branch, "commits": commits}
        serializer = self.get_serializer(data)
        return Response(serializer.data)


class CommitViewSet(ViewSet, GitMixin):
    git_wrapper_class = GitWrapper
    serializer_detail_class = CommitSerializer

    def get_serializer_class(self):
        return self.serializer_detail_class

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        return serializer_class(*args, **kwargs)

    def retrieve(self, request, branch_pk=None, pk=None):
        branch = branch_pk.replace("_", "/")
        git_manager = self.get_git_wrapper(
            self.get_repository_url(), only_in_branch=branch, only_commits=[pk, ]
        )
        commits = git_manager.get_commits()
        serializer = self.get_serializer(commits[0])
        return Response(serializer.data)


class PullRequestViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = PullRequest.objects.all()
    serializer_class = PullRequestSerializer

    @action(detail=True, methods=["put"])
    def close(self, request, pk=None):
        obj_instance = self.get_object()
        obj_instance.status = PullRequest.StatusPullRequest.CLOSED
        obj_instance.save()
        serializer = self.get_serializer(instance=obj_instance)
        return Response(serializer.data)
