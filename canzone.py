import enum
import json

class FIELD(enum.Enum):
    TITOLO = 1
    ARTISTA = 2
    GENERE = 3
    AUTORE = 4
    ALBUM = 5
    TESTO = 6

class Canzone:

    def __init__(self, t="" , a="", au="", al="", anno="", g="", c="", testo=""):
        self.__titolo = t
        self.__artista = a
        self.__autore = au
        self.__album = al
        self.__annopubb = anno
        self.__genere = g
        self.__casadisc = c
        self.__testo = testo
    #SET
    def set_titolo(self, titolo):
        self.__titolo = titolo

    def set_artista(self, artista):
        self.__artista = artista

    def set_autore(self, autore):
        self.__autore = autore

    def set_album(self, album):
        self.__album = album

    def set_annopubb(self, annopubb):
        self.__annopubb = annopubb

    def set_genere(self, genere):
        self.__genere = genere

    def set_casadisc(self, casadisc):
        self.__casadisc = casadisc

    def set_testo(self, testo):
        self.__testo = testo


    #GET

    def get_titolo(self):
        return self.__titolo

    def get_artista(self):
        return self.__artista

    def get_autore(self):
        return self.__autore

    def get_album(self):
        return self.__album

    def get_annopubb(self):
        return self.__annopubb

    def get_genere(self):
        return self.__genere

    def get_casadisc(self):
        return self.__casadisc

    def get_testo(self):
        return self.__testo

    def to_json(self):
        canzone = {};
        canzone["titolo"] = self.__titolo;
        canzone["artista"] = self.__artista;
        canzone["annopubb"] = self.__annopubb;
        canzone["genere"] = self.__genere;
        canzone["album"] = self.__album;
        canzone["casadisc"] = self.__casadisc;
        canzone["autore"] = self.__autore;
        canzone["testo"] = self.__testo;
        return json.dumps(canzone)

    def __str__(self):
        return "%s; %s; %s; %s; %s; %s; %s; %s" %(self.__titolo, self.__artista, self.__annopubb, self.__genere, self.__album, self.__casadisc, self.__autore, self.__testo)

    def __gt__(self, other):
        if self.__titolo.lower > other.__titolo.lower:
            return True
        if self.__autore.lower > other.__autore.lower:
            return True
        if self.__artista.lower > other.__artista.lower:
            return True
        if self.__annopubb.lower > other.__annopubb.lower:
            return True
        if self.__album.lower > other.__album.lower:
            return True
        if self.__genere.lower > other.__genere.lower:
            return True
        if self.__casadisc.lower > other.__casadisc.lower:
            return True
        if self.__testo.lower > other.__testo.lower:
            return True
        return False

    def __lt__(self, other):
        if self.__autore.lower < other.__autore.lower:
            return True
        if self.__artista.lower < other.__artista.lower:
            return True
        if self.__annopubb.lower < other.__annopubb.lower:
            return True
        if self.__album.lower < other.__album.lower:
            return True
        if self.__genere.lower < other.__genere.lower:
            return True
        if self.__casadisc.lower < other.__casadisc.lower:
            return True
        if self.__testo.lower < other.__testo.lower:
            return True
        return False
