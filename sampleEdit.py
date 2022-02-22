#!/usr/bin/python
'''
Greg Girardin
Edit the RC-5 XML file
girardin1972@hotmail.com
'''

from __future__ import print_function
import os, sys, json
import xml.etree.ElementTree as ET

tree = ET.parse( './MEMORY1.RC0' )
root = tree.getroot()

print( tree )
 