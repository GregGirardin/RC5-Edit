# RC5-Edit

Greg Girardin
Lewiston, Maine
Feb 2022

This is a simple Javascript editor for the RC-5 looper pedal's config.

Roland didn't provide the ability to edit these parameters other than
from the pedal itself which is tedious.

After connecting to the unit, the RC5 config files are located in the Boss/ROLAND/DATA directory named:

MEMORY1.RC0
MEMORY2.RC0

Obviously, back up these files before messing with them.

Use this editor to open one of them, edit the parameters you wish, then save the configs.
I save the config as both "MEMORY1.RC0" and "MEMORY2.RC0" so they are identical.
Then unplug power to the RC-5 and reboot.

The "Async" button available at each memory location will tweak a few parameters for samples
that have no tempo (voice, ambient pads, etc). Otherwise I've found the RC-5 will
have some playback artifacts as though it is time stretching the sample.