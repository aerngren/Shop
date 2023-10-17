import csv

class Inventering:
    def __init__(self, namn, id, pris, enhet) -> None:
        if pris < 0:
            raise ValueError('Vi ger inte bort saker i affären!')
        self.namn = namn
        self._id = id
        self._pris = pris
        self._enhet = enhet


    def kolla_varan(self):
        with open('Inventering.csv', 'r', encoding='utf8') as f:
            läsaren = csv.DictReader(f)
            spanaren = list(läsaren)
        
        for sak in spanaren:
            if sak['namn'] == self.namn:
                raise ValueError('En vara med det namnet existrar redan!')
            elif sak['id'] == self._id:
                raise ValueError("En vara med det ID't existarar redan!")

    def lägg_till_vara(self):
        with open('Inventering.csv', 'a', encoding='utf8', newline='') as f:
            spara = csv.writer(f)
            spara.writerow([self.namn, self._id, self._pris, self._enhet])



sak = Inventering("Komb", "222", 20, "kg")
sak.kolla_varan()
sak.lägg_till_vara()