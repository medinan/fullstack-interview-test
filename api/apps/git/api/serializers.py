from rest_framework import serializers


class BranchSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    safe = serializers.CharField(max_length=100)


class CommitSerializer(serializers.Serializer):
    hash = serializers.CharField(max_length=100)
    message = serializers.CharField(max_length=150)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()
    files = serializers.IntegerField()


class BranchDetailSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    commits = CommitSerializer(many=True)

