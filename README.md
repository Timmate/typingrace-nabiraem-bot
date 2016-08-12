## typingrace-nabiraem-bot
A bot written in Python for [typingrace.nabiraem.ru][1] game competition on fast typing.

Python 3.X only. Supports only English and Russian keyboard languages.

## Installation
1. Install [Python 3.X][2] (for Windows users). Install `python3-pip` package if you are using Linux OS.
2. Clone this repository to your local machine. See [Atlassian's Git Tutorial][3] for details. Change working directory
to `typingrace-nabiraem-bot/`.
2. Use `pip install -r requirements.txt` to install all dependencies if you are using Windows OS. If you are a Linux user,
see [pyautogui docs][4] for installation details. Then try to run `pip install -r requirements.txt` in Terminal.
3. Modify `constants.py` file:
  * Set `TEXT_LANGUAGE`, `BUTTON`, `RACES`, `INTERVAL` game constants.

  * Set game elements coordinates and pixel RGB colors according to your screen resolution, OS and browser.
    `pyautogui.displayMousePosition()` could be of great help to deal with pixel coordinates and colors.
    Also, see the *images* directory for some help on finding the game elements' regions.


5. Feel free to experiment with setting different values to the `INTERVAL` constant to adjust typing speed.
6. Have some fun winning races with incredible scores!

## License
Copyright © 2016 TIm Kornev (@Timmate).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the *License* file included in this repository for further details.


[1]: http://typingrace.nabiraem.ru
[2]: https://www.python.org
[3]: https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone
[4]: http://pyautogui.readthedocs.io/en/latest/                                                     
