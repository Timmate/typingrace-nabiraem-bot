## typingrace-nabiraem-bot

A bot for [typingrace.nabiraem.ru][1] game competition on fast typing.

Python 3.x only (for Python 2.x backward compatibility see [this][2]).

Supports only English and Russian keyboard languages.

### Installation & Usage

1. Use `pip install -r requirements.txt` to install all dependencies.
   If you are a Linux user, you may experience issues with `pyautogui`.
   See [pyautogui docs][3] for installation details.
2. Configure `constants.py` file:
  * Set `TEXT_LANGUAGE`, `BUTTON`, `RACES`, `INTERVAL` game constants.

  * Set game elements' coordinates and pixels' RGB colors according to your
    screen resolution, OS and browser. `pyautogui.displayMousePosition()`
    function could be of great help to deal with that.
    Also, see *Images* directory for some help on finding the game elements' regions.

3. Feel free to experiment with setting different values to the `INTERVAL`
   constant to adjust typing speed.
4. To interrupt the program and regain control of the mouse, move the mouse to the top-left corner of your screen.

5. Have some fun winning races with incredible scores!


### License

Copyright © 2016 Tim Kornev (@Timmate).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the *License* file included in this repository for further details.


[1]: http://typingrace.nabiraem.ru
[2]: http://python-future.org/quickstart.html
[3]: http://pyautogui.readthedocs.io/en/latest/                                                     
