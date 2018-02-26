# Key-Sprint

_  __            ____             _       _   
| |/ /___ _   _  / ___| _ __  _ __(_)_ __ | |_
| ' // _ \ | | | \___ \| '_ \| '__| | '_ \| __|
| . \  __/ |_| |  ___) | |_) | |  | | | | | |_
|_|\_\___|\__, | |____/| .__/|_|  |_|_| |_|\__|
         |___/        |_|                     

Hey! Thanks for your interest in Key Sprint!


In this file, we'll be discussing a few things:

* Compatibility
* Requirements
* Installation
* Tutorial
* Troubleshooting
* FAQ
* Credits



COMPATIBILITY
-------------

This script has been written and tested for:

* OS X Yosemite Version 10.10.3 (https://support.apple.com/kb/DL1804)

We do not provide support for any platforms not listed above.



REQUIREMENTS
------------

This script requires the following:

* Python 2.7.10 (https://www.python.org/downloads/release/python-2710/)
* Python sys module (https://docs.python.org/2/library/sys.html)
* Python time module (https://docs.python.org/2/library/time.html)
* Python os module (https://docs.python.org/2/library/os.html)
* Python string module (https://docs.python.org/2/library/string.html)
* Python random module (https://docs.python.org/2/library/random.html)
* Python getch module (https://pypi.python.org/pypi/getch)
* Python getpass module (https://docs.python.org/2/library/getpass.html)
* Python subprocess module (https://docs.python.org/2/library/subprocess.html)



INSTALLATION
------------

All Apple computers ship with Python 2.7.10 installed.
Most of the required modules for Key Sprint to function properly should also come pre-installed.

If for some reason your computer does not have Python 2.7.10, then you'll need to do the following:

1. Visit https://www.python.org/downloads/release/python-2710/
2. Select "Mac OS X 64-bit/32-bit installer"
3. Once the download is completed, just run the file and you'll be fitted with a clean install of Python 2.7.10

You will need to manually install the Python getch module included in your download.
To do this, please complete the following:

1. Navigate to your KeySprint folder through Terminal
2. Type "cd requirements/getch" into Terminal
3. Type "python setup.py install"




TUTORIAL
--------

To start your Computer Tools script, you'll need to do the following:

1. Move the folder "KeySprint" to your Desktop.
2. Open the "Terminal" application
3. Type "cd Desktop" into Terminal and press Enter
4. Type "cd KeySprint" into Terminal and press Enter
5. Type "python game.py" into Terminal and press Enter
6. Done! The script should start and provide further instructions.



TROUBLESHOOTING
---------------

* If Terminal's output included "No such file or directory" at any point:

 - Are you sure you moved the "KeySprint" folder to your Desktop?

 - Did you rename the "KeySprint" folder? If so, please change the name back to "KeySprint".

* If the game didn't run when you typed "python game.py":

 - Are you sure you have Python 2.7.10 installed?



FAQ
---

* How do I reset the highscore?

 - Simply delete the "highscore.txt" file from the "KeySprint" folder



CREDITS
-------

* Contributers

 - Matthew Rosca-Halmagean
 - Rachel Connelly

* Instructors

 - Mr. Wegscheid

* Big text formatter

 - www.bigtext.org

* Python-related questions

 - www.stackoverflow.com
