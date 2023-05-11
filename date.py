date = input('Veuillez inserez une date : ')

moisEnFrancais = {
    "janvier"   : "1", 
    "février"   : "2", 
    "mars"      : "3", 
    "avril"     : "4", 
    "mai"       : "5", 
    "juin"      : "6", 
    "juillet"   : "7", 
    "août"      : "8", 
    "aout"      : "8",
    "septembre" : "9", 
    "octobre"   : "10",
    "novembre"  : "11",
    "décembre"  : "12",
}

lastDayOfMonthTable = {
    "1"   : "31", 
    "2"   : "28", 
    "3"   : "31", 
    "4"   : "30", 
    "5"   : "31", 
    "6"   : "30", 
    "7"   : "31", 
    "8"   : "31", 
    "9"   : "30",
    "10"  : "31", 
    "11"  : "30",
    "12"  : "31",
}

def lastDayOfMonth(number,year):
    if int(number) == 2 and (year%4 == 0) :
        return 29
    return int(lastDayOfMonthTable[number])

def ordinalDate(dateOrdinal=""):
    composan = dateOrdinal.split(" ")
    jours = composan[0]
    mois = moisEnFrancais[composan[1]]
    year = composan[2]
    
    return  {
                "jours" : int(jours) ,
                "mois"  : int(mois)  ,
                "year"  : int(year)
            }
    
    
def incrementDate(date,days):
    
    while days > 0 :
        
        if (date["jours"] + days) <= lastDayOfMonth(str(date["mois"]),int(date["year"])) :
            date["jours"] = date["jours"] + days
            break
        else :
            
            days =  days - lastDayOfMonth(str(date["mois"]),int(date["year"]))
            
            if days <= 0 :
                date["jours"] = date["jours"] + days
                if date["mois"] + 1 == 13 :
                    date["mois"] =  1
                    date["year"] += 1
                else :
                    date["mois"] += 1
                break
            
            if date["mois"] + 1 == 13 :
                date["mois"] =  1
                date["year"] += 1
            else :
                date["mois"] += 1
                
                
    return  date

# affichage de la nouvelle date

dateObject = ordinalDate(date)

print("Votre date",f"{dateObject}")

nombreDeJours = int(input("Donnez le nombre de jours a ajouter dans la date : "))

incrementDate(dateObject, nombreDeJours)

print( dateObject )
