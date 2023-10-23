from datetime import date, datetime
import csv
class Rabatt:
    idag = date.today()
    def __init__(self, id, start_datum, slut_datum, nytt_pris) -> None:
        if datetime.strptime(start_datum, '%Y-%m-%d').date() < self.idag:
            raise ValueError('Det datumet har redan varit!')
        if datetime.strptime(start_datum, '%Y-%m-%d').date() >= datetime.strptime(slut_datum, '%Y-%m-%d').date():
            raise ValueError('Start datumet kan inte vara senare än slut datumet')
        if nytt_pris < 0:
            raise ValueError('Vi ger inte bort varor!')
        self._id = id
        self.kolla_vara(id)
        self.start_datum = start_datum
        self.slut_datum = slut_datum
        self.nytt_pris = nytt_pris
        
        

    def kolla_vara(self, id):
        with open('Inventering.csv', 'r', encoding='utf8') as f:
            läsaren = csv.DictReader(f)
            spanaren = list(läsaren)
        for sak in spanaren:
            if sak['id'] == id:
                break
        else:
            raise ValueError('Varan finns inte')

    def lägg_till_rabatt(self):
        with open('Rabatter.csv', 'a', encoding='utf8', newline='') as f:
            spara = csv.writer(f)
            spara.writerow([self._id,self.start_datum, self.slut_datum, self.nytt_pris])    
    
    @classmethod
    def lägg_på_rabatt(cls, id):
        with open('Rabatter.csv', 'r') as f:
            läsaren = csv.DictReader(f)
            spanaren = list(läsaren)
        for sak in spanaren:
            if sak['id'] == id and date.fromisoformat(sak['slut']) >= cls.idag >= date.fromisoformat(sak['start']):
                return float(sak['pris'])
        return None

    @classmethod
    def lista_rabatt(cls):
        with open('Rabatter.csv', 'r') as f:
            spanaren = list(csv.DictReader(f))
        for _, rad in enumerate(spanaren, 1):
            ny_rad = ', '.join(f'{key}: {value}' for key, value in rad.items())
            print(_, ny_rad)

    @classmethod
    def ta_bort_rabatt(cls, index_bort):
        with open('Rabatter.csv', 'r', newline='') as f:
            spanaren = list(csv.DictReader(f))
        sann_index = index_bort - 1
        if 0 <= sann_index < len(spanaren):
            fieldnames = spanaren[0].keys()
            del spanaren[sann_index]
            with open('Rabatter.csv', 'w', newline='') as f:
                skrivaren = csv.DictWriter(f, fieldnames=fieldnames)
                skrivaren.writeheader()
                skrivaren.writerows(spanaren)
        else:
            return


#vara = Rabatt('222', '2023-10-23', '2023-12-28', 5)

#vara.lägg_till_rabatt()
