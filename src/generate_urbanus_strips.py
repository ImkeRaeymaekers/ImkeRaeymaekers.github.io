#! /usr/bin/env python3

import time

from bs4 import BeautifulSoup

header = """title: Urbanus Strips
slug: urbanus_strips
category: strips
tags: urbanus, strips
date: 2019-01-30
modified: %04d-%02d-%02d

# Urbanus Strips

""" % (time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday)

print(header)

heb_ik_al = [1 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10
    , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20
    , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30
    , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40
    , 41 , 42 , 43 , 44 , 45 , 47 , 48 , 49 , 50
    , 51 , 52 , 53 , 54 , 55 , 56 , 57 , 58 , 59 , 60
    , 61 , 62 , 63 , 64
    , 73
    , 104
    , 111
    , 146 , 150
    , 159
    , 161 , 162 , 163 , 164 , 165 , 166 , 167
    , 172 , 173 , 174 , 175 , 176 , 177 , 178
    , 181]

soup = BeautifulSoup(open("tmp/Lijst_van_albums_van_Urbanus", 'r'), features="html.parser")
albums = {}
nr = 0
for li in soup.body.ol:
    if li.name == "li":
        albums[nr] = li.a.text
        nr+=1
        if nr in heb_ik_al:
            print("* %3d _%s_" % (nr, li.a.text))

