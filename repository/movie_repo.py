class InMemoryRepositoryMovies:
    """
        Clasa creata cu responsabilitatea de a gestiona
        multimea de filme (i.e. sa ofere un depozit persistent pentru obiecte
        de tip Movie)
    """
    def __init__(self):
        self.__movies = []

    def store(self, movie):
        """
        Adauga un film in lista
        :param movie: filmul care se adauga
        :type movie: Movie
        :return: -; lista de filme se modifica prin adaugarea filmului dat
        :rtype:
        """
        self.__movies.append(movie)

    def get_all_movies(self):
        """
        Returneaza o lista cu toate filmele existente
        :rtype: list of objects de tip Movie
        """
        return self.__movies


    def find(self, id):
        """
        Cauta filmul cu id dat
        :param id: id dat
        :type id: str
        :return: filmul cu id dat, None daca nu exista
        :rtype: Movie
        """
        for movie in self.__movies:
            if movie.getId() == id:
                return movie
        return None


    def delete_by_id(self, id):
        """
        Sterge film dupa id
        :param id: id-ul dat
        :type id: str
        :return: filmul sters
        :rtype: Movie
        :raises: ValueError daca id-ul nu exista
        """
        movie = self.find(id)
        if movie is None:
            raise ValueError('Nu exista film cu acest id.')

        self.__movies.remove(movie)
        return movie
    def increasebyid(self,id):
        for movie in self.__movies:
            if movie.getId()==id:
                movie.increasenumarinchirieri()
    def update(self, id, modified_movie):
        """
        Modifica datele filmului cu id dat
        :param id: id dat
        :type id: str
        :param modified_movie: filmul cu datele noi
        :type modified_movie: Movie
        :return: filmul modificat
        :rtype: Movie
        """

        movie = self.find(id)
        if movie is None:
            raise ValueError('Nu exista film cu acest id.')

        movie.setTitlu(modified_movie.getTitlu())
        movie.setDescriere(modified_movie.getDescriere())
        movie.setGen(modified_movie.getGen())
        movie.setNumarinchirieri(0)
        return movie


    def search_by_id(self, id):
        """
        Cauta film dupa id
        :param id: id-ul dat
        :type id: str
        :return: filmul cautat
        :rtype: Movie
        :raises: ValueError daca id-ul nu exista
        """
        movie = self.find(id)
        if movie is None:
            raise ValueError('Nu exista film cu acest id.')

        return movie



def test_store():
    pass


def test_get_all_movies():
    pass