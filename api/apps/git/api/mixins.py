from typing import Type

from django.conf import settings

from ..wrapper import GitWrapper


class GitMixin:
    """
    Mixin to manager git wrapper in viewset class
    """
    git_wrapper_class = None

    def get_git_wrapper_class(self) -> Type[GitWrapper]:
        """
        Get git wrapper class
        """
        return self.git_wrapper_class

    def get_git_wrapper(self, *args, **kwargs) -> Type[GitWrapper]:
        """
        Get git wrapper class instance.
        """
        git_wrapper_class = self.git_wrapper_class
        return git_wrapper_class(*args, **kwargs)

    def get_repository_url(self):
        """
        Get url repository from django settings
        """
        return settings.REPOSITORY_URL
