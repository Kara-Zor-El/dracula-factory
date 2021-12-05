# 🗼Dracula Factory 🏭
Forked from [onedark-factory](https://github.com/AbdelrhmanNile/onedark-factory) 😄

A simple cli to convert any image to a dracula themed wallpaper

![example](./example.png)

## Installation
1. Clone the repo.
2. Install the required packages using pip as shown below:
```
pip3 install rich image-go-nord argparse
```
3. Edit the file ```conv.py``` line 14 with your user name, DO NOT CHANGE THE DIR, IT WILL NOT WORK AS EXPECTED, IF YOU WANT TO EDIT IT THEN DO IT IN BOTH ```conv.py``` and ```drf.sh```.
4. Install it with:
```
sudo make install
```

## Usage
from your terminal run:
```
drf
```
or
```
drf /path/to/image/
```

 All the outputs will be in ~/Pictures/dracula-factory

 ## UNINSTALL
 1. ```cd``` into the repo folder.
 2. Uninstall it with:
 ```
 sudo make uninstall
 ```


 ## Credits
- **Made** with [Schrodinger-Hat's ImageGoNord](https://github.com/Schrodinger-Hat), but with the Dracula palette
- **Text User Interface (TUI)** made with [rich](https://github.com/willmcgugan/rich)
