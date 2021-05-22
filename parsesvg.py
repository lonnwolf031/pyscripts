#!/usr/bin/env python
# -*-coding: utf-8 -*

from bs4 import BeautifulSoup
soup = BeautifulSoup('<svg></svg>', 'xml')


with open("kaarten_regrouped.svg", "r") as file:
    # Read each line in the file, readlines() returns a list of lines
    content = file.readlines()
    # Combine the lines in the list into a string
    content = "".join(content)
    #bs_content = bs(content, "lxml")
    soup = BeautifulSoup(content, 'xml')
    svgfile = soup.find('svg')
    #groups = svgfile.findChildren('g')
    singlecard = svgfile.findChildren('g')

    cardname = "card"
    i = 0

    for thing in singlecard:
        card = cardname + str(i)
        new_svg = soup.new_tag("svg")
        new_svg['xmlns'] = "http://www.w3.org/2000/svg"
        thing.insert_before(new_svg)
        i += 1
        with open('%s.svg' % card, 'w') as file:
            file.write(str(thing))
            pass
       # print(thing)
    # make this svg parent tag

    # add attribute   xmlns="http://www.w3.org/2000/svg"
    # each thing.insert_before(new_div)
    #print(groups)



#print(soup)



#soup.findChildren('g')
# makes list

#for link in soup.find_all('a'):
    #print(link.get('href'))
