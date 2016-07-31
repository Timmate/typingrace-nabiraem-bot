## typingrace-nabiraem-bot
The bot written in Python for [typingrace.nabiraem.ru](http://typingrace.nabiraem.ru) game competition on fast typing.

Python 3.x only. Supports only English and Russian keyboard languages.

## Installation
1. Install [Python 3.x](https://www.python.org).
2. Clone this repository to your local machine. See [Atlassian's Git Tutorial](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone) for details.
2. Use `pip install -r requirements.txt` to install all dependencies.
3. Modify the `typingrace_nabiraem_bot.py` file:
  * Set the game elements coordinates and pixel RGB colors according to your screen resolution, OS and browser.
`pyautogui.displayMousePosition()` could be of great help to deal with pixel coordinates.
Also, see the *images* directory for some help on finding the game elements regions.

  * Set the `TEXT_LANGUAGE`, `BUTTON`, `RACES`, `INTERVAL` game constants.

5. Feel free to experiment with setting different values for `INTERVAL` constant to adjust typing speed.
6. Have some fun winning races with incredible scores!

## License
Copyright © 2016 TIm Kornev (@Timmate).

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.
