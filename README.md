# RC5-Edit

Greg Girardin
Lewiston, Maine
Feb 2022

This is a simple Javascript editor for the Boss RC-5 looper pedal's config.
Boss didn't provide the ability to edit these parameters other than
from the pedal itself which is tedious.

After connecting to the unit, the RC5 config files are located in the Boss/ROLAND/DATA directory named:

MEMORY1.RC0
MEMORY2.RC0

Obviously, back up these files before messing with them.

You may need to edit the RC0 files before editing them as the RC5 may generate some
cruft at the end of the XML. Scroll to the very bottom and see if you see something like
"cse>" after the closing "</database>" tag and delete that line. Otherwise the output
of this editor will include a "parse error" tag which will in turn cause the RC-5 not
to read it properly.

Use this editor to open one of them, edit the parameters you wish, then save the configs.
I save the config as both "MEMORY1.RC0" and "MEMORY2.RC0" so they are identical.
Then unplug power to the RC-5 and reboot.

The "Convert to Async" feature will tweak a few parameters for samples
that have no tempo (voice, ambient pads, etc). Otherwise I've found the RC-5 will
have some playback artifacts as though it is time stretching the sample.

The RC-5 will recalculate parameters like "Recorded Tempo" when you connect to
BOSS Tone Studio, so you may have to update the MEMORY1+2.RC0 file since the RC5
often produces bad results.