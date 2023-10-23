from rabatt import Rabatt
import os
import datetime
import csv
class Kassa:
    grejjor = []
    totalen = 0
    idag = datetime.date.today()
    nu = datetime.datetime.now()
    räknare = 1

    @classmethod
    def handla(cls, produkt, antal):
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
                    Kassa.grejjor.append([sak["namn"], antal, "*", rabatt, "=", antal * rabatt])
                    cls.totalen += antal * rabatt
                    
                else:        
                    Kassa.grejjor.append([sak["namn"], antal,"*",sak["pris"],"=",antal*sak["pris"]])
                    cls.totalen += antal * sak['pris']
            

    @classmethod
    def kvitto(cls):
            cls.kund_antal()
            with open(f'Kvitto_{cls.idag}.txt', 'a', encoding='utf8') as f:
                f.write(f'**{str(cls.idag)} {str(cls.nu.strftime("%X"))}**Kund nr:{cls.räknare}**\n')
                for produkt in Kassa.grejjor:
                    for _ in produkt:
                        f.write(str(_))     
                    f.write('\n')
                f.write(f'-->{cls.totalen}kr<--\n{20*"*"}\n') 
            cls.grejjor.clear()
            cls.totalen = 0

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