#!/bin/env python
# -*- coding: utf-8 -*-
from urllib2 import urlopen
from re import findall
import sys
from html2text import html2text

path = "docs/"
problem_count = 514

urlbase = 'https://projecteuler.net/problem='

for pnum in range(1,problem_count+1):
	page = urlopen(urlbase+str(pnum)).read()
	r = findall('(<div id="content">[\s\S]*?)<div id="footer"',page)
	unctxt=unicode(r[0],"utf8")
	md = html2text(unctxt)
	out = open(path+("problem%03d.md" % (pnum,)),"w")
	out.write(md.encode("utf8"))
	out.close()
