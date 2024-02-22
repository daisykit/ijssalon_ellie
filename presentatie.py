from helper import*

def presenteer(dictionary,totaal):
      lijn=26*"="
      for k,v in dictionary.items():
        print(f"{k} : {v} euros")
      return(f'''{lijn} 
totaal : {totaal} euro''')

