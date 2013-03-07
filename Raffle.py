#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import random

pname=[]
name=open("name.txt", 'r')
context=name.readline()
while context!='':
	pname.append(context)
	context=name.readline()
name.close
slice = random.sample(pname, 1)
winner=open("winner.txt", 'w')
winner.writelines(slice)
winner.close 
