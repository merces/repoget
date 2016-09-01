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

## What's that?

repoget creates a directory with the same name as the username given
and downloads (clones) all user's Github repositories to it. It also
creates a subdirectory for the gists at username/gists.

This program is tested on OS X and Linux only.

## Installation

    # pip install pygithub gitpython
    $ git clone https://github.com/merces/repoget.git
    $ cd repoget/

## Usage

    $ python repoget.py <github_username>

## Example

    $ python repoget.py merces
    Creating ./merces directory...
    Cloning repositories...
     merces/0d1n
     merces/bashacks
     merces/check-password
     merces/examine
     merces/filegrab
     merces/Git-Cheat-Sheet-Chrome-Extension
     merces/hdump
     merces/libpe
     merces/mentebinaria
     merces/openvaccine
     merces/pev
     merces/repoget
     merces/rt3070-linux3
     merces/rules
     merces/scripts
     merces/usbforce
     merces/vise
     merces/yara
    Cloning gists repositories...
     merces/gists/ca5aef8fbd09f2d66224 (Looping and modifying without changing its pointer)
     merces/gists/eb73556139a770443756 (A stenography challenge solution)
     merces/gists/1336cd4739cb1368efed (TLS callback implementation in C)
     merces/gists/36ce6e9602c163cf129e (A minimalist shell skeleton)
     merces/gists/4124617 (devprot - (un)set write protection flag in block devices)
