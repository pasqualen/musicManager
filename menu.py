from canzone import Canzone
from libreria import Libreria


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
    while True:
        cmd = input(">>> ")
        if cmd in "AaCcMmTtSsQq":
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

def main_loop():
    libreria = Libreria("libreria.txt")
    while True:
        stampa_menu()
        cmd = get_comand()
        print("Hai scelto %s" %cmd)
        if cmd == "Q" or cmd == "q":
            esci = input("Sei sicuro di voler uscire? Premere 1 per uscire, 2 per tornare indietro: ")
            if esci == "1":
                input
                print("Bye bye")
                return
            if esci == "2":
                stampa_menu()
        if cmd == "S" or cmd == "s":
            libreria.save()
        if cmd == "C" or cmd == "c":
            c = Canzone()
            nome = input("Titolo: ")
            libreria.delete(nome)
        if cmd == "A" or cmd == "a":
            titolo = input("Titolo: ")
            artista = input("Artista: ")
            autore = input("Autore: ")
            album = input("Album: ")
            annopubb = input("Anno di pubblicazione: ")
            genere = input("Genere: ")
            casadisc = input("Casa Discografica: ")
            testo = input("Testo: ")
            c = Canzone()
            c.set_titolo(titolo)
            c.set_artista(artista)
            c.set_autore(autore)
            c.set_album(album)
            c.set_annopubb(annopubb)
            c.set_genere(genere)
            c.set_casadisc(casadisc)
            c.set_testo(testo)
            libreria.add(c)
        if cmd == "T" or cmd == "t":
            stampa_sottomenu()
            cmd2 = get_comand2()
            print("Hai scelto %s" % cmd2)
            if cmd2 in "123456":
                if cmd2 == "1":
                    titolo = input("Titolo: ")
                    trovati = libreria.find(titolo)
                    for c in trovati:
                        print(c)
                if cmd2 == "2":
                    artista = input("Artista: ")
                    trovati = libreria.find(artista)
                    for c in trovati:
                        print(c)
                if cmd2 == "3":
                    genere = input("Genere: ")
                    trovati = libreria.find(genere)
                    for c in trovati:
                        print(c)
                if cmd2 == "4":
                    autore = input("Autore: ")
                    trovati = libreria.find(autore)
                    for c in trovati:
                        print(c)
                if cmd2 == "5":
                    album = input("Album o inserire 'na' per cercare i singoli: ")
                    trovati = libreria.find(album)
                    for c in trovati:
                        print(c)
                if cmd2 == "6":
                    testo = input("Testo: ")
                    trovati = libreria.find(testo)
                    for c in trovati:
                        print(c)
                return cmd2
            else:
                print("Comando non riconosciuto. Riprova.")
        if cmd == "M" or cmd == "m":
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