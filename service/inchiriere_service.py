from domain.entities import inchiriere
from repository.inchiriere_repo import InMemoryRepositoryInchirieri
from service.movie_service import InMemoryRepositoryMovies


class InchiriereService:
    def __init__(self, repo_i):

        self.__repo = repo_i

    def returnare(self, id_client, id_movie):

        return self.__repo.returnare(id_client, id_movie)


    def new_inchiriere(self, id_client, id_movie):
        i = inchiriere(id_client, id_movie)
        self.__repo.storeinchiriere(i)

        return i


    def get_all_inchirieri(self):
        return self.__repo.get_all_inchirieri()
