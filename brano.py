import json

class Brano:

    def __init__(self, t = "" , a = "", au = [], al = "", anno = "", g = "", c = "", testo = ""):
        self.__titolo = t
        self.__artista = a
        self.__autori = au
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

    def set_autori(self, autori):
        self.__autori = autori

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

    def get_autori(self):
        return self.__autori

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
        canzone = {}
        canzone["titolo"] = self.__titolo
        canzone["artista"] = self.__artista
        canzone["annopubb"] = self.__annopubb
        canzone["genere"] = self.__genere
        canzone["album"] = self.__album
        canzone["casadisc"] = self.__casadisc
        canzone["autori"] = self.__autori
        canzone["testo"] = self.__testo
        return json.dumps(canzone)


    def to_array(self):
        return [self.__titolo, self.__artista, self.__annopubb, self.__genere, self.__album, self.__casadisc, ', '.join(self.__autori), self.__testo] #','.join --- Unisci la lista autori usando la virgola tra un elemento e l'altro
