from rabatt import Rabatt
import os
import datetime
import csv
class Kassa:
    räknare = 1
    def __init__(self) -> None:
            self.grejjor = []
            self.totalen = 0
            self.idag = datetime.date.today()
            self.nu = datetime.datetime.now()


    def handla(self, produkt, antal):
        with open('Inventering.csv', 'r', encoding='utf8') as f:
            läsaren = csv.DictReader(f)
            spanaren = list(läsaren)
        
        for sak in spanaren:
            if sak['id'] == produkt:
                sak['pris'] = float(sak['pris'])
                if sak['enhet'] == 'kg':
                    antal = float(antal)
                else:
                    antal = int(antal)
                rabatt = Rabatt.lägg_på_rabatt(produkt)
                if rabatt is not None:
                    self.grejjor.append([f'{sak["namn"]} {antal} * {rabatt} = {round(antal * rabatt, 2)}'])
                    self.totalen += round(antal * rabatt, 2)
                    
                else:        
                    self.grejjor.append([f'{sak["namn"]} {antal} * {sak["pris"]} = {round(antal * sak["pris"], 2)}'])
                    self.totalen += round(antal * sak['pris'], 2)
            


    def kvitto(self):
        self.kund_antal()
        with open(f'Kvitto_{self.idag}.txt', 'a', encoding='utf8') as f:
            f.write(f'**{str(self.idag)} {str(self.nu.strftime("%X"))}**Kund nr:{self.räknare}**\n')
            for produkt in self.grejjor:
                for _ in produkt:
                    f.write(str(_))     
                f.write('\n')
            f.write(f'-->{self.totalen}kr<--\n{30*"*"}\n') 
        

    @classmethod
    def kund_antal(cls):   
        if os.path.exists('Räknare.txt'):
            with open('Räknare.txt', 'r') as f:
                tal = f.read()
                cls.räknare = tal        

        else:
            with open('Räknare.txt', 'a', newline='') as f:
                f.write('1')    
    @classmethod
    def kund_antal_add(cls):
        tal_uppdatera = int(cls.räknare)
        tal_uppdatera += 1
        with open('Räknare.txt', 'w') as f:
            f.write(str(tal_uppdatera))


#handla = Kassa()
#handla2 = Kassa()
#handla.handla("111", 3)
#handla.handla("222", 5)
#handla.kund_antal()
#print(handla.räknare)
#print(handla._totalen)
#for produkt in Kassa.grejjor:
#    for _ in produkt:
#         print(_, end=" ")
#    print()