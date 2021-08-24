#!/usr/bin/env python3

import os, sys
from github import Github
from git import Repo

CLONE_FORKS = False
GITHUB_PERSONAL_ACCESS_TOKEN = "" # https://github.com/settings/tokens

g = Github(GITHUB_PERSONAL_ACCESS_TOKEN if GITHUB_PERSONAL_ACCESS_TOKEN else None)

try:
    username = sys.argv[1]
except:
    print("Usage:\n\t%s <github_username>" % sys.argv[0])
    sys.exit(1)

u = g.get_user(username)

for repo in u.get_repos():
    try:
        if repo.parent:
            if CLONE_FORKS:
                print("Cloning %s, which was forked from %s..." % (repo.name, repo.parent.full_name))
                Repo.clone_from(repo.clone_url, username + "/forks/" + repo.name)
            else:
                print("Skipping %s because it is was forked from %s..." % (repo.name, repo.parent.full_name))
        else:
            print("Cloning %s..." % repo.name)
            Repo.clone_from(repo.clone_url, username + "/repos/" + repo.name)
    except:
        continue
        
for gist in u.get_gists():
    try:
        print("Cloning gist ID %s (%s)..." % (gist.id, gist.description))
        dirname = gist.description if gist.description else gist.id
        Repo.clone_from(gist.git_pull_url, username + "/gists/" + dirname)
    except:
        continue

