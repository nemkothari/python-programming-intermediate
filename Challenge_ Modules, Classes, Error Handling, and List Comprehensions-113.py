## 2. Introduction to the Data ##

import csv
f= open("nfl_suspensions_data.csv","r")
nfl_suspensions = list(csv.reader(f))
nfl_suspensions=nfl_suspensions[1:]

years={}
for i in nfl_suspensions:
    if i[5] in years:
        years[i[5]] =years[i[5]]+1
    else:
        years[i[5]]=1
        
print(years)



## 3. Unique Values ##

import csv
f= open("nfl_suspensions_data.csv","r")
nfl_suspensions = list(csv.reader(f))
nfl_suspensions=nfl_suspensions[1:]

unique_teams =set([x[1] for x in nfl_suspensions])

unique_games =set([x[2] for x in nfl_suspensions])

print(unique_teams)
print(unique_games)



    

## 4. Suspension Class ##

class Suspension():
    def __init__(self,r):
        self.name = r[0]
        self.team = r[1]
        self.games = r[2] 
        self.year = r[5]
third_suspension = Suspension(nfl_suspensions[2])
        

## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
    
        try:
            self.year=int(row[5])
        except Exception as ex:
            self.year=0
            
    def get_year(self):
        return(self.year)

missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()