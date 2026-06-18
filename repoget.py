#!/usr/bin/env python3

# SPDX-License-Identifier: GPL-3.0-or-later
#
# Copyright (c) 2016, 2021, 2025 Fernando Mercês
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.

import sys
from github import Github, Auth
from git import Repo

CLONE_FORKS = False
GITHUB_PERSONAL_ACCESS_TOKEN = "" # https://github.com/settings/tokens

g = Github(auth=Auth.Token(GITHUB_PERSONAL_ACCESS_TOKEN)) if GITHUB_PERSONAL_ACCESS_TOKEN else Github()

try:
    username = sys.argv[1]
except:
    print("Usage:\n\t%s <github_username>" % sys.argv[0])
    sys.exit(1)

try:
    u = g.get_user(username)
except:
    sys.exit(1)

for repo in u.get_repos():
    try:
        if repo.parent:
            if CLONE_FORKS:
                print("Cloning %s, which was forked from %s..." % (repo.name, repo.parent.full_name))
                Repo.clone_from(repo.clone_url, username + "/forks/" + repo.name)
            else:
                print("Skipping %s because it was forked from %s..." % (repo.name, repo.parent.full_name))
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
