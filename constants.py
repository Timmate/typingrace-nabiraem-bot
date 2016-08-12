#
# NAME         : constants.py
#
# DESCRIPTION  : Set the game elements coordinates and pixel RGB colors according
#                to your screen resolution, OS and browser.
#                `pyautogui.displayMousePosition()` could be of great help to deal
#                with pixel coordinates and colors. Also, see *images* directory
#                for some help on finding the game elements' regions.
#
# AUTHOR       : Tim Kornev (@Timmate on GitHub)
#
# CREATED DATE : 12th of August, 2016
#


# Set general constants.
# ======================

BUTTON = 'right'       # I am left-handed so right button is used for clicking,
                       # dragging, etc. Change this to 'left' if the left button
                       # is used primarily on your computer.
                       
RACES = 5              # specify here number of races

TEXT_LANGUAGE = 'ENG'  # specify here the language of the races' texts

DURATION = 0.3         # mouse move time

INTERVAL = 0.075       # time to wait after typing each character (type speed measure)
                       # i.e. 0.075 is apprx. 800 cpm
                       # and 0.1 is apprx. 600 cpm on my laptop.
                       # Note that the speed higher than 800 cpm is restricted by
                       # the Anti-Cheat app.

SCREENSHOTS_DIR_NAME = 'typingrace_nabiraem_screenshots'    # store screenshots with
                                                            # races' statistics. 

# Set main menu constants.
# ========================

START_BUTTON_COORDS = (575, 462)
START_BUTTON_COLOR = (147, 197, 75)     # colors's values are stored in RGB format
LOGIN_BUTTON_COORDS = (1213, 108)
LOGIN_BUTTON_COLOR = (244, 124, 60)
DOWN_ARROW_BUTTON_COORDS = (788, 462)
CCR_BUTTON_COORDS = (729, 556)          # CCR stands for Create Custom Race


# Set CCR menu constants.
# =======================

GEAR_COORDS = (234, 305)
GEAR_COLOR = (244, 124, 60)
LANGUAGE_FIELD_COORDS = (484, 240)
RUS_LANGUAGE_OPTION_COORDS = (465, 258)
ENG_LANGUAGE_OPTION_COORDS = (488, 276)

# Set game window constants.
# ==========================

RACER_COORDS = (66, 678)
RACER_COLOR = (230, 6, 7)


# Set statistics window constants.
# ================================

MAIN_MENU_BUTTON_COORDS = (1095, 156)
MAIN_MENU_BUTTON_COLOR = (192, 151, 13)
