#!/bin/env python

from urllib2 import urlopen
from re import findall
import sys
import html2text.html2text as html2text

path = "docs/"
problem_count = 514

urlbase = 'https://projecteuler.net/problem='

for pnum in range(1,problem_count+1):
	page = urlopen(urlbase+str(pnum)).read()
	r = findall('(<div id="content">[\s\S]*?)<div id="footer"',page)
	md = html2text.html2text(r[0])
	out = open(path+("problem%03d.md" % (pnum,)),"w")
	out.write(md.encode("utf8"))
	out.close()