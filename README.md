# jinglebells
This project visualizes songs with LEDs using a Raspberry Pi. I wanted to build something fun to show my niece over the winter holidays, so the whole thing has a bit of an xmas theme to it!

Each LED represents a different note in a diatonic scale, with the leftmost LED representing "do", and the rightmost LED representing "ti".

The music is coded in, and played from, an instance of Sonic Pi that is running on my Raspberry Pi 3B+. The code sends OSC messages for every note played. 

A Python script listens for these OSC messages, and lights up a corresponding LED in time with the music.
