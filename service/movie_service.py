from domain.entities import Movie
from domain.validators import MovieValidator
from repository.movie_repo import InMemoryRepositoryMovies
import random
import string


class MovieService:
    def __init__(self, repo, validator):
        """
        Initializeaza service
        :param repo: obiect de tip repo care ne ajuta sa gestionam multimea de filme
        :type repo: InMemoryRepositoryMovies
        :param validator: validator pentru verificarea filmelor
        :type validator: ShowValidator
        """
        self.__repo = repo
        self.__validator = validator

    def add_movie(self, id, titlu, descriere, gen):
        """
        Adauga serial
        :param id: id-ul filmului
        :type id: int
        :param titlu: titlul filmului
        :type titlu: str
        :param descriere: descrierea filmului
        :type descriere: str
        :param gen: genul filmului
        :type gen: str
        :return: obiectul de tip Movie creat
        :rtype:-; filmul s-a adaugat in lista
        :raises: ValueError daca filmul are date invalide
        """
        m = Movie(id, titlu, descriere, gen,0)

        self.__validator.validate(m)
        self.__repo.store(m)
        return m


    def get_random_string(self, length):
        result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
        return result_str

    def get_random_movie(self, id, titlu, descriere, gen):

        m = Movie(id, titlu, descriere, gen,0)
        self.__repo.store(m)
        return m

    def get_all_movies(self):
        """
        Returneaza o lista cu toate filmele disponibile
        :return: lista de filme disponibile
        :rtype: list of objects de tip Movie
        """
        return self.__repo.get_all_movies()

    def delete_movie(self, id):
        """
        Sterge filmul cu id dat din lista
        :param id: id-ul dat
        :type id: int
        :return: filmul sters
        :rtype: Movie
        :raises: ValueError daca nu exista film cu id-ul dat
        """
        return self.__repo.delete_by_id(id)


    def update_movie(self, id, titlu, descriere, gen,numar_inchirieri):
        """
        Modifica datele serialului cu id dat
        :param id: id-ul serialului de modificat
        :type id: str
        :param titlu: noul titlu al serialului
        :type titlu: str
        :param an_aparitie: noul an de aparitie al serialului
        :type an_aparitie: int
        :param eps: noul numar de episoade pentru serial
        :type eps: int
        :return: serialul modificat
        :rtype:Serial
        :raises: ValueError daca noile date nu sunt valide, sau nu exista serial cu id dat
        """
        m = Movie(id, titlu, descriere, gen,numar_inchirieri)

        self.__validator.validate(m)
        return self.__repo.update(id, m)


    def search_movie(self, id):
        """
        Cauta filmul cu id dat din lista
        :param id: id-ul dat
        :type id: int
        :return: filmul cautat
        :rtype: Movie
        :raises: ValueError daca nu exista film cu id-ul dat
        """
        return self.__repo.search_by_id(id)
    def increasenumarinchirieri(self,id):
        self.__repo.increasebyid(id)
def test_add_movie():
    repo = InMemoryRepositoryMovies()
    validator = MovieValidator()
    test_srv = MovieService(repo, validator)

    added_movie = test_srv.add_movie(1, 'The Notebook', 'un prim film frumos', 'romance')
    assert (added_movie.getId() == 1)
    assert (added_movie.getTitlu() == 'The Notebook')
    assert (added_movie.getGen() == 'romance')

    assert (len(test_srv.get_all_movies()) == 1)

    try:
        added_movie = test_srv.add_movie(2, 'T', 'un prim film frumos', 'romance')
        assert False
    except ValueError:
        assert True

test_add_movie()