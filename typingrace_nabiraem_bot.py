#! python3
#
# NAME         : typingrace_nabiraem_bot.py
#
# VERSION      : 1.0
#
# DESCRIPTION  : A bot for typingrace.nabiraem.ru game competition on fast typing.
#
# AUTHOR       : Tim Kornev (@Timmate on GitHub)
#
# CREATED DATE : 27th of July, 2016
#


import os
import time
import logging
import re
import random

import pyautogui
import requests
import bs4
import pyperclip

from constants import *
from lang_dicts import rus_eng_dict


pyautogui.PAUSE = 0.5

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%H:%M:%S')
# Uncomment the line below to disable logging.
# logging.disable(logging.INFO)


# Start the program.
# ==================

logging.info('\n\n' + ' PROGRAM STARTED '.center(70, '_') + '\n')
logging.info('Press Ctrl-C to abort at any time.')
logging.info('To interrupt mouse movement, move mouse to upper left corner.')
# Print the prettified race text language.
logging.info('\n\n' + ' Language: {} '.center(70, ':').format(TEXT_LANGUAGE) + '\n')
os.makedirs(SCREENSHOTS_DIR_NAME, exist_ok=True)  # create dir for
                                                  # screenshots.

# try/except is used here to handle the KeyboardInterrupt exception that
# could be raised by pressing Ctrl-C hotkey combination.
try:
    for race in range(RACES):   # race *RACES* times.

        # Print the prettified race number.
        logging.info('\n\n' + ' RACE {} '.center(70, '=').format(str(race + 1)) + \
                      '\n')


# Navigate through the main menu.
# ===============================

        # Check whether the main page window is opened by locating the
        # green Start button.
        main_page_found = False
        x, y = START_BUTTON_COORDS
        color = START_BUTTON_COLOR

        while not main_page_found:
            if pyautogui.pixelMatchesColor(x, y, color):
                main_page_found = True
                logging.info('I am on the main page.')
            else:
                logging.info('Could not find the green Start button. Where am I?')
                time.sleep(1)

        # Check whether the user is logged in.  If not, the custom race
        # cannot be created.
        pyautogui.moveTo(500, 600)  # move mouse to some position in the
                                    # center so that it does not hover
                                    # over login button as in that case
                                    # it changes it's color to a darker one.

        x, y = LOGIN_BUTTON_COORDS
        color = LOGIN_BUTTON_COLOR  # that is original Login button's color

        if pyautogui.pixelMatchesColor(x, y, color):
            logging.info('The user is not logged in.')
            logging.info('End of the program.')
            raise Exception('The custom race cannot be created unless ' + \
                            'the user is logged in.')
        else:
            logging.info('The user is logged in.')
            logging.info('OK. Continue.')

        # Open dropdown menu by clicking the little Down Arrow button
        # (on the right side of the Start button), then click Create Custom
        # Race button.
        x, y = DOWN_ARROW_BUTTON_COORDS
        pyautogui.click(x, y, button=BUTTON, duration=DURATION)
        x, y = CCR_BUTTON_COORDS
        pyautogui.click(x, y, button=BUTTON, duration=DURATION)
        logging.info('Clicked Create Custom Race button.')

        # Check whether the CCT menu is loaded by locating
        # the orange gears.
        ccr_menu_found = False
        x, y = GEAR_COORDS
        color = GEAR_COLOR

        while not ccr_menu_found:
            if pyautogui.pixelMatchesColor(x, y, color):
                ccr_menu_found = True
                logging.info('A am creating the custom race...')
            else:
                logging.info('Could not find the CCR menu.')
                time.sleep(1)


# Create the custom race.
# =======================

        # Whatever the language of the race text is, change it
        # to *TEXT_LANGUAGE*.
        x, y = LANGUAGE_FIELD_COORDS
        pyautogui.click(x, y, button=BUTTON, duration=DURATION)  # open the Language
                                                                 # dropdown menu
        if TEXT_LANGUAGE == 'ENG':
            x, y = ENG_LANGUAGE_OPTION_COORDS
            pyautogui.click(x, y, button=BUTTON, duration=DURATION)  # click English
                                                                     # language label
            pyautogui.typewrite('\t' * 5)  # go to the Number Of
                                           # Participants radio button.
        elif TEXT_LANGUAGE == 'RUS':
            x, y = RUS_LANGUAGE_OPTION_COORDS
            pyautogui.click(x, y, button=BUTTON, duration=DURATION)  # click Russian
                                                                     # language label
            pyautogui.typewrite('\t' * 6)   # go to the Number Of
                                            # Participants radio button.
                                            # In Russian CCR menu there
                                            # is also the Text field for
                                            # choosing the text type that
                                            # should be skipped.

        logging.info('Changed the language of the race text to {}.'.format(TEXT_LANGUAGE))

        for i in range(random.randint(0, 3)):  # choose a random number of
            pyautogui.press('right')           # participants.

        pyautogui.typewrite('\t' * 3)          # go to the Go button
        pyautogui.press('enter')               # hit the Go button


# Enter the race.
# ===============

        # Wait until the race window is loaded by locationg the racer in
        # red.
        race_window_found = False
        x, y = RACER_COORDS
        color = RACER_COLOR

        while not race_window_found:
            if pyautogui.pixelMatchesColor(x, y, color):
                race_window_found = True
                logging.info('I see the race game window.')
            else:
                logging.info('Could not find the race game window.')
                time.sleep(1)


# Extract the text.
# =================

        # The race text can be extracted from one of the html elements.

        pyautogui.hotkey('ctrl', 'l')     # press Ctrl-L hotkey combo to
                                          # go to the link of the webpage.
        pyautogui.hotkey('ctrl', 'c')     # press Ctrl-C hotkey combo to
                                          # copy the link.
        pyautogui.press('esc')            # press Esc to close the link panel.
        url = pyperclip.paste()

        race_id = '#' + os.path.basename(url)
        logging.info('Entered the race {}.'.format(race_id))

        # Parse the html code with Beautiful Soup.
        res = requests.get(url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        if TEXT_LANGUAGE == 'ENG':
            # Find the element with the race text.
            elem_with_text = soup.select('script[type="text/javascript"]')

            # Use this regex to grab the race text.
            text_regex = re.compile(r'''
            \"parts\"\:\[\"
            (.*)                    # this group stores the race text
            \"\]
            ''', re.VERBOSE)

            data = elem_with_text[35].getText()
            data = data.replace('\\n', ' ').replace('\\', '') #
            mo = text_regex.search(data)     # 'mo' stands for Match objects
            race_text = mo.group(1) + ' '    # store the clean result here
            race_text = race_text.replace('","', ' ') # sometimes the text will have
                                                      # two parts separated with
                                                      # "," characters

            # Change the keyboard input language to English.
            x, y = LANGUAGE_BAR_COORDS
            pyautogui.click(x, y, button=BUTTON, duration=DURATION)
            x, y = LANGUAGE_BAR_ENG_COORDS
            pyautogui.click(x, y, button=BUTTON, duration=DURATION)

        elif TEXT_LANGUAGE == 'RUS':
            # If *TEXT_LANGUAGE* is not English, translit the text to English.
            # NOTE: different html tags are used for scrapping the text
            # data in English and Russian languages.
            elem_with_text = soup.select('textarea')
            data = elem_with_text[0].text
            # We need to clean text a bit to get exactly what we want.
            data = data.replace('=', '').replace('\n', ' ').replace('  ', ' ')

            # Use this regex to grab the race text.
            text_regex = re.compile(r'''
                \#
                \d+
                (.+)   # this group stores the race text
                ''', re.VERBOSE)

            mo = text_regex.search(data)
            race_text = mo.group(1)[1:]
            # Use list comprehension concept for transliting the text
            # to English: if char is in dict's keys, translit it with
            # the dict key's value.  Otherwise, do nothing with that char (for
            # some symbols like '%', '!', '*' that could be typed using the
            # same key on Rus and Eng keyboards).
            race_text = ''.join([rus_eng_dict[char] if char in rus_eng_dict.keys() \
                                 else char for char in race_text])

            # Change the keyboard input language to Russian.
            x, y = LANGUAGE_BAR_COORDS
            pyautogui.click(x, y, button=BUTTON, duration=DURATION)
            x, y = LANGUAGE_BAR_RUS_COORDS
            pyautogui.click(x, y, button=BUTTON, duration=DURATION)


# Wait for beginning of the race.
# ===============================

        # Wait for beginning of the race by checking html's <title> tag.
        # When the race begins, title changes from "#<race_id>" to "Информация
        # о заезде #<race_id>" and countdown begins.
        title_text = ''    # use empty string instead of None as NoneType object
                           # is not iterable (for the first iteration).
        go_title = 'Информация'
        while not go_title in title_text:
            # Update the page and check the title until it changes.
            res = requests.get(url)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            title_elem = soup.select('title')
            title_text = title_elem[0].getText()
            logging.info('Waiting for beginning of the race...')
            time.sleep(1)

        logging.info('The countdown begins.')


# Type the text.
# ==============

        time.sleep(8)   # it takes apprx. 8 seconds from the title change
                        # to the actual beginning of the race
        logging.info('The race begins. I am going to win it.')
        # Some first chars should be typed with a bit lower speed than
        # the specified value of *INTERVAL* in order to avoid the
        # Anti-Cheat ban.
        pyautogui.typewrite(race_text[:10], interval=0.15)
        pyautogui.typewrite(race_text[10:], interval=INTERVAL)


# Return to the main menu.
# ========================

        # Check whether the race statistics window is loaded by locating
        # the white-yellow "Список гонок" button.  Note that this block of code
        # also handles Anti-Cheat app ban message as it also has this button.
        statistics_window_found = False
        x, y = MAIN_MENU_BUTTON_COORDS
        color = MAIN_MENU_BUTTON_COLOR
        # The same thing as with the login button: make sure
        # the cursor does not hover over the button so that it changes it's
        # color to a darker one.
        pyautogui.moveTo(500, 500)

        while not statistics_window_found:
            if pyautogui.pixelMatchesColor(x, y, color):
                statistics_window_found = True
                pyautogui.screenshot(os.path.join(SCREENSHOTS_DIR_NAME, 'race_{}.png'.format(str(race + 1))))
                logging.info('The race is over.')
                logging.info('Took a screenshot of the race statistics.')

            else:
                logging.info('Could not see the statistics window.')
                time.sleep(1)

        # Click the Main Menu button.
        pyautogui.click(x, y, button=BUTTON, duration=DURATION)
        logging.info('Clicked the Main Menu button.')


    # End the program when the 'for' loop is over.
    logging.info('\n\n' + ' END OF THE PROGRAM '.center(70, '_') + '\n\n')


except KeyboardInterrupt: # handle the exception
    logging.info('\n\n' + ' END OF THE PROGRAM '.center(70, '_') + '\n\n')
