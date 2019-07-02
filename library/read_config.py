# -*- coding: utf-8 -*-
###############################
##### -  Global variables used in library.py and ...
###############################


menu_icons_list = {
    'project_icons/menu_icons/1--new.png'                 : 'nouveau',
    'project_icons/menu_icons/2--open.png'                : 'fopen',
    'project_icons/menu_icons/3--save.png'                : 'save',
    'project_icons/menu_icons/5--copy.png'                : 'copy',
    'project_icons/menu_icons/6--cut.png'                 : 'cut',
    'project_icons/menu_icons/7--paste.png'               : 'paste',
    'project_icons/menu_icons/8--undo.png'                : 'undo',
    'project_icons/menu_icons/9--redo.png'                : 'redo',
    'project_icons/menu_icons/10--bold.png'               : 'bold',
    'project_icons/menu_icons/11--italic.png'             : 'italic',
    'project_icons/menu_icons/13--underline.png'          : 'underline',
    'project_icons/menu_icons/14--left-alignment.png'     : 'left_alignment',
    'project_icons/menu_icons/15--center-alignment.png'   : 'center_alignment',
    'project_icons/menu_icons/16--right-alignment.png'    : 'right_alignment',
    'project_icons/menu_icons/17--settings.png'           : 'settings_w',
    'project_icons/menu_icons/18--search.png'   	      : 'find'
}

other_icons = {
	'close_frame' : 'project_icons/other_icons/frame_close.png',
    'desktop' : 'project_icons/other_icons/desktop.png',
	'aboutme' : 'project_icons/other_icons/aboutme.png',
}

###############################
##### -  reading default values from configuration.ini
###############################

import configparser

conteur=configparser.ConfigParser()
conteur.read('configuration.ini')

config_font_style        = conteur.get('font_settings','font_style')
config_font_size         = conteur.get('font_settings','font_size')

config_font_color        = conteur.get('color_settings','font_color')
config_text_background   = conteur.get('color_settings','text_background')

config_window_height     = conteur.get('window_size_settings','window_height')
config_window_width      = conteur.get('window_size_settings','window_width')

config_show_icons        = conteur.get('menu_settings','show_icons')
config_show_shortcuts    = conteur.get('menu_settings','show_shortcuts')

config_window_top        = conteur.get('window_position_settings','window_top')
config_window_left       = conteur.get('window_position_settings','window_left')

config_style_1           = conteur.get('ready_styles_settings','style_1')
config_font_style_1      = conteur.get('ready_styles_settings','font_style_1')
config_bg_style_1        = conteur.get('ready_styles_settings','bg_style_1')

config_style_2           = conteur.get('ready_styles_settings','style_2')
config_font_style_2      = conteur.get('ready_styles_settings','font_style_2')
config_bg_style_2        = conteur.get('ready_styles_settings','bg_style_2')

config_style_3           = conteur.get('ready_styles_settings','style_3')
config_font_style_3      = conteur.get('ready_styles_settings','font_style_3')
config_bg_style_3        = conteur.get('ready_styles_settings','bg_style_3')

config_weight_text       = conteur.get('text_styles','weight')
config_slant_text        = conteur.get('text_styles','slant')
config_underline_text    = conteur.get('text_styles','underline')
config_alignment_text    = conteur.get('text_styles','alignment')
