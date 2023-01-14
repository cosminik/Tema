from domain.entities import Client
from domain.validators import ClientValidator
from repository.client_repo import InMemoryRepositoryClients
import random
import string


class ClientService:
    def __init__(self, repo_c, val_c):
        """
        Initializeaza service
        :param repo_c: obiect de tip repo care ne ajuta sa gestionam multimea de clienti
        :type repo_c: InMemoryRepositoryClients
        :param val_c: validator pentru verificarea clientilor
        :type val_c: ClientValidator
        """
        self.__repo = repo_c
        self.__validator = val_c

    def get_random_string(self, length):
        result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
        return result_str

    def get_random_client(self, id, nume, CNP, email):

        c = Client(id, nume, CNP, email,0)
        self.__repo.store(c)
        return c

    def add_client(self, id, nume, CNP, email):
        """
        Adauga client
        :param id: id-ul clientului
        :typw id: int
        :param nume: numele clientului
        :type nume: str
        :param CNP: CNP-ul clientului
        :type CNP: int
        :param email: Email-ul clietului
        :type email: str
        :return: obiectul de tip Client creat
        :rtype:-; clientul s-a adaugat in lista
        :raises: ValueError daca clientul are date invalide
        """
        c = Client(id, nume, CNP, email,0)

        self.__validator.validatec(c)
        self.__repo.store(c)
        return c


    def get_all_clients(self):
        """
        Returneaza o lista cu toti clientii disponibili
        :return: lista de clienti disponibili
        :rtype: list of objects de tip Client
        """
        return self.__repo.get_all_clients()


    def delete_client(self, id):
        """
        Sterge filmul cu id dat din lista
        :param id: id-ul dat
        :type id: str
        :return: filmul sters
        :rtype: Movie
        :raises: ValueError daca nu exista film cu id-ul dat
        """
        return self.__repo.delete_by_id(id)

    def update_client(self, id, nume, CNP, email):
        """
        Modifica datele clientului cu id dat
        :param id: id-ul clientului de modificat
        :type id: str
        :param nume: noul nume al clientului
        :type nume: str
        :param CNP: noul CNP al serialului
        :type CNP: int
        :param email: noul email serial
        :type email: str
        :return: clientul modificat
        :rtype:Client
        :raises: ValueError daca noile date nu sunt valide, sau nu exista client cu id dat
        """
        c = Client(id, nume, CNP, email,0)

        self.__validator.validatec(c)
        return self.__repo.update(id, c)


    def search_client(self, id):
        """
        Cauta clientul cu id dat din lista
        :param id: id-ul dat
        :type id: str
        :return: clientul cautat
        :rtype: Clientul
        :raises: ValueError daca nu exista client cu id-ul dat
        """
        return self.__repo.search_by_id(id)


def test_add_client():
    repo = InMemoryRepositoryClients()
    validator = ClientValidator()
    test_srv = ClientService(repo, validator)

    added_client = test_srv.add_client(1, 'Primul Client', 6030405271567, 'email1@yahoo.com')
    assert (added_client.getIdClient() == 1)
    assert (added_client.getNume() == 'Primul Client')
    assert (added_client.getCNP() == 6030405271567)
    assert (added_client.getEmail() == 'email1@yahoo.com')

    assert (len(test_srv.get_all_clients()) == 1)

    try:
        added_show = test_srv.add_client(2, 'Primul Client', 603040527156, 'email1@yahoo.com')
        assert False
    except ValueError:
        assert True

test_add_client()