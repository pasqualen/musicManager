from brano import Brano
from libreria import Libreria

COMMANDS =["A","C","M","T","L","Q"]
COMMANDS2 = ["1","2","3","4","5","6"]
ATTRIBUTES = ["Titolo","artista","annopubb","genere","album","casadisc","autori","testo"]

def stampa_menu():
    print("Scegli tra le varie opzioni cosa fare")
    print("   ")
    print("A - Aggiungi brano")
    print("C - Cancella brano")
    print("M - Modifica brano")
    print("T - Trova brano")
    print("L - Lista brani")
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
        cmd = input(">>> ").upper()
        if cmd in COMMANDS:
            return cmd
        else:
            print("Comando non riconosciuto. Riprova.")

def get_comand2():
    while True:
        cmd2 = input(">>> ")
        if cmd2 in COMMANDS2:
            return cmd2
        else:
            print("Comando non riconosciuto. Riprova.")


def getAnno():
    while True:
        anno = input("Anno di pubblicazione: ")
        if (anno.isdigit() and int(anno) > 1900 and int(anno) <= 2020) :
            return anno
        else:
            print("Anno non riconosciuto. Riprova.")

def cerca(libreria):
    stampa_sottomenu()
    cmd2 = get_comand2()
    print("Hai scelto %s" % cmd2)
    brani = []
    if cmd2 == "1":
        titolo = input("Titolo: ").upper()
        brani = libreria.findTitolo(titolo)
    if cmd2 == "2":
        artista = input("Artista: ").upper()
        brani = libreria.findArtista(artista)
    if cmd2 == "3":
        genere = input("Genere: ").upper()
        brani = libreria.findGenere(genere)
    if cmd2 == "4":
        autore = input("Autore: ").upper()
        brani = libreria.findAutore(autore)
    if cmd2 == "5":
        album = input("Album/Singoli: ").upper()
        brani = libreria.findAlbum(album)
    if cmd2 == "6":
        testo = input("Testo: ").upper()
        brani = libreria.findTesto(testo)
    return brani


def stampa(risultati):
    print("{:d} brano/i trovati".format(len(risultati)))
    format_row ="{:^25}" * (len(ATTRIBUTES) + 1)
    print(format_row.format("Numero",*ATTRIBUTES))
    for i in range(len(risultati)):
        print(format_row.format(i+1,*risultati[i].to_array()))



def main_loop():
    libreria = Libreria("libreria.txt")
    while True:
        print("------------------------------")
        print("Benvenuto in Music Project 2.0")
        print("------------------------------")
        stampa_menu()
        cmd = get_comand()
        print("Hai scelto %s" %cmd)
        if cmd == "Q":
            esci = input("Sei sicuro di voler uscire? Premere 1 per uscire, 2 per tornare indietro: ")
            if esci == "1":
                input
                print("Bye bye")
                return
            if esci == "2":
                stampa_menu()
            else:
                print("Comando non riconosciuto.")
        elif cmd == "C":
            risultati = cerca(libreria)
            if len(risultati) > 0:
                stampa(risultati)
                posizione = input("Quale risultato vuoi cancellare? Inserire il numero, 0 per annullare ")
                if posizione != "0" and posizione.isdigit() and int(posizione) > 0 and int(posizione) <= len(risultati):
                    brano_2 = risultati[int(posizione) - 1]
                    conferma = input("Sei sicuro di voler cancellare? Premere 1 per confermare, 2 per annullare: ")
                    if conferma == "1":
                        libreria.delete(brano_2)
                else: print("Operazione annullata")
            else: print("Nessun risultato trovato")
        elif cmd == "A":
            titolo = input("Titolo: ").upper()
            artista = input("Artista: ").upper()
            autori = input("Inserire Autori separati da virgola: ").upper()
            album = input("Album: ").upper()
            annopubb = getAnno()
            genere = input("Genere: ").upper()
            casadisc = input("Casa Discografica: ").upper()
            testo = input("Testo: ").upper()
            c = Brano(titolo, artista, [autore.strip() for autore in autori.split(',')], album, annopubb, genere, casadisc, testo)
            libreria.add(c)
        elif cmd == "T":
            risultati = cerca(libreria)
            if len(risultati) > 0 :
                stampa(risultati)
            else: print("Nessun risultato trovato")
        elif cmd == "M":
            risultati = cerca(libreria)
            if len(risultati) > 0 :
                stampa(risultati)
                posizione = input("Quale risultato vuoi modificare? Inserire il numero, 0 per annullare ")
                if posizione != "0" and posizione.isdigit() and int(posizione) > 0 and int(posizione) <= len(risultati):
                    brano_old = risultati[int(posizione) - 1]
                    print("Premere invio per non modificare il campo")
                    titolo = input("Titolo: ").upper()
                    if (titolo == ""):
                        titolo = brano_old.get_titolo()
                    artista = input("Inserire nuovo artista: ").upper()
                    if (artista == ""):
                        artista = brano_old.get_artista()
                    artista = input("Inserire nuovo artista: ").upper()
                    if (autori == ""):
                        autori = brano_old.get_autori()
                    autori = input("Nuovo Autori: ").upper()
                    if (album == ""):
                        album = brano_old.get_album()
                    album = input("Nuovo Album: ").upper()
                    if (annopubb == ""):
                        annopubb = brano_old.get_annopubb()
                    annopubb = input("Nuovo Anno Pubblicazione: ")
                    annopubb = getAnno()
                    if (genere == ""):
                        genere = brano_old.get_genere()
                    genere = input("Nuovo Genere: ").upper()
                    if (casadisc == ""):
                        casadisc = brano_old.get_casadisc()
                    casadisc = input("Nuova casa discografica: ").upper()
                    if (testo == ""):
                        testo = brano_old.get_testo()
                    testo = input("Nuovo testo: ").upper()
                    brano_new = Brano(titolo, artista, [autore.strip() for autore in autori.split(',')], album, annopubb, genere, casadisc, testo)
                    libreria.update(brano_old, brano_new)
                else: print("Operazione annullata")
            else: print("Nessun risultato trovato")
        elif cmd == "L":
            risultati = libreria.get_lista()
            stampa(risultati)
            print("")
        else:
            print("Comando non riconosciuto. Riprova.")


main_loop()