
# screen blanking app for kivy apps on Raspbery Pi 

Quick and dirty screensaver solution to force the screen on the Raspberry Pi to blanking mode (because – at least in my case – the kivy app suppresses the normal functioning of the Raspi's screensaver).<br>

As I didn't manage to get working the genuine screensaver, I wrote this small kivy app as a quick workaround. It opens a window on which sreen motions (mouse or touch) are detected and which forces the screen to blank mode after a certain time of inactivity.

## downsides:
It's only a workaround – a simple kivy window/app that sets the timer to zero every time it registrates a motion on this window. That means, the timer continues if this window is covered by another app (or minimized) and blanks the screen even when you're working on it. It's no problem to reactivate the screen, as a simple touch is enough to switch it on again. But later, before you leave the screen, this app has to be in front and reset by a touch, otherwise the timer continues above the threshold (e.g. 356/20) and doesn't reach it again (and therefore doesn't blank the screen).

## used hardware and software:
Python version 3.11<br>
Kivy version 2.2.1<br>
Raspberry Pi 4 with Debian GNU/Linux 11 (bullseye)<br>
4.3" touchscreen (DSI)<br>

## what worked for me:
To make an executable app from the code that can be easily started by simply clicking on it, I packaged the code with pyinstaller this way: 
- open the terminal in the folder where the code is saved (or open the terminal anywhere and go there with the cd keyword)
- type in the terminal:
pyinstaller my_code_to_package.py
- This creates some new files and folders in the folder where the original code is. The executable is found in a subfolder of "dist".
