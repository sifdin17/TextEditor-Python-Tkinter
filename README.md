

# TextEditor in Python OO with Tkinter 

This project to be shared with my dev students.

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
- Changing window size and position (with synced preview - inspired from **CMD**)
- menu icons attached to the text editor for quick access.
- Search dialog for searching inside the texteditor
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
#### read_config.py
Includes All Image/icons Dictionaries and Configparser module to configuration.ini data.

#### main_window.py
Main window class includes the GUI and all methods attached to the Menubar and text styling menu.

> **Note:** all styling changes within this window will be stored in the ```Configuration.in``` file..

![](https://res.cloudinary.com/cloudjs/image/upload/v1672610764/github/textnote.jpg)

#### settings_window.py
TopLevel settings window includes the GUI and methods for ListBox, Spinbox, Entry and button actions. Also includes a Frame Preview of the window size and X,Y positions...

![](https://res.cloudinary.com/cloudjs/image/upload/v1672610731/github/settings_tabs.jpg)

the window preview is inspired from the window setting from windows ***CMD***. the ```configuration.ini``` will save the X,Y position and load the window at the speciefied position each time...
![](https://res.cloudinary.com/cloudjs/image/upload/v1672610666/github/cmd_preview.jpg)

we have used the ```winfo_screenwidth()``` and ```winfo_screenheight()``` to auto get the width and height of the users own screen, which allows the user to preview the position of the window correctly.

this is a part of the code:
```python
  self.preview_frame_w = float(340)
  self.preview_frame_h = float(150)

  self.original_screen_width  = float(self.master.winfo_screenwidth()) 
  self.original_screen_height = float(self.master.winfo_screenheight())

  self.width_persentage  = float(self.original_screen_width/self.preview_frame_w) 
  self.height_persentage = float(self.original_screen_height/self.preview_frame_h)

  self.notebad_calc_width  = (float(config_window_width)/self.width_persentage)
  self.notebad_calc_height = (float(config_window_height)/self.height_persentage)

  self.notebad_calc_left_pos = (float(config_window_left)/self.width_persentage) 
  self.notebad_calc_top_pos = (float(config_window_top)/self.height_persentage)
  
  position_preview_frame = LabelFrame( tab_for_window_size , text="  Preview Position  " ,bg="#ffffff",borderwidth=1.5, padx=5, pady=0)
  position_preview_frame.place(x=0, y=100, width=355, height=175)
  position_preview_inside_frame = Frame( position_preview_frame, width=self.preview_frame_w, height=self.preview_frame_h, bg="#000000")
  position_preview_inside_frame.place(x=0, y=0)
```
> **Note:** code is not perfect, you probably going to find an error somewhere =D

## Contributing
Pull requests are welcome for all kind of changes!
