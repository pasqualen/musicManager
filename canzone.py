class Canzone:
    __nome: str

    def __init__(self):
        self.titolo = ""
        self.artista = ""
        self.autore = ""
        self.album = ""
        self.annopubb = ""
        self.genere = ""
        self.casadisc = ""
        self.testo = ""

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

    def __contains__(self, what):
        if what.lower() in self.__titolo.lower():
            return True

    def __contains__(self, who):
        if who.lower() in self.__artista.lower():
             return True
        # if what.lower() in self.__autore.lower():
        #     return True
        # if what.lower() in self.__album.lower():
        #     return True
        # if what.lower() in self.__annopubb.lower():
        #     return True
        # if what.lower() in self.__genere.lower():
        #     return True
        # if what.lower() in self.__casadisc.lower():
        #     return True
        # if what.lower() in self.__testo.lower():
        #     return True
