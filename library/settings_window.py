import configparser
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from tkinter.colorchooser import *
import os


from tkinter import filedialog
from tkinter import messagebox

from library.read_config import *

from PIL import Image, ImageTk


imgDict={}

#======================================
# Settings Window
#======================================

class Settings_class:


    def __init__(self,master,content,prefe_window):
        self.master = master
        self.content = content
        self.prefe_window = prefe_window

        self.all_variable_initiation()
        
        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(family="Calibri", size=10)



    #############################
    # initiate default values
    #############################
    def all_variable_initiation(self) :

        self.font_family=config_font_style
        self.font_size=config_font_size

        self.font_color = config_font_color
        self.text_background = config_text_background

        self.window_width = config_window_width
        self.window_height = config_window_height

        self.window_top_position = config_window_top
        self.window_left_position = config_window_left

        self.style1 = eval(config_style_1)
        self.style2 = eval(config_style_2)
        self.style3 = eval(config_style_3)

        self.config_font_style_1 = config_font_style_1
        self.config_bg_style_1 = config_bg_style_1
        self.config_font_style_2 = config_font_style_2
        self.config_bg_style_2 = config_bg_style_2
        self.config_font_style_2 = config_font_style_2
        self.config_bg_style_2 = config_bg_style_2



    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # creating setting window with all widgets 
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
    def create_settings_window(self, *args) :   

        # Top level window
        self.prefe_window = Toplevel(self.master)
        self.prefe_window.grab_set()
        self.prefe_window.title("Setting")
        self.prefe_window.geometry("400x382")
        self.prefe_window.resizable(False, False)


        #create Notebook tabs
        tab_control = ttk.Notebook( self.prefe_window ,padding=10)

        gui_style = ttk.Style()
        gui_style.configure('My.TFrame', background='#ffffff')
        ttk.Style().configure("TNotebook.Tab", padding=[15, 2])


        tab_for_fonts = ttk.Frame( tab_control, width=300, height=275, style='My.TFrame')
        tab_control.add( tab_for_fonts, text='Colors',padding=10)

        tab_for_layout = ttk.Frame( tab_control, width=300, height=200, style='My.TFrame')
        tab_control.add( tab_for_layout, text='Fonts',padding=10)

        tab_for_window_size = ttk.Frame( tab_control, width=300, height=200, style='My.TFrame')
        tab_control.add( tab_for_window_size, text='Layout',padding=10)




        ########## - Colors Tab Frame - ##########
        #
        #
        # Color Frame
        #
        #

        font_color_frame = LabelFrame( tab_for_fonts , text="  Choose Colors  " ,bg="#ffffff",borderwidth=1.5, padx=5, pady=0)
        font_color_frame.place(x=0, y=5, width=357, height=90)

        label_font_choose= Label(font_color_frame, text="Font Color:", bg="#ffffff")
        label_bg_choose = Label(font_color_frame, text="Background Color:", bg="#ffffff")
        label_font_choose.place(x=3, y=7)
        label_bg_choose.place(x=3, y=35)

        global entry_font_choose,entry_bg_choose,font_choose_btn,background_choose_btn


        get_font_c = Settings_class.get_config_default_font_color(self)
        get_text_c = Settings_class.get_config_default_bg_color(self)
        entry_font_choose = Entry(font_color_frame,fg=config_font_color, state="readonly", textvariable=StringVar(value=get_font_c), font=('Calibri',11), bd=2, relief=GROOVE)
        entry_bg_choose = Entry(font_color_frame,fg=config_text_background, state="readonly", textvariable=StringVar(value=get_text_c) , font=('Calibri',11), bd=2, relief=GROOVE)
        entry_font_choose.place(x=115, y=5)
        entry_bg_choose.place(x=115, y=35)


        font_choose_btn = Button( font_color_frame , text = "Choose Color", relief=GROOVE, height=1,width=12, font=('Calibri',10), pady=0 , command = self.choose_font_color)
        background_choose_btn = Button(font_color_frame, text = "Choose Color", relief=GROOVE, height=1,width=12, font=('Calibri',10), pady=0 , command = self.choose_bg_color)

        font_choose_btn.place(x=245, y=5)
        background_choose_btn.place(x=245, y=35)

        #checking of a theme is set to disable btns
        Settings_class.check_colors_btns_state(self)

        #
        #
        # Ready styles Frame
        #
        #

        ready_styles_frame = LabelFrame( tab_for_fonts , text="  Custom Style  " ,bg="#ffffff",borderwidth=1.5, padx=5, pady=0)
        ready_styles_frame.place(x=0, y=110, width=357, height=75)

        self.radio_style = IntVar()  

        radio_style_costum = Radiobutton(ready_styles_frame,bg="#ffffff",activebackground="#ffffff", text="Default Colors", variable=self.radio_style, value=0, command=self.set_ready_style) 
        radio_style1 = Radiobutton(ready_styles_frame,bg="#ffffff",activebackground="#ffffff", text="Sky Blue Color", variable=self.radio_style, value=1, command=self.set_ready_style)
        radio_style2 = Radiobutton(ready_styles_frame,bg="#ffffff",activebackground="#ffffff", text="Sunset Color", variable=self.radio_style, value=2, command=self.set_ready_style)  
        radio_style3 = Radiobutton(ready_styles_frame,bg="#ffffff",activebackground="#ffffff", text="Nature Color", variable=self.radio_style, value=3, command=self.set_ready_style)  
        
        radio_style_costum.deselect()
        radio_style1.deselect()
        radio_style2.deselect()
        radio_style3.deselect()

        if self.style1:
            radio_style1.select()
            print(self.style1)
        elif self.style2:
            radio_style2.select()
            print(self.style2)

        elif self.style3:
            radio_style3.select()
            print(self.style3)

        else:
            radio_style_costum.select()


        radio_style_costum.place(x=3, y=5)
        radio_style1.place(x=3, y=25)
        radio_style2.place(x=190, y=5)
        radio_style3.place(x=190, y=25)

        #
        #
        # Preview Colors Frame
        #
        #

        global preview_frame_bg, preview_frame_text


        preview_color_frame = LabelFrame( tab_for_fonts , text="  Preview Colors " ,bg="#ffffff",borderwidth=1.5, padx=5, pady=0)
        preview_color_frame.place(x=0, y=200, width=357, height=75)

        preview_frame_bg = Frame( preview_color_frame, width=342, height=50, bg=get_text_c)
        preview_frame_bg.place(x=0, y=0)


        preview_frame_text = Message(preview_frame_bg, text="This is a Preview text that displays colors, background, font and fontsize...", width=340, bg=get_text_c, fg=get_font_c, font=(config_font_style, config_font_size))
        preview_frame_text.place(x=5, y=5)







        ########## - Fonts Tab Frame - ##########
        #
        #
        # Font Family Frame
        #
        #

        global police_entry, police_sys_list, police_listbox
        police_sys_list = list(tkFont.families())
        police_sys_list.sort()


        font_family_frame = LabelFrame( tab_for_layout , text="  Font Family  " ,bg="#ffffff",borderwidth=1.5, padx=5, pady=0)
        font_family_frame.place(x=0, y=0, width=215, height=185)

        police_entry = Entry(font_family_frame, state="readonly", width=20,textvariable=StringVar(value=config_font_style), font=('Calibri',11), bd=2, relief=GROOVE)
        police_entry.place(x=0, y=5, width=200)

        #Listbox for Police

        police_frame = Frame(font_family_frame, background="#cccccc", padx=1, pady=1)
        police_frame.place(x=0, y=35, width=199,height=125) 

        scroll_for_police = Scrollbar(police_frame)
        scroll_for_police.pack(side=RIGHT, fill=Y)

        police_listbox = Listbox(police_frame, width= 28,height=5,font=('Calibri',10),bd=0,highlightthickness=0,bg="#ffffff",exportselection=False)
        police_listbox.pack(side =LEFT, fill=Y)

        #get fonts system
        for i in range(0, len(police_sys_list)):
            police_listbox.insert(i+1, police_sys_list[i])

        #link scrool with listbox -- fix scrool issue!!!
        scroll_for_police['command'] = police_listbox.yview
        police_listbox['yscrollcommand'] = scroll_for_police.set
        # append function on select
        police_listbox.bind('<<ListboxSelect>>',self.changePolice)


        #
        #
        # Font size frame
        #
        #

        global fontsize_listbox

        font_size_frame = LabelFrame( tab_for_layout , text="  Font Size  " ,bg="#ffffff",borderwidth=1.5, padx=5, pady=0)
        font_size_frame.place(x=220, y=0, width=135, height=185)

        #Listbox for size
        fontsize_in_frame = Frame(font_size_frame, background="#cccccc", padx=1, pady=1)
        fontsize_in_frame.place(x=0, y=5, width=120,height=155) 

        scroll_for_fontsize = Scrollbar(fontsize_in_frame)
        scroll_for_fontsize.pack(side=RIGHT, fill=Y)

        fontsize_listbox = Listbox(fontsize_in_frame, width= 15,height=5,font=('Calibri',10),bd=0,highlightthickness=0,bg="#ffffff",exportselection=False)
        fontsize_listbox.pack(side =LEFT, fill=Y)

        for i in range(10, 34):
            fontsize_listbox.insert(i+1, i)

        #link scrool - fix issue
        scroll_for_fontsize['command'] = fontsize_listbox.yview
        fontsize_listbox['yscrollcommand'] = scroll_for_fontsize.set
        # append event 
        fontsize_listbox.bind('<<ListboxSelect>>',self.changeSize)


        #
        #
        # Preview Font changes Frame
        #
        #


        global preview_font_frame_bg, preview_frame_text_font
        preview_font_frame = LabelFrame( tab_for_layout , text="  Preview Font  " ,bg="#ffffff",borderwidth=1.5, padx=5, pady=0)
        preview_font_frame.place(x=0, y=200, width=357, height=75)

        preview_font_frame_bg = Frame( preview_font_frame, width=342, height=50, bg=get_text_c)
        preview_font_frame_bg.place(x=0, y=0)

        preview_frame_text_font = Message(preview_font_frame_bg, text="This is a Preview text that displays colors, background, font and fontsize...", width=340, bg=get_text_c, fg=get_font_c, font=(config_font_style, config_font_size))
        preview_frame_text_font.place(x=5, y=5)




        ########## - Window Size and Position Tab Frame - ##########
        #
        #
        # Window Size Frame
        #
        #

        global window_width_spinbox, window_height_spinbox, window_left_spinbox, window_top_spinbox

        window_size_frame = LabelFrame( tab_for_window_size , text="  Window Size  " ,bg="#ffffff",borderwidth=1.5, padx=5, pady=0)
        window_size_frame.place(x=0, y=5, width=175, height=90)

        label_window_width = Label(window_size_frame, text="window width:", bg="#ffffff", font=('Calibri',10))
        label_window_height = Label(window_size_frame, text="window height:", bg="#ffffff", font=('Calibri',10))
        label_window_width.place(x=3, y=7)
        label_window_height.place(x=3, y=35)



        # calculations to make the frame take the screen size persentage !!!
        max_width_spin  = int(self.master.winfo_screenwidth())
        max_height_spin = int(self.master.winfo_screenheight())
        min_width_spin  = int(self.master.winfo_screenwidth() / 4)
        min_height_spin = int(self.master.winfo_screenheight() / 4)

        #set max position so the window don't disapaire
        max_left_spin  = int(self.master.winfo_screenwidth() - (self.master.winfo_screenwidth()/4))
        max_top_spin = int(self.master.winfo_screenheight() - (self.master.winfo_screenheight()/4))


        #spinboxs for width and height
        window_width_spinbox = Spinbox(window_size_frame, from_=min_width_spin, to=max_width_spin, textvariable=StringVar(value=self.window_width), width=7, increment=10, state = 'readonly', command=self.window_preview_changes)
        window_width_spinbox.place(x=100, y=8)
        window_height_spinbox = Spinbox(window_size_frame, from_=min_height_spin, to=max_height_spin, textvariable=StringVar(value=self.window_height), width=7, increment=10, state = 'readonly', command=self.window_preview_changes)
        window_height_spinbox.place(x=100, y=37)


        #
        #
        # Window Position Frame
        #
        #

        window_position_frame = LabelFrame( tab_for_window_size , text="  Window Position  " ,bg="#ffffff",borderwidth=1.5, padx=5, pady=0)
        window_position_frame.place(x=180, y=5, width=175, height=90)

        label_position_left = Label(window_position_frame, text="Left Position:", bg="#ffffff", font=('Calibri',10))
        label_position_top = Label(window_position_frame, text="Top Position:", bg="#ffffff", font=('Calibri',10))
        label_position_left.place(x=3, y=7)
        label_position_top.place(x=3, y=35)

        #spinboxs for top and left position
        window_left_spinbox = Spinbox(window_position_frame, from_=0, to=max_left_spin, textvariable=StringVar(value=self.window_left_position), width=7, increment=10, state = 'readonly', command=self.window_preview_changes)
        window_left_spinbox.place(x=100, y=8)
        window_top_spinbox = Spinbox(window_position_frame, from_=0, to=max_top_spin, textvariable=StringVar(value=self.window_top_position), width=7, increment=10, state = 'readonly', command=self.window_preview_changes)
        window_top_spinbox.place(x=100, y=37)



        #
        #
        # Window Position Preview Frame
        #
        #


        # i need a cup of "ATAY" for this 
        self.preview_frame_w = float(340)
        self.preview_frame_h = float(150)

        self.original_screen_width  = float(self.master.winfo_screenwidth()) # width of the screen
        self.original_screen_height = float(self.master.winfo_screenheight())

        self.width_persentage  = float(self.original_screen_width/self.preview_frame_w) #calculating persentage =D - making it dynamic
        self.height_persentage = float(self.original_screen_height/self.preview_frame_h)

        self.notebad_calc_width  = (float(config_window_width)/self.width_persentage)
        self.notebad_calc_height = (float(config_window_height)/self.height_persentage)

        self.notebad_calc_left_pos = (float(config_window_left)/self.width_persentage) # resizing position based on the width - check later 
        self.notebad_calc_top_pos = (float(config_window_top)/self.height_persentage)


        #Set default sizes from config after new calc - test later!
        position_preview_frame = LabelFrame( tab_for_window_size , text="  Preview Position  " ,bg="#ffffff",borderwidth=1.5, padx=5, pady=0)
        position_preview_frame.place(x=0, y=100, width=355, height=175)
        position_preview_inside_frame = Frame( position_preview_frame, width=self.preview_frame_w, height=self.preview_frame_h, bg="#000000")
        position_preview_inside_frame.place(x=0, y=0)


        #insert desktop image into the frame
        desktop_icon = Image.open( other_icons.get('desktop') )
        desktop_img = ImageTk.PhotoImage(desktop_icon)
        desktop_label = Label(position_preview_inside_frame, image=desktop_img,borderwidth=0)
        imgDict['desktop'] = desktop_img 
        desktop_label.pack()


        #Preview changes on the Frame
        global notebad_sample_preview
        notebad_sample_preview = Frame( position_preview_inside_frame, width=self.notebad_calc_width, height=self.notebad_calc_height, bg="#ffffff",borderwidth=0)
        notebad_sample_preview.place(x=self.notebad_calc_left_pos, y=self.notebad_calc_top_pos)

        #frame header background color, allow expand to see window header when resizing
        load_bar_frame_label = Label(notebad_sample_preview,bg="#546A78",borderwidth=0,padx=0,pady=0 )
        load_bar_frame_label.place( x=0, y=0, relwidth=1, height=8)

        #align small close icon to top right, using andchor=NE to prevent image resize
        load_close_frame_icon = Image.open( other_icons.get('close_frame') )
        load_close_frame_img = ImageTk.PhotoImage(load_close_frame_icon)
        load_close_frame_label = Label(notebad_sample_preview, image=load_close_frame_img,borderwidth=0)
        imgDict['close_frame'] = load_close_frame_img 
        load_close_frame_label.place(relx=1, x=0, y=0, anchor=NE)


        # Placing the NoteBook
        tab_control.place(x=0, y=0,width=400)

        # Action Buttons Frame
        action_buttons_frame = Frame( self.prefe_window)
        action_buttons_frame.place(x=0, y=340,width=388)

        cancel_button = Button( action_buttons_frame , text = "Cancel", relief=GROOVE, height=1,width=10,padx=1, pady=3, command=self.cancel_clicked)
        cancel_button.pack(side=RIGHT)
        apply_button = Button( action_buttons_frame , text = "Apply", relief=GROOVE, height=1,width=10,padx=1, pady=3, command=self.apply_clicked)
        apply_button.pack(side=RIGHT,padx=10)
        save_button = Button( action_buttons_frame , text = "Save", relief=GROOVE, height=1,width=10,padx=1, pady=3, command= self.save_clicked)
        save_button.pack(side=RIGHT)

        #self.prefe_window.mainloop()

    def get_config_default_font_color(self, *args):
        if self.style1:
            return config_font_style_1
        elif self.style2:
            return config_font_style_2
        elif self.style3:
            return config_font_style_3
        else:
            return self.font_color

    def get_config_default_bg_color(self):
        if self.style1:
            return config_bg_style_1
        elif self.style2:
            return config_bg_style_2
        elif self.style3:
            return config_bg_style_3
        else:
            return self.text_background

    def check_colors_btns_state(self, *args):
        if self.style1 | self.style2 | self.style3:
            font_choose_btn.config(state="disabled")
            background_choose_btn.config(state="disabled")
            entry_font_choose.config(state="disabled")
            entry_bg_choose.config(state="disabled")
        else:
            font_choose_btn.config(state="normal")
            background_choose_btn.config(state="normal")
            entry_font_choose.config(state="normal")
            entry_bg_choose.config(state="normal")

    def choose_font_color(self, *args):

        old_color = self.font_color
        self.font_color = askcolor()
        if self.font_color[1] is None:
            print("no font color were choosen!")
            self.font_color = old_color
        else:
            preview_frame_text.config(fg=self.font_color[1])
            entry_font_choose.config(fg=self.font_color[1], textvariable=StringVar(value=self.font_color[1]))
            
            preview_frame_text_font.config(fg=self.font_color[1])

            #### -- set new values-- ####
            self.font_color = self.font_color[1]
    
    def choose_bg_color(self, *args):
        old_background = self.text_background
        self.text_background = askcolor()
        if self.text_background[1] is None:
            print("no font color were choosen!")
            self.text_background = old_background
        else:
            entry_bg_choose.config(fg=self.text_background[1], textvariable=StringVar(value=self.text_background[1]))

            preview_frame_text.config(bg=self.text_background[1])
            preview_frame_bg.config(bg=self.text_background[1])

            preview_font_frame_bg.config(bg=self.text_background[1])
            preview_frame_text_font.config(bg=self.text_background[1])

            #### -- set new values-- ####
            self.text_background = self.text_background[1]
    
    def changeSize(self, *args):
        #### -- set new values-- ####
        self.font_size = fontsize_listbox.get(fontsize_listbox.curselection())

        if self.font_family is None:
            preview_frame_text.config(font=(config_font_style, self.font_size))
            preview_frame_text_font.config(font=(config_font_style, self.font_size))
        else:
            preview_frame_text.config(font=(self.font_family, self.font_size))
            preview_frame_text_font.config(font=(self.font_family, self.font_size))

    def changePolice(self, *args):
        #### -- set new values-- ####
        self.font_family = police_listbox.get(police_listbox.curselection())

        police_entry.config(textvariable=StringVar(value=self.font_family))

        if self.font_size is None:
            preview_frame_text.config(font=(self.font_family, config_font_size))
            preview_frame_text_font.config(font=(self.font_family, config_font_size))
        else:
            preview_frame_text.config(font=(self.font_family, self.font_size))
            preview_frame_text_font.config(font=(self.font_family, self.font_size))

    def set_ready_style(self, *args):
        self.theme_num = self.radio_style.get()

        entry_font_choose.config(state="disabled")
        entry_bg_choose.config(state="disabled")
        font_choose_btn.config(state="disabled")
        background_choose_btn.config(state="disabled")

        self.style1 = False
        self.style2 = False
        self.style3 = False

        if self.theme_num == 1:
            self.style1 = True
            self.style2 = False
            self.style3 = False

            self.font_color = config_font_style_1
            self.text_background = config_bg_style_1
        elif self.theme_num == 2:
            self.style1 = False
            self.style2 = True
            self.style3 = False

            self.font_color = config_font_style_2
            self.text_background = config_bg_style_2
        elif self.theme_num == 3:
            self.style1 = False
            self.style2 = False
            self.style3 = True

            self.font_color = config_font_style_3
            self.text_background = config_bg_style_3
        else:
            self.font_color = config_font_color
            self.text_background = config_text_background
            entry_font_choose.config(state="readonly")
            entry_bg_choose.config(state="readonly")
            font_choose_btn.config(state="normal")
            background_choose_btn.config(state="normal")

        #apply choosen styles to both frames
        preview_frame_text.config(fg=self.font_color)
        entry_font_choose.config(fg=self.font_color, textvariable=StringVar(value=self.font_color))
        preview_frame_text_font.config(fg=self.font_color)
        entry_bg_choose.config(fg=self.text_background, textvariable=StringVar(value=self.text_background))
        preview_frame_text.config(bg=self.text_background)
        preview_frame_bg.config(bg=self.text_background)
        preview_font_frame_bg.config(bg=self.text_background)
        preview_frame_text_font.config(bg=self.text_background)

    def window_preview_changes(self, *args):

        self.preview_frame_w = float(340)
        self.preview_frame_h = float(150)

        self.original_screen_width  = float(self.master.winfo_screenwidth()) 
        self.original_screen_height = float(self.master.winfo_screenheight())

        self.width_persentage  = (self.original_screen_width/self.preview_frame_w) 
        self.height_persentage = (self.original_screen_height/self.preview_frame_h)

        self.notebad_calc_width  = (float(window_width_spinbox.get())/self.width_persentage)
        self.notebad_calc_height = (float(window_height_spinbox.get())/self.height_persentage)

        self.notebad_calc_left_pos = (float(window_left_spinbox.get())/self.width_persentage)  
        self.notebad_calc_top_pos = (float(window_top_spinbox.get())/self.height_persentage)

        notebad_sample_preview.config(width=self.notebad_calc_width, height= self.notebad_calc_height)
        notebad_sample_preview.place(x=self.notebad_calc_left_pos, y=self.notebad_calc_top_pos)

    def cancel_clicked(self, *args):

        self.prefe_window.destroy()

    def apply_clicked(self, *args):
        if self.style1:
            conteur['ready_styles_settings']['style_1'] = str(True)
            conteur['ready_styles_settings']['style_2'] = str(False)
            conteur['ready_styles_settings']['style_3'] = str(False)
            self.content.config(fg=str(config_font_style_1),bg=str(config_bg_style_1))

        elif self.style2:
            conteur['ready_styles_settings']['style_1'] = str(False)
            conteur['ready_styles_settings']['style_2'] = str(True)
            conteur['ready_styles_settings']['style_3'] = str(False)
            self.content.config(fg=str(config_font_style_2),bg=str(config_bg_style_2))

        elif self.style3:
            conteur['ready_styles_settings']['style_1'] = str(False)
            conteur['ready_styles_settings']['style_2'] = str(False)
            conteur['ready_styles_settings']['style_3'] = str(True)
            self.content.config(fg=str(config_font_style_3),bg=str(config_bg_style_3))

        else:
            conteur['ready_styles_settings']['style_1'] = str(False)
            conteur['ready_styles_settings']['style_2'] = str(False)
            conteur['ready_styles_settings']['style_3'] = str(False)

            conteur['color_settings']['font_color']      = str(self.font_color)
            conteur['color_settings']['text_background'] = str(self.text_background)

            self.content.config(fg=str(self.font_color),bg=str(self.text_background))

        conteur['font_settings']['font_style'] = str(self.font_family)
        conteur['font_settings']['font_size']  = str(self.font_size)
        self.content.config(font=(str(self.font_family),str(self.font_size)))

        conteur['window_size_settings']['window_height'] = str(window_height_spinbox.get())
        conteur['window_size_settings']['window_width']  = str(window_width_spinbox.get())

        print(window_height_spinbox.get())

        conteur['window_position_settings']['window_top']  = str(window_top_spinbox.get())
        conteur['window_position_settings']['window_left'] = str(window_left_spinbox.get())

        self.master.geometry('%dx%d+%d+%d' % (int(window_width_spinbox.get()), int(window_height_spinbox.get()), int(window_left_spinbox.get()), int(window_top_spinbox.get())))


        #save changes in config file
        conteur.write(open('configuration.ini','w'))

        return 1

    def save_clicked(self, *args):
        if Settings_class.apply_clicked(self):
            self.prefe_window.destroy()



    


