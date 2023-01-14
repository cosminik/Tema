class InMemoryRepositoryClients:
    """
        Clasa creata cu responsabilitatea de a gestiona
        multimea de clienti (i.e. sa ofere un depozit persistent pentru obiecte
        de tip Client)
    """
    def __init__(self):
        self.__clients = []

    def store(self, client):
        """
        Adauga un client in lista
        :param client: clientul care se adauga
        :type client: Client
        :return: -; lista de clienti se modifica prin adaugarea clientului dat
        :rtype:
        """
        self.__clients.append(client)

    def get_all_clients(self):
        """
        Returneaza o lista cu toti clientii existenti
        :rtype: list of objects de tip Client
        """
        return self.__clients

    def find(self, id):
        """
        Cauta clientul cu id dat
        :param id: id dat
        :type id: str
        :return: clientul cu id dat, None daca nu exista
        :rtype: Client
        """
        for client in self.__clients:
            if client.getIdClient() == id:
                return client
        return None

    def delete_by_id(self, id):
        """
        Sterge clientul dupa id
        :param id: id-ul dat
        :type id: str
        :return: clientul sters
        :rtype: Client
        :raises: ValueError daca id-ul nu exista
        """
        client = self.find(id)
        if client is None:
            raise ValueError('Nu exista client cu acest id.')

        self.__clients.remove(client)
        return client

    def update(self, id, modified_client):
        """
            Modifica datele clientului cu id dat
            :param id: id dat
            :type id: str
            :param modified_client: clientul cu datele noi
            :type modified_client: Client
            :return: clientul modificat
            :rtype: Client
        """

        client = self.find(id)
        if client is None:
            raise ValueError('Nu exista client cu acest id.')

        client.setNume(modified_client.getNume())
        client.setCNP(modified_client.getCNP())
        client.setEmail(modified_client.getEmail())
        client.setNumarinchirieri(0)
        return client


    def search_by_id(self, id):
        """
        Cauta client dupa id
        :param id: id-ul dat
        :type id: str
        :return: clientul cautat
        :rtype: Client
        :raises: ValueError daca id-ul nu exista
        """
        client = self.find(id)
        if client is None:
            raise ValueError('Nu exista client cu acest id.')

        return client


def test_store():
    pass


def test_get_all_clients():
    pass