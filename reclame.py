from algemene_functies import mijn_functie_2


def aanbieding_1(smaak,prijs,korting):
    korting=prijs*(1.00-korting)
    print(f"Vandaag in de aanbieding: emmertje ijs (1 Liter) in de smaak {smaak}, van {prijs} euro voor {korting:.2f} euro")

def inkomsten_totaal(inkomsten,btw):
    totaal=0
    for v in inkomsten:
         totaal+=v
    
    bedrag=totaal*(0.01*btw)
    print(f"Het totaal van alle inkomsten deze week is {totaal:.2f} euro, waarover {bedrag:.2f} euro btw betaald dient te worden" )

def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst),min(mijn_lijst)]

def gemiddelde(mijn_lijst):
    totaal=0
    for i in mijn_lijst:
        totaal+=i
    aantal=len(mijn_lijst)
    gem=totaal/aantal
    print(f"De gemiddelde inkomsten deze week zijn {gem:.2f} euro")

def meervoudig(invoer_lijst):
    global mijn_lijst
    mijn_lijst=invoer_lijst
    antwoord=laag_en_hoog(mijn_lijst)
    return antwoord


def combinatie(invoer_lijst_2):
    korte_lijst=laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0],korte_lijst[1])

