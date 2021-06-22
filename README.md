## dotracker

dotracker is simple script for tracking do files

#### Installation

`./install.sh`


#### How it works

dotracker creates a'dotfiles' directory with every config file/folder specified in the config.json

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
