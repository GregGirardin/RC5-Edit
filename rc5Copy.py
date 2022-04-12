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
      print( "? #" + fileIndex + " " + fileName )

if os.path.isfile( "MEMORY1.RC0" ):
  print( "Copying MEMORY1.RC0" )
  shutil.copy( "MEMORY1.RC0", RC5_DATA_DIR )
  shutil.copy( "MEMORY1.RC0", RC5_DATA_DIR + "MEMORY2.RC0" )

print( "Complete." )