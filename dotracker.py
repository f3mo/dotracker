#!/usr/bin/python3
import json
import os
from filecmp  import cmp, dircmp
from shutil import copy, copytree


USER = os.getlogin()
dotfiles = f'/home/{USER}/dotfiles'

config_path = f'/home/{USER}/config.json'

try:
    os.mkdir(dotfiles)
    copy('config.json', f'{dotfiles}/config.json')
except:
    pass

try:
    os.mkdir(dotfiles)
    copy('config.json', f'{dotfiles}/config.json')
except:
    pass


paths = {}


with open(config_path, 'r')as f:
    configs = json.loads(f.read())


path = configs['dir'][0]

if len(path) == 0:
    print(f'\nConfig is empty. \nLocation:{dotfiles}/config.json')
    exit()


for name, folder in  path.items():
    path = f'{dotfiles}/{name}'
    path_name = name
    name = folder.split('/')[-1]
    dest = f'{path}/{name}'

    if os.path.isfile(folder):
        try:
            os.mkdir(path)
        except:
            pass

        try:
            copy(folder, dest, follow_symlinks=True)
        except:
            pass

    try:
        os.mkdir(path)
    except:
        pass

    try:
        copytree(folder, dest)
    except:
        pass

print("Dotfiles Updated")
