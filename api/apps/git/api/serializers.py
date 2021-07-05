from rest_framework import serializers

from ..models import PullRequest


class BranchSerializer(serializers.Serializer):
    """
    Serializer for branch representation.
    """
    source = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)


class CommitSerializer(serializers.Serializer):
    """
    Serializer for commit representation.
    """
    hash = serializers.CharField(max_length=100)
    message = serializers.CharField(max_length=150)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()
    files = serializers.CharField(max_length=100)


class BranchDetailSerializer(serializers.Serializer):
    """
    Serializer for branch detail representation.
    """
    name = serializers.CharField(max_length=100)
    commits = CommitSerializer(many=True)


class PullRequestSerializer(serializers.ModelSerializer):
    """
    Serializer for pull request representation.
    """
    class Meta:
        model = PullRequest
        fields = [
            "pk",
            "title",
            "author",
            "branch_base",
            "branch_compare",
            "description",
            "status"
        ]
