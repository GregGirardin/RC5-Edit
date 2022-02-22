#!/usr/bin/python
'''
python sample parameter tweak utility for RC-5
Greg Girardin
girardin1972@hotmail.com
'''

from __future__ import print_function
import os, sys, json

def nameGen( nameString ):
  print( " XML for " + nameString )
  while len( nameString ) < 12:
    nameString += " "
  nameString = nameString[ 0 : 12 ]

  print( "<NAME>" )
  for i in range( 0, len( nameString ) ):
    numStr = str( i + 1 )
    if( len( numStr ) == 1 ):
      numStr = "0" + numStr
    print( "<C" + numStr + ">" + str( ord( nameString[ i ] ) ) + "</C" + numStr + ">" )
  print( "</NAME>" )

def paramGen( waveLen, bpm ):
  print( "Len:", waveLen )
  print( "BPM:", bpm )
  print()

  nBeats = int( waveLen * bpm / 2646000 )
  nBeats4 = int( nBeats + 3 - nBeats % 4 ) # round up to a factor of 4 (4bpm)
  waveLenAdj = nBeats4 * 2646000 / bpm

  print( "TRACK/MeasLen:", nBeats4 / 4 )
  print( "TRACK/RecTmp:", bpm * 10 ) # xml is tenths of bpm
  print( "TRACK/WavLen:", waveLenAdj )

  print( "MASTER/Tempo:", bpm * 10 )
  print( "MASTER/LpLen:", nBeats4 / 4 )

  print( "RHYTHM/Beat:", 2 ) # 2 means 4/4, always use this for now.

if len( sys.argv ) < 2:
  print( "usage sampleCalc <sampleCount | nameString> <bpm>" )
  exit()

if isinstance( sys.argv[ 1 ], str ):
  nameGen( sys.argv[ 1 ] )
else:
  waveLen = int( sys.argv[ 1 ] )
  if( waveLen < 10000 ) or ( waveLen > 100000000 ):
    print( "Wavelen out of range." )
    exit()

  bpm = 100
  if len( sys.argv ) > 2:
    bpm = int( sys.argv[ 2 ] )
    if( bpm < 30 ) or ( bpm > 300 ):
      print( "BPM out of range." )
      exit()
  
  paramGen( waveLen, bpm )