#midi inputter. use with MIDItoLights.py

use_osc "localhost", 4585

live_loop :midi_piano do
  note, velocity = sync "/midi/launchkey_mini/0/1/note_on"
  synth :beep, note: note
  osc "midi", note
end