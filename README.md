```
                                                         888    
                                                         888    
                                                         888    
    888d888  .d88b.  88888b.   .d88b.   .d88b.   .d88b.  888888 
    888P"   d8P  Y8b 888 "88b d88""88b d88P"88b d8P  Y8b 888    
    888     88888888 888  888 888  888 888  888 88888888 888    
    888     Y8b.     888 d88P Y88..88P Y88b 888 Y8b.     Y88b.  
    888      "Y8888  88888P"   "Y88P"   "Y88888  "Y8888   "Y888 
                     888                    888                 
                     888               Y8b d88P                 
                     888                "Y88P"                  

```

## What?

**repoget** clones all repositories and gists from a given
GitHub username.

## Why

During OSINT investigations, you may want to inspect all logged events
in a repository using commands like `git log`. This is only possible if
you clone the repository instead of just downloading an archive.

This script is also useful for downloading everything from a
GitHub user as a form of backup, in case the person deletes the account
or the account is taken down for some reason.

## Installation

```sh
git clone https://github.com/merces/repoget.git
cd repoget/
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Usage

Before using it, consider adding a GitHub
[personal access token](https://github.com/settings/tokens) to `repoget.py`,
otherwise you will be limited by the number of unauthenticated requests GitHub allows.

```sh
python repoget.py <github_username>
```

## Example

Clone all repos and gists from `github.com/merces`:

```sh
python repoget.py merces
Cloning aleph...
Cloning bashacks...
Cloning bonzim...
Cloning check-password...
Skipping Detect-It-Easy because it was forked from horsicq/Detect-It-Easy...
Skipping docs because it was forked from HyperDbg/docs...
Cloning umbreon_check...
Cloning gist ID d9188c2670caf28e70d3d3f6f6e1ceb5 (read a file using libbfd)...
Cloning gist ID 6efa466a60c67451f028f5d4f24f9404 ()...
Cloning gist ID 283a905fd9132b17ad9dc4664e6f8bc1 (5 star rank in PHP)...
Cloning gist ID ca5aef8fbd09f2d66224 (Looping and modifying without changing its pointer)...
```

You'll find the repositories in `merces/repos` and the gists in `merces/gists`.
