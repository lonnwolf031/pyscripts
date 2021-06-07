#!/usr/bin/env python
# -*-coding: utf-8 -*

from bs4 import BeautifulSoup
soup = BeautifulSoup('<svg></svg>', 'xml')

with open("test.svg", "r") as file:
    # Read each line in the file, readlines() returns a list of lines
    content = file.readlines()
    # Combine the lines in the list into a string
    content = "".join(content)
    # bs_content = bs(content, "lxml")
    soup = BeautifulSoup(content, 'xml')
    svgfile = soup.find('svg')
    # groups = svgfile.findChildren('g')
    singlecard = svgfile.findChildren('g')

    cardname = "test"
    i = 0

    for thing in singlecard:
        card = cardname + str(i)
        new_svg = soup.new_tag("svg")
        new_svg['xmlns'] = "http://www.w3.org/2000/svg"
        thing = thing.insert_before(new_svg)
        i += 1
        print(thing)
