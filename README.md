# RC5-Edit

Greg Girardin
Lewiston, Maine
Mar 2022

This is a simple Javascript editor for the Boss RC-5 looper pedal's config.
Boss didn't provide the ability to edit these parameters other than
from the pedal itself which is tedious.

After connecting to the unit, the RC5 config files are located in the Boss/ROLAND/DATA directory named:

MEMORY1.RC0
MEMORY2.RC0

Obviously, back up these files before messing with them.

Use this editor to open one of them, edit the parameters you wish, then save the configs.
I save the config as both "MEMORY1.RC0" and "MEMORY2.RC0" so they are identical.

The "Convert to Async" feature will tweak a few parameters for samples
that have no tempo (voice, ambient pads, etc). Otherwise the RC-5 may
have some playback artifacts it is time stretching the sample to the current tempo.

rc5Copy.py is a python script that will copy audio files from the current directory
to a mounted RC5 unit. See the file for description.
