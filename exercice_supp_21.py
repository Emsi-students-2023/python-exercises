import requests
from bs4 import BeautifulSoup

def scrap_it(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', id='table1')
    cells = []
    for tr in table.find_all('tr'):
        cells.append(tr.find_all('td')[1].text)
    cells.pop(0)
    # print(cells)
    lowercells = []
    for l in cells:
        lowercells.append(l.lower())
    return lowercells

# print ('\n',lowercells)
var = input('give us the name :')
# print(var)
def get_it(lowercells):
    x = []
    final = []
    bankai = 0
    out = True
    mew=''
    condition = False
    while bankai != len(var):
        for a in lowercells:
            if a.startswith(var[bankai]):
                x.append(a)
        for e in x:
            if (len(e) > 1 and e in var):
                if condition == True:
                    final.pop(-1)
                final.append(e)
                x.clear()
                exit
            elif len(e) == 1 and e in var:
                final.append(e)
                condition = True
                continue
        condition = False
        bankai += len(final[-1])
    name = final
    if var == name:
        for e in range(len(final)):
            final[e] = final[e].title()
        final= ''.join(final)
        return final
    else:
        return name
url = 'https://www.angelo.edu/faculty/kboudrea/periodic/structure_numbers.htm'
cells = scrap_it(url)
print(get_it(cells))
#lost every existant brain cell in it and yet still buggy
