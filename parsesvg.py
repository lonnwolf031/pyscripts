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
    groups = svgfile.findChildren('g')
    print(groups)



#print(soup)



#soup.findChildren('g')
# makes list

#for link in soup.find_all('a'):
    #print(link.get('href'))
