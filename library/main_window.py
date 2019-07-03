# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

from tkinter.colorchooser import *
from library.settings_window import *

import tkinter.font as tkFont
from PIL import Image, ImageTk


#imports configparser and images list
from library.read_config import *

savedFile = {1:""}
imgDict={}

#======================================
# Principale Window
#======================================

class BlockNote_window:

    def __init__(self,master,content,icons_menu):
        self.master = master
        self.content=content
        self.icons_menu=icons_menu

        #initiat style variables
        self.all_variable_initiation()

    def create_window(self):
        self.master = Tk()
        self.master.title("Editeur de Texte")

        # set the dimensions of the screen 
        # and where it is placed base on conteur values
        self.master.geometry('%dx%d+%d+%d' % (int(config_window_width), int(config_window_height), int(config_window_left), int(config_window_top)))

    def add_text(self):
        self.content = Text(self.master,padx=10,pady=5, undo=True)
        self.content.config(fg=str(BlockNote_window.get_config_default_font_color(self)) ,bg=str(BlockNote_window.get_config_default_bg_color(self)))
        self.content.config(font=(config_font_style,config_font_size))
        self.content.pack(expand=1,side=BOTTOM,fill='both')

        #import text style from configuration.ini
        self.change_text_style(self.weight_v, self.underline_v, self.slant_v)
        
        # justify text  -- problem in loads first time - fix later
        self.content.tag_configure("%s" % self.alignment, justify=self.alignment.lower())
        self.content.tag_add("%s" % self.alignment, 1.0, "end")

    def generate(self):
        self.master.mainloop()

    #======================================
    # Some variables initiation
    #======================================

    def all_variable_initiation(self) :

        self.weight_v    = config_weight_text
        self.slant_v     = config_slant_text
        self.underline_v = eval(config_underline_text)
        self.alignment   = config_alignment_text

    #======================================
    # BarMenu Actions
    #======================================

    # New NotePad winodw
    def nouveau(self ,*args):
        import os
        os.popen("python main.py")

    # Open an Existing file
    def fopen(self, *args):
        file = self.master.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select File",filetypes = (("Text Files","*.txt"),("all files","*.*")))
        
        if file:
            self.master.title('{} - {}'.format(os.path.basename(file), "Editeur de texte"))
            self.content.delete(1.0, END)
            with open(file) as _file:
                self.content.insert(1.0, _file.read())


    # Save As Method
    def saveAs(self, *args):
        # create save dialog
        fichier=self.master.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Enregistrer Sous\
        ",filetypes = (("Fichier Texte","*.txt"),("Tous les fichiers","*.*")))

        if fichier:
            fichier = fichier + ".txt"
            
            savedFile[1] = fichier
            f = open(fichier,"w")
            s = self.content.get("1.0",END)
            f.write(s) 
            f.close()
       
    # Save Method 
    def save(self, *args):
        if(savedFile[1] ==""):
            self.saveAs()            
        else:
            f = open(savedFile[1],"w")
            s = self.content.get("1.0",END)
            f.write(s) 
            f.close() 

    # Exit Method
    def quitter(self):
        if messagebox.askokcancel("Are you sure?", "Please Confirm that you want to exit!"):
            self.master.quit()

    # Undo text changes
    def undo(self, event=None):
        try:
            self.content.edit_undo()
        except:
            print('Nothing to undo...')

    # redo text changes
    def redo(self, *args):
        try:
            self.content.edit_redo()
        except:
            print('Nothing to redo...')

    # Copy text
    def copy(self, *args):
        try:
            self.content.clipboard_clear()
            self.content.clipboard_append(self.content.selection_get())
        except:
            print('Nothing to copy...')

    # Cut text
    def cut(self, *args):
        try:
            self.copy()
            self.content.delete("sel.first","sel.last")  
        except:
            print('Nothing to cut...')

    # Paste Text
    def paste(self, *args):
        try:
            self.content.insert(INSERT, self.content.clipboard_get())
        except:
            print('Nothing to paste...')

    # Delete Selected text
    def clear(self,*args):
        sel = self.content.get(SEL_FIRST, SEL_LAST)
        if sel!='':
            self.content.delete(SEL_FIRST, SEL_LAST)
        else:
            print("Noting to clear")

    # Delete All text
    def clearall(self,*args):
        try:
            self.content.delete(1.0 , END)
        except:
            print('Nothing to clear...')

    # Select All text
    def selectAll(self, *args):
        self.content.tag_add(SEL, '1.0', END)
        self.content.mark_set(0.0, END)
        self.content.see(INSERT)

    def left_alignment(self , *args):
        self.content.tag_configure("LEFT",justify=LEFT)
        self.content.tag_add("LEFT", 1.0, "end")

        conteur['text_styles']['alignment']  = "LEFT"
        conteur.write(open('configuration.ini','w'))

    def right_alignment(self , *args):
        self.content.tag_configure("RIGHT",justify=RIGHT)
        self.content.tag_add("RIGHT", 1.0, "end")

        conteur['text_styles']['alignment']  = "RIGHT"
        conteur.write(open('configuration.ini','w'))

    def center_alignment(self , *args):
        self.content.tag_configure("CENTER",justify=CENTER)
        self.content.tag_add("CENTER", 1.0, "end")

        conteur['text_styles']['alignment']  = "CENTER"
        conteur.write(open('configuration.ini','w'))

    def bold(self,*args):

        if self.weight_v =="bold":
            self.weight_v = "normal"
        else:
            self.weight_v = "bold"
        self.change_text_style(self.weight_v, self.underline_v, self.slant_v)
      
    def underline(self,*args):

        if self.underline_v:
            self.underline_v = 0
        else:
            self.underline_v = 1
        self.change_text_style(self.weight_v, self.underline_v, self.slant_v)

    def italic(self,*args):
        if self.slant_v =="roman":
            self.slant_v = "italic"
        else:
            self.slant_v = "roman"
        self.change_text_style(self.weight_v, self.underline_v, self.slant_v)

    def change_text_style(self, boldness, underline, slant):
        styling = tkFont.Font(family=config_font_style, size=config_font_size,weight= boldness,slant=slant, underline=underline)
        self.content.configure(font=styling)

        conteur['text_styles']['underline']  = str(underline)
        conteur['text_styles']['weight']  = boldness
        conteur['text_styles']['slant']  = slant
        conteur.write(open('configuration.ini','w'))

    def find(self, *args):
        self.content.tag_remove('found', '1.0', END)
        target = simpledialog.askstring('Search', 'words to search:')
        simpledialog
        if target:
            idx = '1.0'
            while 1:
                idx = self.content.search(target, idx, nocase=1,
                        stopindex=END)
                if not idx:
                    break
                lastidx = '%s+%dc' % (idx, len(target))
                self.content.tag_add('found', idx, lastidx)
                idx = lastidx

            self.content.tag_config('found',foreground='white', background="blue")

    def open_about(self, *args):
        about_window = Toplevel(self.master)
        about_window.grab_set()
        about_window.title("About Me")
        about_window.geometry("250x150")
        about_window.resizable(False, False)
        about_window.configure(background='white')


        aboutme_icon = Image.open( other_icons.get('aboutme') )
        aboutme_icon = aboutme_icon.resize((100,100))
        aboutme_img = ImageTk.PhotoImage(aboutme_icon)
        aboutme_label = Label(about_window, image=aboutme_img,borderwidth=0, bg="white")
        imgDict['aboutme'] = aboutme_img 
        aboutme_label.pack()

        my_name= Label(about_window, text="SAIFEDDINE CHAGDALI",fg="black", bg="white", font=('Calibri',10))
        my_name.place(x=60, y=100)

        git_link= Label(about_window, text="github.com/sifdin17/TextEditor",fg="blue", bg="white",font=('Calibri',10))
        git_link.place(x=40, y=120)



    #======================================
    # action that opens the setting window
    #======================================

    def settings_w(self, *args):

        # New Settings Instance
        preference_window = Settings_class(self.master,self.content,"Settings_win")
        # Create all widgets
        preference_window.create_settings_window()


    #===========================
    # BarMenu Creation
    #===========================

    def add_menu(self):
        # 1 - Création de la barre des menus
        menuBar = Menu(self.master)
        
        # 2 - Création du menu Fichier
        global menuFichier
        menuFichier = Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label = "File", menu=menuFichier)
        menuFichier.add_command(label="New", command=self.nouveau)
        menuFichier.add_command(label="Open", command=self.fopen)
        menuFichier.add_command(label="Save", command=self.save)
        menuFichier.add_command(label="Save as", command=self.saveAs)
        menuFichier.add_separator()
        menuFichier.add_command(label="Exit", command = self.quitter) 
        self.master.config(menu = menuBar)
        
        #3 - Création du Menu Edition
        global menuEdition
        menuEdition= Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label = "Edit", menu=menuEdition)
        menuEdition.add_command(label="Undo", command = self.undo)
        menuEdition.add_command(label="Redo", command = self.redo)
        menuEdition.add_separator()
        menuEdition.add_command(label="Copy", command=self.copy)
        menuEdition.add_command(label="Cut", command = self.cut)
        menuEdition.add_command(label="Paste", command=self.paste)
        menuEdition.add_separator()
        menuEdition.add_command(label="Delete",command=self.clear)
        menuEdition.add_command(label="Delete All",command=self.clearall)
        menuEdition.add_command(label="Select All",command=self.selectAll)

       
        # Création du Menu Options
        menuOutils = Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label = "Tools", menu = menuOutils)

        global show_icons_menucheck, show_shortcuts_menucheck

        show_icons_menucheck = IntVar()
        show_icons_menucheck.set(config_show_icons)
        menuOutils.add_checkbutton(label='Show Icons',onvalue=1, offvalue=0, variable=show_icons_menucheck, command=self.toggle_icons)

        show_shortcuts_menucheck = IntVar()
        show_shortcuts_menucheck.set(config_show_shortcuts)
        menuOutils.add_checkbutton(label='Show Shortcuts',onvalue=True, offvalue=False, variable=show_shortcuts_menucheck, command=self.toggle_shortcuts)


        menuOutils.add_separator()
        menuOutils.add_command(label="Settings", command=self.settings_w)
        
        # Création du Menu Aide
        menuAide = Menu(menuBar,tearoff=0)
        menuBar.add_cascade(label = "Help", menu = menuAide)
        menuAide.add_command(label="About",command=self.open_about)

        if config_show_shortcuts:
            BlockNote_window.add_shortcuts_to_menu(self)

    #===========================
    # BarMenu Checkbuttons Action
    #===========================

    def toggle_shortcuts(self):
        if show_shortcuts_menucheck.get():
            BlockNote_window.add_shortcuts_to_menu(self)
        else:
            BlockNote_window.remove_shortcuts_from_menu(self)

        conteur['menu_settings']['show_shortcuts']  = str( show_shortcuts_menucheck.get() )
        conteur.write(open('configuration.ini','w'))

    def add_shortcuts_to_menu(self, *args):

        menuFichier.entryconfig(0, accelerator='Ctrl+N')
        menuFichier.entryconfig(1, accelerator='Ctrl+O')
        menuFichier.entryconfig(2, accelerator='Ctrl+S')

        menuEdition.entryconfig(0, accelerator='Ctrl+Z')
        menuEdition.entryconfig(1, accelerator='Ctrl+Y')
        menuEdition.entryconfig(3, accelerator='Ctrl+C')
        menuEdition.entryconfig(4, accelerator='Ctrl+X')
        menuEdition.entryconfig(5, accelerator='Ctrl+V')
        menuEdition.entryconfig(9, accelerator='Ctrl+A')

        # bind shortcuts to menuBar

        self.content.bind('<Control-N>', self.nouveau)
        self.content.bind('<Control-n>', self.nouveau)
        self.content.bind('<Control-O>', self.fopen)
        self.content.bind('<Control-o>', self.fopen)
        self.content.bind('<Control-S>', self.save)
        self.content.bind('<Control-s>', self.save)
        self.content.bind('<Control-z>', self.undo)
        self.content.bind('<Control-Z>', self.undo)
        self.content.bind('<Control-y>', self.redo)
        self.content.bind('<Control-Y>', self.redo)
        self.content.bind('<Control-c>', self.copy)
        self.content.bind('<Control-C>', self.copy)
        self.content.bind('<Control-x>', self.cut)
        self.content.bind('<Control-X>', self.cut)
        self.content.bind('<Control-v>', self.paste)
        self.content.bind('<Control-V>', self.paste)
        self.content.bind('<Control-A>', self.selectAll)
        self.content.bind('<Control-a>', self.selectAll)

    def remove_shortcuts_from_menu(self, *args):
        menuFichier.entryconfig(0, accelerator='')
        menuFichier.entryconfig(1, accelerator='')
        menuFichier.entryconfig(2, accelerator='')

        menuEdition.entryconfig(0, accelerator='')
        menuEdition.entryconfig(1, accelerator='')
        menuEdition.entryconfig(3, accelerator='')
        menuEdition.entryconfig(4, accelerator='')
        menuEdition.entryconfig(5, accelerator='')
        menuEdition.entryconfig(9, accelerator='')

        """# unbind shortcuts from menuBar 
        self.content.unbind('<Control-N>', self.nouveau)
        self.content.unbind('<Control-n>', self.nouveau)
        self.content.unbind('<Control-O>', self.fopen)
        self.content.unbind('<Control-o>', self.fopen)
        self.content.unbind('<Control-S>', self.save)
        self.content.unbind('<Control-s>', self.save)
        self.content.unbind('<Control-z>', self.undo)
        self.content.unbind('<Control-Z>', self.undo)
        self.content.unbind('<Control-y>', self.redo)
        self.content.unbind('<Control-Y>', self.redo)
        self.content.unbind('<Control-c>', self.copy)
        self.content.unbind('<Control-C>', self.copy)
        self.content.unbind('<Control-x>', self.cut)
        self.content.unbind('<Control-X>', self.cut)
        self.content.unbind('<Control-v>', self.paste)
        self.content.unbind('<Control-V>', self.paste)
        self.content.unbind('<Control-A>', self.selectAll)
        self.content.unbind('<Control-a>', self.selectAll)"""

    def add_icons_menu(self):
        self.icons_menu=Frame(height=10,borderwidth=0, padx=5, pady=0)
        self.icons_menu.pack(side=TOP,fill=X)

    def add_icons(self):
        i = 0
        for path, bind_function in menu_icons_list.items():

            load = Image.open(path)
            load = load.resize((16,16))
            img = ImageTk.PhotoImage(load)

            label_name = bind_function+"_label" # problem d smya -- fix later !

            label_name = Label(self.icons_menu,cursor="hand2", image=img)
            imgDict[path] = img # save image ref in imgDict -- keep track of the reference or else it wont work!!! 
            label_name.pack(side=LEFT,padx=2,pady=5)

            bind_function = "self."+bind_function 
            label_name.bind( "<Button>", eval( bind_function )) # convert string into variable name 

            #add space between labels - just for styling
            i = i+1
            if i in [3,6,8,11,14]:
                label_name = str(i)+"_label"
                label_name = Label(self.icons_menu,text="|",fg="#cccccc",width=0)
                label_name.pack(side=LEFT,padx=5,pady=0)
                
    def toggle_icons(self):
        if show_icons_menucheck.get():
            self.add_icons_menu()
            self.add_icons()
        else:
            self.icons_menu.pack_forget()

        conteur['menu_settings']['show_icons']  = str( show_icons_menucheck.get() )
        conteur.write(open('configuration.ini','w'))

        
    #===================================================
    # reading default style colors from configuration.ini
    #===================================================

    def get_config_default_font_color(self):

        print( eval(config_style_1) )
        if eval(config_style_1):
            return config_font_style_1
        elif eval(config_style_2):
            return config_font_style_2
        elif eval(config_style_3):
            return config_font_style_3
        else:
            return config_font_color

    def get_config_default_bg_color(self):
        if eval(config_style_1):
            return config_bg_style_1
        elif eval(config_style_2):
            return config_bg_style_2
        elif eval(config_style_3):
            return config_bg_style_3
        else:
            return config_text_background

