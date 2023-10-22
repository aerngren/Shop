from kassa import Kassa
from Inventory import Inventering
from rabatt import Rabatt
def menu():
    while True:
        print('KASSA')
        print('1. Ny kund\n2. Administrera\n')
        val= input('0. Avsluta\n>>> ')

        if val == "1":
            while True:
                print('KASSA')
                for produkt in Kassa.grejjor:
                    for _ in produkt:
                        print(_, end=" ")
                    print()    
                print(f'-->{Kassa.totalen}')
                print('kommandon:')
                print('<produktid> <antal>\nPAY')
                
                varor = input('Kommando: ')
                if varor.upper() == "PAY":
                    Kassa.kvitto()
                    Kassa.kund_antal_add()
                    break
                else:
                    produkt, antal = varor.split(' ')
                    Kassa.handla(produkt, antal)
            
        elif val == "2":
            administrera_varor()
        
        elif val =="0":
            break
        
        else:
            print('Ogiltigt val!')
def administrera_varor():
    while True:
        print('Varuhantering')
        print('1. Lägg till vara')
        print('2. Lägg till rabatt')
        print('3. Ta bort rabatt')
        val = input("\n0. Gå tillbaka\n>>> ")
        if val == "1":
            print('Lägg till vara')
            namn = input('Namn på varan: ')
            id = input('ID på varan: ')
            pris = input('Pris på varan: ')
            enhet = input('Kg eller st pris: ')
            grej = Inventering(namn, id, pris, enhet)
            grej.ändra_namn_pris()
        elif val == "2":
            print('Lägg till rabatt')
            id = input('Vilket ID har produkten: ')
            start = input('När ska rabatten starta ÅÅÅÅ-MM-DD: ')
            slut = input('När ska rabatten upphöra ÅÅÅÅ-MM-DD: ')
            pris = float(input('Vad ska priset vara under perioden: '))
            rabatt = Rabatt(id, start, slut, pris)
            rabatt.lägg_till_rabatt()

        elif val =="3":
            Rabatt.lista_rabatt()
            val = int(input('Vilken ska vi ta bort, eller gå tillbaka med 0: '))
            if val == 0:
                return
            else:
                Rabatt.ta_bort_rabatt(val)
                return
        
        elif val == "4":
            id = input('Vilke id har varan: ')
            nytt_namn = input('Vilket är det nya namnet: ')
            nytt_pris = float(input('Vilket är det nya priset: '))
            Inventering.ändra_namn_pris(id, nytt_namn, nytt_pris)



if __name__ == '__main__':
    menu()