#!/usr/bin/python
'''
python sample copier for BOSS RC-5 looper
Greg Girardin
girardin1972@hotmail.com

In the local directory there should be a waves.txt and a collection of wav files.
Each line of waves.txt (up to line 98) should be the name of a .wav file in the local directory

line 0: myWave1.wav
line 1: myWave2.wav
.
.
line 98: myWave99.wav

For example, you could create waves.txt from the shell

  shell% ls *.wav >waves.txt

Then rearrage as desired.

RC5_WAVDIR is the base directory of the RC5's waves. ex: "/Volumes/BOSS RC-5/ROLAND/WAVE"
You'll have to attach the RC5 to the RC5 editor obviously.

) open waves.txt
) optionally, save the RCV_WAVDIR/00N_1 contents to a local directory 
) optionally, clear the RCV_WAVDIR/00N_1 directories 
) copy the local wav files named in line N to the RCV_WAVDIR/00N_1 directory
'''

from __future__ import print_function
import os, shutil, glob, copy, sys

RC5_WAV_DIR = "/Volumes/BOSS\ RC-5/ROLAND/WAV"
WAVE_FILE = "waves.txt"

def getInput():
  # Copied from http://stackoverflow.com/questions/983354/how-do-i-make-python-to-wait-for-a-pressed-key
  import termios, fcntl, sys, os
  fd = sys.stdin.fileno()
  flags_save = fcntl.fcntl( fd, fcntl.F_GETFL )
  attrs_save = termios.tcgetattr( fd )
  attrs = list( attrs_save )
  attrs[ 0 ] &= ~( termios.IGNBRK | termios.BRKINT | termios.PARMRK | termios.ISTRIP |
                   termios.INLCR  | termios.IGNCR  | termios.ICRNL  | termios.IXON )
  attrs[ 1 ] &= ~termios.OPOST
  attrs[ 2 ] &= ~( termios.CSIZE | termios.PARENB )
  attrs[ 2 ] |= termios.CS8
  attrs[ 3 ] &= ~( termios.ECHONL | termios.ECHO | termios.ICANON | termios.ISIG | termios.IEXTEN )
  termios.tcsetattr( fd, termios.TCSANOW, attrs )
  fcntl.fcntl( fd, fcntl.F_SETFL, flags_save & ~os.O_NONBLOCK )
  try:
    ret = sys.stdin.read( 1 )
    if ord( ret ) == 27: # Escape
      ret = sys.stdin.read( 1 )
      ret = sys.stdin.read( 1 )
      if ret == 'A':
        ret = 'UP'
      elif ret == 'B':
        ret = 'DOWN'
      elif ret == 'C':
        ret = 'RIGHT'
      elif ret == 'D':
        ret = 'LEFT'
      else:
        print( int( ret ) )
        exit()

  except KeyboardInterrupt:
    ret = 0
  finally:
    termios.tcsetattr( fd, termios.TCSAFLUSH, attrs_save )
    fcntl.fcntl( fd, fcntl.F_SETFL, flags_save )
  return ret

# Open waves.txt
if not os.path.exists( WAVE_FILE ):
  print( WAVE_FILE, "does not exist." )
  exit()

if not os.path.exists( RC5_WAV_DIR ):
  print( "Path to RC5 does not exist." )
  exit()

print( "Backup files from RC-5 locally?" )
ch = getInput()
if( ch == 'y' or ch == "Y" ):
  print( "TBD: Backing up..." )
  exit()
  # make backupdir
  # Copy all waves locally and create a waves.txt

  # Save waves.txt

# clear directory
print( "Deleting wav files." )

for fileIndex in range( 1, 99 ):
  dirName = RC5_WAV_DIR
  dirName += "00" if( fileIndex < 10 ) else "0"
  dirName += str( fileIndex ) + "_1";

  for filename in os.listdir( dirName ):
    file_path = os.path.join( dirName, filename )
    try:
      if os.path.isfile( file_path ):
        # os.unlink( file_path )
        print( "Deleting:" + file_path );
      else:
        print( "Unexpected:" + file_path )
    except Exception as e:
      print( 'Failed to delete %s. Reason: %s' % ( file_path, e ) )

sf = open( WAVE_FILE, "r" )
fLines = sf.readlines()
sf.close()

fileIndex = 0

for line in fLines:
  print( line )
  fileIndex += 1
  if os.path.isfile( line ):
    print( "Copying:" + line )
  else:
    print( "File not found:" + line );

 print( "Complete." )

  # destDir = RC5_WAV_DIR + 
