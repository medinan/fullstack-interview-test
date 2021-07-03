from django.conf import settings


class GitMixin:
    git_wrapper_class = None

    def get_git_wrapper_class(self):
        return self.git_wrapper_class

    def get_git_wrapper(self, *args, **kwargs):
        git_wrapper_class = self.git_wrapper_class
        return git_wrapper_class(*args, **kwargs)

    def get_repository_url(self):
        return settings.REPOSITORY_URL
