from canzone import Canzone

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
            fields = linea.split(";")
            c = Canzone()
            c.set_artista(fields[1])
            c.set_titolo(fields[0])
            c.set_album(fields[2])
            c.set_annopubb(fields[3])
            c.set_genere(fields[4])
            c.set_autore(fields[5])
            c.set_casadisc(fields[6])
            c.set_testo(fields[7])
            self.__lista.append(c)
        f.close()

    def add(self, c):
        self.__lista.append(c)


    def save(self):
        f = open(self.__filename, "w")
        for c in self.__lista:
            f.write("%s\n" %str(c))
        f.close()

    def find(self, what):
        ret = []
        for c in self.__lista:
            if what in c:
                ret.append(c)
        return ret

    def modify(self, titolo, artista, autore, album, genere, annopubb, casadisc, testo):
        for i in range(len(self.__lista)):
            if self.__lista[i].get_titolo().lower() == titolo.lower():
                self.__lista[i].set_artista(artista)
                self.__lista[i].set_autore(autore)
                self.__lista[i].set_album(album)
                self.__lista[i].set_genere(genere)
                self.__lista[i].set_annopubb(annopubb)
                self.__lista[i].set_casadisc(casadisc)
                self.__lista[i].set_testo(testo)
                return

    def delete(self, what):
        for i in range(len(self.__lista)):
            if self.__lista[i].get_titolo().lower() == what.lower():
                self.__lista.pop(i)
                return