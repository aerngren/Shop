import csv
import os
import datetime
class Kassa:
    grejjor = []
    def __init__(self) -> None:
        self.idag = datetime.date.today()
        self.nu = datetime.datetime.now()
        self._totalen = 0
        self.räknare = 1


    def handla(self, vara, antal):
        with open('Inventering.csv', 'r', encoding='utf8') as f:
            läsaren = csv.DictReader(f)
            spanaren = list(läsaren)
        
        for sak in spanaren:
            if sak['id'] == vara:
                    Kassa.grejjor.append([sak["namn"], antal,"*",sak["pris"],"=",antal*float(sak["pris"])])
                    self._totalen += antal * float(sak['pris'])

    def kvitto(self):
            with open(f'Kvitto_{self.idag}.txt', 'a', encoding='utf8') as f:
                f.write(f'**{str(self.nu.strftime("%X"))}**Kund nr:{self.räknare}**\n')
                for produkt in Kassa.grejjor:
                    for _ in produkt:
                        f.write(str(_))     
                    f.write('\n')
                f.write(f'-->{self._totalen}kr<--\n{20*"*"}\n') 


    def kund_antal(self):   
        if os.path.exists('Räknare.txt'):
            with open('Räknare.txt', 'r') as f:
                tal = f.read()
                self.räknare = tal        

        else:
            with open('Räknare.txt', 'a', newline='') as f:
                f.write('1')    

    def kund_antal_add(self):
        tal_uppdatera = int(self.räknare)
        tal_uppdatera += 1
        with open('Räknare.txt', 'w') as f:
            f.write(str(tal_uppdatera))

handla = Kassa()
handla2 = Kassa()
handla.handla("111", 3)
handla.handla("222", 5)
handla.kund_antal()
handla.kvitto()
handla.kund_antal_add()
print(handla.räknare)
print(handla._totalen)
for produkt in Kassa.grejjor:
    for _ in produkt:
         print(_, end=" ")
    print()