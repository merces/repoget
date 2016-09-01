#!/usr/bin/env python

# pip install pygithub gitpython

import os, sys
from pygithub3 import Github
from git import Repo

# Set user to None for gist repositories
def clone_repository(user, repo, path):
   try:
      if user:
         Repo.clone_from('https://github.com/%s/%s.git' % (user, repo), path)
      else:
         # repo is the gist hash then
         Repo.clone_from('https://gist.github.com/%s.git' % repo, path)
   except:
      print 'Error cloning \'%s\'' % repo

try:
   ghuser = sys.argv[1]
except:
   print "                                                     888    "
   print "                                                     888    "
   print "                                                     888    "
   print "888d888  .d88b.  88888b.   .d88b.   .d88b.   .d88b.  888888 "
   print "888P\"   d8P  Y8b 888 \"88b d88\"\"88b d88P\"88b d8P  Y8b 888    "
   print "888     88888888 888  888 888  888 888  888 88888888 888    "
   print "888     Y8b.     888 d88P Y88..88P Y88b 888 Y8b.     Y88b.  "
   print "888      \"Y8888  88888P\"   \"Y88P\"   \"Y88888  \"Y8888   \"Y888 "
   print "                 888                    888                 "
   print "                 888               Y8b d88P                 "
   print "                 888                \"Y88P\"             v0.1\n"
   print 'This program downloads all git repositories and gists from a given Github username.\n\n\
Usage:\n\t%s <github_username>\n' % sys.argv[0]
   sys.exit(1)

try:
   print 'Creating ./%s directory...' % ghuser
   os.mkdir(ghuser)
except:
   print 'Error: no write permission or directory already exists. You should fix that.'
   sys.exit(1)

gh = Github()
repos = gh.repos.list(user=ghuser, type='owner')
print 'Cloning repositories...'
for i in repos.iterator():
   print ' %s/%s' % (ghuser, i.name)
   clone_repository(ghuser, i.name, '%s/%s' % (ghuser, i.name))

gists = gh.gists.list(user=ghuser)
print 'Cloning gists repositories...'
for i in gists.iterator():
   print ' %s/gists/%s (%s)' % (ghuser, i.id, i.description)
   clone_repository(None, i.id, '%s/gists/%s' % (ghuser, i.id))
