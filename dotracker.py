#1/usr/bin/python3


import json
import os
from filecmp  import cmp, dircmp
from shutil import copy, copytree


USER = os.getlogin()
dotfiles = f'/home/{USER}/dotfiles'



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


with open('config.json', 'r')as f:
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
        if cmp(folder, f'{path}/{name}'):
            print('Dotfiles are up to date')
            exit()
        try:
            os.mkdir(path)
            copy(folder, dest, follow_symlinks=True)
        except:
            pass
    elif dircmp(folder, f'{path}/{name}'):
        print('Dotfiles are up to date')
        exit()
    try:
        os.mkdir(path)
        copytree(folder, dest)
    except:
        pass
