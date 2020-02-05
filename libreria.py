import json
from brano import Brano

class Libreria:
    def __init__(self, filename):
        self.__filename = filename
        self.__lista = []
        try:
            f = open(self.__filename, "r")
        except:
            f = open(self.__filename, "w")
            f.close()
            f = open(self.__filename, "r")
        for linea in f:
            linea = linea.strip('\n')
            jsonMap = json.loads(linea)
            c = Brano()
            c.set_artista(jsonMap["artista"])
            c.set_titolo(jsonMap["titolo"])
            c.set_album(jsonMap["album"])
            c.set_annopubb(jsonMap["annopubb"])
            c.set_genere(jsonMap["genere"])
            c.set_autori(jsonMap["autori"])
            c.set_casadisc(jsonMap["casadisc"])
            c.set_testo(jsonMap["testo"])
            self.__lista.append(c)
        f.close()


    def add(self, c):
        self.__lista.append(c)
        self.__save()

    def update(self, oldBrano, newBrano):
        self.__lista[self.__lista.index(oldBrano)] = newBrano
        self.__save()

    def delete(self, brano):
        self.__lista.remove(brano)
        self.__save()

    def get_lista(self):
        return self.__lista


    def __save(self):
        f = open(self.__filename, "w")
        for c in self.__lista:
            f.write("%s\n" %c.to_json())
        f.close()

    def findTitolo(self, what):
        ret = []
        for c in self.__lista:
            if what in c.get_titolo():
               ret.append(c)
        return ret

    def findArtista(self, what):
        ret = []
        for c in self.__lista:
            if what in c.get_artista():
               ret.append(c)
        return ret

    def findAutore(self, what):
        ret = []
        for c in self.__lista:
            if what in c.get_autori():
               ret.append(c)
        return ret

    def findAlbum(self, what):
        ret = []
        for c in self.__lista:
            if what in c.get_album():
               ret.append(c)
        return ret

    def findAnnopubb(self, what):
        ret = []
        for c in self.__lista:
            if what in c.get_annopubb():
               ret.append(c)
        return ret

    def findGenere(self, what):
        ret = []
        for c in self.__lista:
            if what in c.get_genere():
               ret.append(c)
        return ret

    def findCasadisc(self, what):
        ret = []
        for c in self.__lista:
            if what in c.get_casadisc():
               ret.append(c)
        return ret

    def findTesto(self, what):
        ret = []
        for c in self.__lista:
            if what in c.get_testo():
               ret.append(c)
        return ret


