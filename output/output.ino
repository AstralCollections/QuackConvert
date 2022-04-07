//Converted at 2022-04-07 03:16:51.857774
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
  // Default
  
  DigiKeyboard.delay(750);
  DigiKeyboard.sendKeyStroke(KEY_R, KEY_LEFT_GUI);
  
  DigiKeyboard.delay(1000);
  DigiKeyboard.print("powershell Start-Process notepad -Verb runAs");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  
  DigiKeyboard.delay(750);
  DigiKeyboard.sendKeyStroke(KEY_Y, KEY_LEFTALT);
  
  DigiKeyboard.delay(750);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.print("powershell.exe \"start google.com\"");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);

  delay(1000);
  while (1) {}
}
