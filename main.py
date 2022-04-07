import argparse, os
from datetime import datetime
from shutil import copyfile

ducky_format = {'gui': 'KEY_LEFT_GUI', 'windows': 'KEY_LEFT_GUI', 'enter': 'KEY_ENTER', ' ': 'KEY_SPACEBAR', 'space': 'KEY_SPACEBAR', 'escape': 'KEY_ESCAPE', 'backspace': 'KEY_BACKSPACE', 'tab': 'KEY_TAB', 'capslock': 'KEY_CAPS_LOCK', 'printscreen': 'KEY_PRINTSCREEN', 'scrolllock': 'KEY_SCROLL_LOCK', 'pause': 'KEY_PAUSE', 'insert': 'KEY_INSERT', 'home': 'KEY_HOME', 'pagup': 'KEY_PAGEUP', 'delete': 'KEY_DELETE', 'end': 'KEY_END', 'pagedown': 'KEY_PAGEDOWN', 'uparrow': 'KEY_UPARROW', 'downarrow': 'KEY_DOWNARROW', 'leftarrow': 'KEY_LEFTARROW', 'rightarrow': 'KEY_RIGHTARROW', 'up': 'KEY_UPARROW', 'down': 'KEY_DOWNARROW', 'left': 'KEY_LEFTARROW', 'right': 'KEY_RIGHTARROW', 'numlock': 'KEYPAD_NUMLOCK', 'keypad_enter': 'KEYPAD_ENTER', 'mute': 'KEY_MUTE', 'volumeup': 'KEY_VOLUME_UP', 'volumedown': 'KEY_VOLUME_DOWN', 'lockingcaps': 'KEY_LOCKING_CAPS_LOCK', 'lockingnum': 'KEY_LOCKING_NUM_LOCK', 'lockingscroll': 'KEY_LOCKING_SCROLL_LOCK', 'leftcontrol': 'KEY_LEFTCONTROL', 'leftshift': 'KEY_LEFTSHIFT', 'shift': 'KEY_LEFTSHIFT', 'leftalt': 'KEY_LEFTALT', 'alt': 'KEY_LEFTALT', 'leftgui': 'KEY_LEFT_GUI', 'rightcontrol': 'KEY_RIGHTCONTROL', 'ctrl': 'KEY_RIGHTCONTROL', 'rightshift': 'KEY_RIGHTSHIFT', 'rightalt': 'KEY_RIGHTALT', 'rightgui': 'KEY_RIGHT_GUI', 'menu': 'KEY_MENU', 'f1': 'KEY_F1', 'f2': 'KEY_F2', 'f3': 'KEY_F3', 'f4': 'KEY_F4', 'f5': 'KEY_F5', 'f6': 'KEY_F6', 'f7': 'KEY_F7', 'f8': 'KEY_F8', 'f9': 'KEY_F9', 'f10': 'KEY_F10', 'f11': 'KEY_F11', 'f12': 'KEY_F12', 'a': 'KEY_A', 'b': 'KEY_B', 'c': 'KEY_C', 'd': 'KEY_D', 'e': 'KEY_E', 'f': 'KEY_F', 'g': 'KEY_G', 'h': 'KEY_H', 'i': 'KEY_I', 'j': 'KEY_J', 'k': 'KEY_K', 'l': 'KEY_L', 'm': 'KEY_M', 'n': 'KEY_N', 'o': 'KEY_O', 'p': 'KEY_P', 'q': 'KEY_Q', 'r': 'KEY_R', 's': 'KEY_S', 't': 'KEY_T', 'u': 'KEY_U', 'v': 'KEY_V', 'w': 'KEY_W', 'x': 'KEY_X', 'y': 'KEY_Y', 'z': 'KEY_Z', '1': 'KEY_1', '2': 'KEY_2', '3': 'KEY_3', '4': 'KEY_4', '5': 'KEY_5', '6': 'KEY_6', '7': 'KEY_7', '8': 'KEY_8', '9': 'KEY_9', '0': 'KEY_0'}
global last_command

def sendKeyStroke(i):
    space_split = i.split(" ")
    o = "DigiKeyboard.sendKeyStroke("

    if len(space_split) > 1:
        for x in range(0, len(space_split)):
          if x>=1 and x<len(space_split):
            o = o + ", "

          try: o = o + ducky_format[space_split[x].lower()]
          except: pass

          if x == len(space_split) - 1:
            o = o + ");"

    else:
        o = o + ducky_format[space_split[0].lower()]
        o = o + ");"

    return o

def sendModKeyStroke(i):
    space_split = i.split(" ")

    o = "DigiKeyboard.sendKeyStroke("

    if len(space_split) > 1:
        for x in range(1, len(space_split)):
          if x>=2 and x<len(space_split):
            o = o + ", "
          o = o + ducky_format[space_split[x].lower()]

          if x == len(space_split) - 1:
            o = o + ", " + ducky_format[space_split[0].lower()] + ");"
    else:
        o = o + ducky_format[space_split[0].lower()]
        o = o + ");"

    return o

def parseDuckyLine(i):
  global last_command

  o = ""
  space_split = i.split(" ")

  if space_split[0] == "DELAY":
    o = "\n  DigiKeyboard.delay(" + space_split[1] + ");"

  elif space_split[0] == "REM":
    o = "// " + space_split[1]

  elif space_split[0] == "STRING":
    string = i[7:]
    string = string.replace("\\", "\\\\")
    string = string.replace("\"", "\\\"")
    o = "DigiKeyboard.print(\""
    o = o + string
    o = o + "\");"

  elif space_split[0] == "REPLAY":
    o = "for (int i=0; i < " + space_split[1] + "; i++) {\n"
    o = o + '    ' + last_command
    o = o + "\n  }"

  elif space_split[0] == "GUI" or space_split[0] == "ALT" or space_split[0] == "CTRL" or space_split[0] == "SHIFT":
    o = sendModKeyStroke(i)

  elif space_split[0] == "CTRL-SHIFT":
    space_split = i.space_split(" ")
    o = "DigiKeyboard.sendKeyStroke(" + ducky_format[space_split[1].lower()] + ", " + "KEY_LEFTCONTROL | KEY_LEFTSHIFT);"

  elif space_split[0] == "CTRL-ALT":
    space_split = i.space_split(" ")
    o = "DigiKeyboard.sendKeyStroke(" + ducky_format[space_split[1].lower()] + ", " + "KEY_LEFTCONTROL | KEY_LEFTALT);"

  elif space_split[0] == "ALT-SHIFT":
    space_split = i.space_split(" ")
    o = "DigiKeyboard.sendKeyStroke(" + ducky_format[space_split[1].lower()] + ", " + "KEY_LEFTALT | KEY_LEFTSHIFT);"

  else:
    o = sendKeyStroke(i)

  last_command = o
  return o

parser = argparse.ArgumentParser(
    description='Convert Rubber Ducky scripts to an Arduino sketch that can run on the DigiSpark ATtiny85 USB device.', 
    epilog="Quack Quack"
)

parser.add_argument('--script', help='Ducky script to convert')
parser.add_argument('--out', help='Output script directory')

args = parser.parse_args()

infile = open(args.script)
outdir = os.getcwd() + '/' + args.out
if os.path.isdir(outdir) == False: os.mkdir(outdir)
destpath = outdir + '/' + args.out + '.ino'
dest = open(destpath, 'w')

dest.write("//Converted at " + str(datetime.now()))

dest.write('''
#include "keymap.h"

#include "DigiKeyboard.h"

#define KEYSTROKE_DELAY 1000

int iterationCounter = 0;

void setup() {
  pinMode(0, OUTPUT); //LED on Model B
  pinMode(1, OUTPUT); //LED on Model A
  digitalWrite(0, LOW); // turn the LED off by making the voltage LOW
  digitalWrite(1, LOW);
}

void loop() {
    DigiKeyboard.update();
    DigiKeyboard.sendKeyStroke(0);
    DigiKeyboard.delay(KEYSTROKE_DELAY);
''')

for line in infile:
  if line.strip() != '':
    outString = parseDuckyLine(line.strip())
    dest.write('  ' + outString + '\n')

dest.write('''
  delay(1000);
  while (1) {}
}
''')
copyfile("keymap.h", outdir + '/' + "keymap.h")

print(f'''
Input File..: {args.script}
Output Dir..: {outdir}
Desitination: {destpath}
''')