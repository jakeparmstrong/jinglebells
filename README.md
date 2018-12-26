# jinglebells
This project visualizes songs with LEDs using a Raspberry Pi. I wanted to build something fun to show my niece over the winter holidays, so the whole thing has a bit of an xmas theme to it!

Each LED represents a different note in a diatonic scale, with the leftmost LED representing "do", and the rightmost LED representing "ti".

The music is coded in, and played from, an instance of Sonic Pi that is running on my Raspberry Pi 3B+. The code sends OSC messages for every note played. 

A Python script listens for these OSC messages, and lights up a corresponding LED in time with the music.

## Materials

I used:
* Raspberry Pi 3B+
* 9 male-female leads
* 7 220-ohm resistors
* 7 LEDs (4 red and 3 green for the festive colours)

## Circuit Diagram
![jingle bells circuit diagram](https://raw.githubusercontent.com/jakeparmstrong/jinglebells/master/jinglebells_bb.png)

## Procedure

1. Start OSCtoLights.py (I ran it on Python 3.x). This script assigns LEDs to each GPIO pin used, listens on port 3585 for incoming messages, and parses those messages (in a very inelegant manner) to visualize one note at a time on te LED set.
2. Run your Sonic Pi tune on the same Raspberry Pi. Make sure that you set the outbound OSC messages to use the same port (here, 3585).

Note: if you are writing your own sonic pi tunes, make sure to format the OSC messages as  "octave/pitch". See sample code.
