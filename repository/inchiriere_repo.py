class InMemoryRepositoryInchirieri:

    def __init__(self):
        self.__inchirieri = []

    def storeinchiriere(self, inchiriere):
        self.__inchirieri.append(inchiriere)

    def get_all_inchirieri(self):
        return self.__inchirieri

    def find(self, id_client, id_movie):

        for inchiriere in self.__inchirieri:
            if inchiriere.getIdClient() == id_client and inchiriere.getIdMovie() == id_movie:
                return inchiriere
        return None

    def returnare(self, id_client, id_movie):
        inchiriere = self.find(id_client, id_movie)
        if inchiriere is None:
            raise ValueError('Clientul cautat nu a inchiriat acest film')

        self.__inchirieri.remove(inchiriere)
        return inchiriere
