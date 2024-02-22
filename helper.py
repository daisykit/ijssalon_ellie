def decoreer(tekst=""):
    tekst= "header"
    lengte= len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag,personen):
        bedrag_pp =bedrag/personen
        return f"Het bedrag per persoon is {bedrag_pp} euro"

def onderstreep(tekst=""):
      uit=[]
      uit.append(tekst)
      uit.insert(1,len(tekst)*"=")
      return uit

def som(dictionary):
       values=dictionary.values()
       total=sum(values)
       return (total)
      


