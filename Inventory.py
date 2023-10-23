import csv

class Inventering:
    def __init__(self, namn, id, pris, enhet) -> None:
        if pris < 0:
            raise ValueError('Vi ger inte bort saker i affären!')
        self._pris = pris
        if not namn:
            raise ValueError('Varan måste ha ett namn')
        self.namn = namn
        if not id:
            raise ValueError('Varan måste ha ett ID')    
        self._id = id
        if not enhet:
            raise ValueError('Varan måste ha en enhet')
        self._enhet = enhet


    def kolla_varan(self):
        with open('Inventering.csv', 'r', encoding='utf8') as f:
            spanaren = list(csv.DictReader(f))
        
        for sak in spanaren:
            if sak['namn'] == self.namn:
                raise ValueError('En vara med det namnet existrar redan!')
            elif sak['id'] == self._id:
                raise ValueError("En vara med det ID't existarar redan!")
        self.lägg_till_vara()

    
    def lägg_till_vara(self):
        with open('Inventering.csv', 'a', encoding='utf8', newline='') as f:
            spara = csv.writer(f)
            spara.writerow([self.namn, self._id, self._pris, self._enhet])
    
    @classmethod
    def ändra_namn_pris(cls, id, nytt_namn, nytt_pris):
        if nytt_pris <= 0:
            raise ValueError('Vi ger inte bort saker!') 
        with open('Inventering.csv', 'r+', encoding='utf8', newline='') as f:
            spanaren = list( csv.DictReader(f))
            hittad = False
            for row in spanaren:
                if row['id'] == id:
                    row['namn'] = nytt_namn
                    row['pris'] = float(nytt_pris)
                    hittad = True
            if not hittad:
                raise ValueError('Varan finns ej')

            f.seek(0)
            skrivaren = csv.DictWriter(f, fieldnames=spanaren[0].keys())
            skrivaren.writeheader()
            skrivaren.writerows(spanaren)
#sak = Inventering("Komb", "222", 20, "kg")
#sak.kolla_varan()
#sak.lägg_till_vara()