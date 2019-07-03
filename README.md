

# TextEditor in Python OO with Tkinter 

Crmf School Project
 This project has been developed on windows 10 using Python 3

## Release Information
**Author:** Saifeddine Chagdali

**Release Date:** 06/30/2019

## Library required

Requires Python and Tkinter, os and PIL modules.

Use the package manager pip to install PIL.

```bash
pip install pillow
```

Once the modules are installed you can run the TextEditor using:
```bash
$ python main.py
```

## Features

- Using Oriented Object 
- Loading and saving changes in configuration.ini
- Changing font type and font size (synced)
- Changing Font styles and colors (synced)
- Changing window size and position (with synced preview - inspired from CMD)

## File Structure
#### configuration.ini
This file is used to manage and save editable configuration. The configuration file is organized into the following sections:

```bash
[font_settings] # For font style and size
[color_settings] # For font color and text background color
[window_size_settings] # window width and height settings
[window_position_settings] # top and left position of the window
[menu_settings] # show/hide menu icons, show/hide shortcuts
[ready_styles_settings] # ready theme colors and backgrounds
[text_styles] # weight, italic and underline
```
#### main_window.py
Main window class includes the GUI and all methods attached to the Menubar and text styling menu.

#### settings_window.py
TopLevel settings window includes the GUI and methods for ListBox, Spinbox, Entry and button actions. Also includes a Frame Preview of the window size and X,Y positions...

#### read_config.py
Includes All Image/icons Dictionary and Configparser module to configuration.ini data.



## ScreenShots
![](https://raw.githubusercontent.com/sifdin17/TextEditor/master/demo_screenshots/cmd.jpg)

![](https://raw.githubusercontent.com/sifdin17/TextEditor/master/demo_screenshots/editor_preview.jpg )






Contributing
Pull requests are welcome for all kind of changes...
