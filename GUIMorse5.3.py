# SIT210 5.3D
## Code template used from core-electronics.com.au, thanks heaps! ##
## Also used my code from SIT210 2.1P ##
## Blink text entered in Morse Code ##

# import the required libraries
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import sys
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)

### HARDWARE DEFINITIONS ###
led=LED(15)

### GUI DEFINITIONS ###
window = Tk()
window.title("LED Morse Transaltor")
windowFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

# Morse variables
oneUnit = 0.3
dot = oneUnit
dash = 3 * oneUnit
pauseMidLetter = oneUnit
pauseAfterLetter = 3 * oneUnit
pauseAfterWord = 7 * oneUnit

placeholderText = "text to blink in morse"
textTooLongPlaceholder = "only up to 12 characters"

### Event Functions ###
# iterates through the string and blinks the right morse code
# this is long, sorry. usually i'd use a switch statement, but all
# the python hacks for a switch were just as inelegant...
def morseBlink():
    textEntry = entryField.get().upper()
    if len(textEntry) > 12:
        entryField.delete(0, tkinter.END)
        entryField.insert(10, textTooLongPlaceholder)
        return
    if textEntry and textEntry != placeholderText and textEntry != textTooLongPlaceholder:
        for character in textEntry:
            if character == 'A':
                BlinkDot() 
                time.sleep(pauseMidLetter)
                BlinkDash() 
                time.sleep(pauseAfterLetter)

            elif character == 'B': 
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseAfterLetter)

            elif character == 'C': 
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseAfterLetter)

            elif character == 'D':
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseAfterLetter)

            elif character == 'E':
                BlinkDot()
                time.sleep(pauseAfterLetter)

            elif character == 'F': 
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseAfterLetter)

            elif character == 'G':
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseAfterLetter)

            elif character == 'H': 
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseAfterLetter)

            elif character == 'I':
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseAfterLetter)

            elif character == 'J':
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseAfterLetter)

            elif character == 'K':
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseAfterLetter)

            elif character == 'L':
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseAfterLetter)

            elif character == 'M': 
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseAfterLetter)

            elif character == 'N':
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseAfterLetter)

            elif character == 'O':
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseAfterLetter)

            elif character == 'P':
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseAfterLetter)

            elif character == 'Q': 
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseAfterLetter)

            elif character == 'R':
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseAfterLetter)

            elif character == 'S':
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseAfterLetter)

            elif character == 'T':
                BlinkDash()
                time.sleep(pauseAfterLetter)

            elif character == 'U':
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseAfterLetter)

            elif character == 'V': 
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseAfterLetter)

            elif character == 'W':
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseAfterLetter)

            elif character == 'X': 
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseAfterLetter)

            elif character == 'Y': 
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseAfterLetter)

            elif character == 'Z':
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDash()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseMidLetter)
                BlinkDot()
                time.sleep(pauseAfterLetter)

            elif character.isspace():
                time.sleep(pauseAfterWord)

# blinks a dot
def BlinkDot():
    led.on()
    time.sleep(dot)
    led.off()

# blinks a dash
def BlinkDash():
    led.on()
    time.sleep(dash)
    led.off()

# elegantly closes the program
def close():
    RPi.GPIO.cleanup()
    window.destroy()

# fuction to clear the text entry box when the user clicks in
def clearOnCLick(event):
   event.widget.delete(0, tkinter.END)

### WIDGETS ###

# Button, triggers the connected command when it is pressed
tkinter.Label(window, text="Enter text to convert to Morse").grid(row=0,column=0)
morseButton = Button(window, text="morse it", font=windowFont, command=morseBlink, bg='white', height=1, width=20)
morseButton.grid(row=0,column=2)

entryField = tkinter.Entry(window)
entryField.grid(row=0, column=1)
entryField.insert(10, placeholderText)
entryField.bind("<Button-1>", clearOnCLick)

# used to close the program
exitButton = Button(window, text='Exit', font=windowFont, command=close, bg='red', height=1, width=6)
exitButton.grid(row=3, column=1)

window.protocol("WM_DELETE_WINDOW", close) # cleanup GPIO when user closes window

window.mainloop() # Loops forever






