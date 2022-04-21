#!/usr/bin/python
'''
python sample copier for BOSS RC-5 looper
Greg Girardin
girardin1972@hotmail.com

In the local directory create a file called waves.txt with the names of the .wav files to be copied.
Each line of waves.txt (up to line 99) should be the name of a .wav file in the local directory.

line 1: myWave1.wav
line 2: myWave2.wav
.
.
line 99: myWave99.wav

For example, you could create waves.txt from the shell as follows

  shell% ls *.wav >waves.txt

Then edit waves.txt to rearrage the lines as desired.

Attach the RC5 to the RC5 editor so its direcotry is mounted.

Then execute this script.

RC5_WAVDIR is the base directory of the RC5's waves. ex: "/Volumes/BOSS RC-5/ROLAND/WAVE"
'''

from __future__ import print_function
import os, shutil, glob, copy, sys

RC5_WAV_DIR = "/Volumes/BOSS RC-5/ROLAND/WAVE/"
RC5_DATA_DIR = "/Volumes/BOSS RC-5/ROLAND/DATA/"
WAVE_FILE = "waves.txt"

# Open waves.txt
if not os.path.exists( WAVE_FILE ):
  print( WAVE_FILE, "does not exist." )
  exit()

if not os.path.exists( RC5_WAV_DIR ):
  print( "Path to RC5 does not exist." )
  exit()

# clear directory
print( "Deleting wav files." )

for fileIndex in range( 1, 100 ):
  dirName = RC5_WAV_DIR + ( "00" if( fileIndex < 10 ) else "0" ) + str( fileIndex ) + "_1";

  for filename in os.listdir( dirName ):
    file_path = os.path.join( dirName, filename )
    try:
      if os.path.isfile( file_path ):
        os.unlink( file_path )
        print( "Deleting:" + file_path )
      else:
        print( "Unexpected:" + file_path )
    except Exception as e:
      print( 'Failed to delete %s. Reason: %s' % ( file_path, e ) )

sf = open( WAVE_FILE, "r" )
fLines = sf.readlines()
sf.close()

fileIndex = 0

for line in fLines:
  fileIndex += 1
  if( fileIndex > 99 ):
    print( "Max lines exceeded." )
    break
  fileName = line[ 0 : -1 ]
  if len( fileName ) > 4: # Skip blank lines. Shortest is "X.wav"
    if os.path.isfile( fileName ):
      print( "Copying:" + fileName )
      dirName = RC5_WAV_DIR + ( "00" if( fileIndex < 10 ) else "0" ) + str( fileIndex ) + "_1";
      shutil.copy( fileName, dirName )
    else:
      print( "? #" + str( fileIndex ) + " " + fileName )
      print( "Failed." )
      exit( 0 )

if os.path.isfile( "MEMORY1.RC0" ):
  print( "Copying MEMORY1.RC0" )
  shutil.copy( "MEMORY1.RC0", RC5_DATA_DIR )
  shutil.copy( "MEMORY1.RC0", RC5_DATA_DIR + "MEMORY2.RC0" )

print( "Complete." )
