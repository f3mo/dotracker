## dotracker

dotracker is simple script for tracking dot files

#### Installation

`./install.sh`


#### How it works

dotracker creates a'dotfile' directory for every config file/folder specified in the config file

```

../dotfiles/
├── config
├── config.json
├── i3
│   └── config
├── i3blocks
│   └── config
└── vim

4 directories, 3 files


```

##### Conifguration

`/home/<user>/config.json`


```
{
    "dir": [
    {
       "i3": "/home/me/.config/i3/config",
       "vim": "/home/me/.vimrc",
       "config": "/home/me/.config"
      }
    ]
}



```

##### Usage
`dotracker`
