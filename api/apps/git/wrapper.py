import logging
from pydriller import Repository

logger = logging.getLogger(__name__)


class GitWrapper(Repository):

    def get_branches(self):
        for path_repo in self._conf.get('path_to_repos'):
            with self._prep_repo(path_repo=path_repo) as git:
                logger.info('Analyzing git repository in %s', git.path)
                remote_refs = git.repo.remote().fetch()
                return [
                    {
                        "source": refs.name.split("/")[0],
                        "name": "/".join(refs.name.split("/")[1:]),
                    }
                    for refs in remote_refs
                ]

    def get_commits(self):
        commits = self.traverse_commits()
        return [
            {
                "hash": commit.hash,
                "message": commit.msg,
                "author": commit.author.name,
                "email": commit.author.email,
                "date": commit.author_date,
                "files": f"{commit.files} modified files",
            }
            for commit in commits
        ]
