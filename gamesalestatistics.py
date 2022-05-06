import csv # imports file type

#creates links to file line placement for easy access
TITLE = 0
PLATFORM = 1
YEAR = 2
GENRE = 3
COMPANY = 4
NA_SALES = 5
EU_SALES = 6
JP_SALES = 7
OTHER_SALES = 8
GLOBAL_SALES = 9

def main():
    data = create_dictionary('vgsales.csv') # access function 
    # create empty lists to store repeatable options
    companies = []
    platforms = []
    years = []
    genres = []
    # create variables for question winners (unnessisary but i wanted to)
    bsgame = '?'
    bsgamesales = 0.0
    bscompany = '?'
    bscompanysales = 0.0
    bsgenre = '?'
    bsgenresales = 0.0
    bsyear = '?'
    bsyearsales = 0.0


    for item in data.items(): # loop through all lines of file
        game = item[1] # set current line to game

        # make sorted lists of avalible platforms, years, genres, and companies
        if game[COMPANY] not in companies: # see if new item
            companies.append(game[COMPANY]) # add item to list
        companies.sort() # sort list

        if game[PLATFORM] not in platforms:
            platforms.append(game[PLATFORM])
        platforms.sort()

        if game[YEAR] not in years:
            years.append(game[YEAR])
        years.sort()

        if game[GENRE] not in genres:
            genres.append(game[GENRE])
        genres.sort()
    

        # find the best selling game
        if float(game[GLOBAL_SALES]) > bsgamesales: # checks to see if current games sales are more that current highest sales
            bsgamesales = float(game[GLOBAL_SALES]) # updates current highest sales to the sales of current game
            bsgame = (f'{game[TITLE]} at {game[GLOBAL_SALES]} million units') # returns current best selling game and sales


    #find best selling company
    for  C in companies: # loop through companies
        companysales = 0.0 # total sales that resets for each company
        for row in data.items(): # loops through data set
                game = row[1] # set current line to game
                if game[COMPANY] == C: # only lets games from current company pass
                    companysales += float(game[GLOBAL_SALES]) # adds up all sales from current company
        if companysales > bscompanysales: # compares current company's total sales to the current best
            bscompanysales = companysales # changes current best to current company
            bscompany = (f'{C} at {bscompanysales:.2f} million units')# returns best company and sales


    #find the best selling game genre
    for  G in genres: # loop through genres
        genresales = 0.0 # total sales that resets for each genre
        for row in data.items(): # loops through data set
                game = row[1] # set current line to game
                if game[GENRE] == G: # only lets games from current genre pass
                    genresales += float(game[GLOBAL_SALES]) # adds up all sales from current genre
        if genresales > bsgenresales: # compares current genre's total sales to the current best
            bsgenresales = genresales # changes current best to current genre
            bsgenre = (f'{G} at {bsgenresales:.2f} million units')# returns best genre and sales


    #find the best selling game genre
    for  Y in years: # loop through genres
        yearsales = 0.0 # total sales that resets for each genre
        for row in data.items(): # loops through data set
                game = row[1] # set current line to game
                if game[YEAR] == Y: # only lets games from current genre pass
                    yearsales += float(game[GLOBAL_SALES]) # adds up all sales from current genre
        if yearsales > bsyearsales: # compares current genre's total sales to the current best
            bsyearsales = yearsales # changes current best to current genre
            bsyear = (f'{Y} at {bsyearsales:.2f} million units')# returns best genre and sales


    # print winners
    print(f'\nBest Selling Game.')
    print(bsgame)
    print(f'\nBest Selling Company.')
    print(bscompany)
    print(f'\nBest Selling Genre.')
    print(bsgenre)
    print(f'\nBest Selling Year.')
    print(bsyear)
    print()


def create_dictionary(csv_file1):
    dictionary = {} # create empty dictionary
    with open(csv_file1, 'rt') as csv_file: # open csv file and give it a desegnation
        reader = csv.reader(csv_file)
        next(csv_file)#skips first line
        for row in reader: # loop through csv file
            dictionary[row[0]] = row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10] # add each item from row of csv file to a new row in the dictionary
    return dictionary # output the newly made dictionary with all the data from the csv file

if __name__ == '__main__':
    main()