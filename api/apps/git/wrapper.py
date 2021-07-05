from pydriller import Repository
from django.utils.text import slugify


class GitWrapper(Repository):

    def get_branches(self):
        for path_repo in self._conf.get('path_to_repos'):
            with self._prep_repo(path_repo=path_repo) as git:
                remote_refs = git.repo.remote().fetch()
                result = []
                for refs in remote_refs:
                    split_name = refs.name.split("/")
                    source = split_name.pop(0)
                    name = "/".join(split_name).replace("/", "_")
                    result.append(
                        {
                            "source": source,
                            "name": name,
                        }
                    )
                return result

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
