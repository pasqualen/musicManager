from canzone import Canzone
from canzone import FIELD
from libreria import Libreria

COMMANDS =["a","c","m","t","s","q"]

def stampa_menu():
    print("A - Aggiungi")
    print("C - Cancella")
    print("M - Modifica")
    print("T - Trova")
    print("S - Salva")
    print("Q - Esci")

def stampa_sottomenu():
    print("Cercare per quali delle seguenti categorie?")
    print("1 - Titolo")
    print("2 - Artista")
    print("3 - Genere")
    print("4 - Autore")
    print("5 - Album/Singoli")
    print("6 - Testo")


def get_comand():
        cmd = input(">>> ").lower()
        if cmd in COMMANDS:
            return cmd
        else:
            print("Comando non riconosciuto. Riprova.")

def get_comand2():
    while True:
        cmd2 = input(">>> ")
        if cmd2 in "123456":
            return cmd2
        else:
            print("Comando non riconosciuto. Riprova.")


def getAnno():
    while True:
        anno = input("Anno di pubblicazione: ");
        if (anno.isdigit() and int(anno) > 1900 and int(anno) < 2020) :
            return anno
        else:
            print("Anno non riconosciuto. Riprova.")


def main_loop():
    libreria = Libreria("libreria.txt")
    while True:
        stampa_menu()
        cmd = get_comand()
        print("Hai scelto %s" %cmd)
        if cmd == "q":
            esci = input("Sei sicuro di voler uscire? Premere 1 per uscire, 2 per tornare indietro: ")
            if esci == "1":
                input
                print("Bye bye")
                return
            if esci == "2":
                stampa_menu()
        if cmd == "s":
            libreria.save()
        if cmd == "c":
            c = Canzone()
            nome = input("Titolo: ")
            libreria.delete(nome)
        if cmd == "a":
            titolo = input("Titolo: ")
            artista = input("Artista: ")
            autore = input("Autore: ")
            album = input("Album: ")
            annopubb = getAnno()
            genere = input("Genere: ")
            casadisc = input("Casa Discografica: ")
            testo = input("Testo: ")
            c = Canzone(titolo, artista, autore, album, annopubb, genere, casadisc, testo)
            libreria.add(c)
        if cmd == "t":
            stampa_sottomenu()
            cmd2 = get_comand2()
            print("Hai scelto %s" % cmd2)
            campoDaCercare = "";
            valoreDaCercare = "";

            if cmd2.isdigit() and int(cmd2) >= 1 and int(cmd2) <= 6 :
                campoDaCercare = FIELD(int(cmd2))
                valoreDaCercare = input(campoDaCercare.name + " :");

                trovati = libreria.find(campoDaCercare, valoreDaCercare)

                for c in trovati:
                    str(c)
                    print(c)
            else:
                print("Comando non riconosciuto. Riprova.")
        if cmd == "m":
            c = Canzone()
            titolo = input("Titolo: ")
            artista = input("Inserire nuovo artista: ")
            autore = input("Nuovo Autore: ")
            album = input("Nuovo Album: ")
            annopubb = input("Nuovo anno di pubblicazione: ")
            genere = input("Nuovo genere: ")
            casadisc = input("Nuova casa discografica: ")
            testo = input("Nuovo testo: ")
            libreria.modify(titolo, artista, genere, album, annopubb, genere, casadisc, testo)
            pass


main_loop()