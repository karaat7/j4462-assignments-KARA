import urllib2, csv
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
#br is basically an open browser window
br.open('http://enrarchives.sos.mo.gov/enrnet/PickaRace.aspx')

# Fill out the top form
br.select_form(nr=0)
br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']
br.submit('ctl00$MainContent$btnElectionType')

# Fill out the bottom form
br.select_form(nr=0)
br.form['ctl00$MainContent$cboRaces'] = ['750003269']
br.submit('ctl00$MainContent$btnCountyChange')

# Get HTML
html = br.response().read()

########## YOUR CODE HERE ##########

#Set up BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
table = soup.find('table', {'id': 'MainContent_dgrdCountyRaceResults'})

list_of_rows = []
for row in table.findAll('tr')[2:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '',)
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("PrimaryResults1.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["County", "Hillary Clinton, DEM", "Henry Hewes, DEM", "Roque Rocky De La Fuente, DEM", "Bernie Sanders, DEM", "Keith Judd, DEM", "Willie L. Wilson, DEM", "Martin J. O Malley, DEM", "John Wolfe, DEM", "Jon Adams, DEM", "Uncommitted, DEM", "Chris Christie, REP", "Jeb Bush, REP", "Ben Carson, REP", "Donald J. Trump, REP", "Marco Rubio, REP", "Ted Cruz, REP", "Rick Santorum, REP", "Carly Fiorina, REP", "John R. Kasich, REP", "Rand Paul, REP", "Jim Lynch, REP", "Mike Huckabee, REP", "Uncommitted, REP", "Austin Petersen, LIB", "Steven Elliott Steve Kerbel, LIB", "Rhett Rosenquest Smith, LIB", "Cecil Ince, LIB", "Marc Allan Feldman, LIB", "Uncommitted, LIB", "Uncommitted, CST"])
writer.writerows(list_of_rows)

