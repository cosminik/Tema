import random
import string
class Movie:
    no_instances = 0

    def __init__(self, id, titlu, descriere, gen,numar_inchirieri):
        """
        Creeaza un nou film cu titlul, descrierea si genul dat
        :param id: id-ul filmului
        :type id: int
        :param titlu: titlul filmului
        :type titlu: str
        :param descriere: descrierea filmului
        :type descriere: str
        :param gen: genul filmului
        :type gen: str

        """

        self.__id = id
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen
        self.__numar_inchirieri=numar_inchirieri
        Movie.no_instances += 1

    def getId(self):
        return self.__id

    def get_random_string(length):
        result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
        print(result_str)

    def getTitlu(self):
        return self.__titlu

    def getDescriere(self):
        return self.__descriere

    def getGen(self):
        return self.__gen
    def getNumarinchirieri(self):
        return self.__numar_inchirieri
    def setId(self, value):
        self.__id = value

    def setTitlu(self, value):
        self.__titlu = value

    def setDescriere(self, value):
        self.__descriere = value

    def setGen(self, value):
        self.__gen = value
    def setNumarinchirieri(self,value):
        self.__numar_inchirieri=value
    def increasenumarinchirieri(self):
        self.__numar_inchirieri+=1
    def __eq__(self, other):
        """
        Verifica egalitatea intre filmul curent si filmul other
        :param other:
        :type other: Movie
        :return: True daca filmele sunt egale (=au acelasi id si acelasi titlu), False altfel
        :rtype: bool
        """
        if self.__id == other.getId() and self.__titlu == other.getTitlu():
            return True
        return False

    def __str__(self):
        return f"Id film: {self.__id} ; Titlu film: {self.__titlu} ; Descriere: {self.__descriere} ; Gen: {self.__gen} ; Numar inchirieri: {self.__numar_inchirieri}"
    @staticmethod
    def getNumberOfMovieObjects():
        return Movie.no_instances


def test_create_movie():
    movie1 = Movie(1, 'The Notebook', 'un prim film frumos', 'romance',0)
    assert (movie1.getId() == 1)
    assert (movie1.getTitlu() == 'The Notebook')
    assert (movie1.getDescriere() == 'un prim film frumos')
    assert (movie1.getGen() == 'romance')

    movie1.setId(1)
    movie1.setTitlu('The Notebook')
    movie1.setDescriere('un prim film frumos')
    movie1.setGen('romance')

    assert (movie1.getId() == 1)
    assert (movie1.getTitlu() == 'The Notebook')
    assert (movie1.getDescriere() == 'un prim film frumos')
    assert (movie1.getGen() == 'romance')


def test_equals_movie():
    movie1 = Movie(1, 'The Notebook', 'un prim film frumos', 'romance',0)
    movie2 = Movie(1, 'The Notebook', 'un prim film frumos', 'romance',0)

    assert (movie1 == movie2)

    movie3 = Movie(2, 'Titanic', 'un alt film frumos', 'romance',0)
    assert (movie1 != movie3)


class Client:
    no_instances = 0

    def __init__(self, id, nume, CNP, email,numar_inchirieri):
        """
                Creeaza un nou client cu numele, CNP-ul si emailul dat
                :param id: id-ul clientului
                :type id: int
                :param nume: numele clientului
                :type nume: str
                :param CNP: CNP-ul clientului
                :type CNP: int
                :param email: email-ul clientului
                :type email: str

                """

        self.__idClient = id
        self.__nume = nume
        self.__CNP = CNP
        self.__email = email
        self.__numar_inchirieri=numar_inchirieri
        Client.no_instances += 1

    def getIdClient(self):
        return self.__idClient

    def getNume(self):
        return self.__nume

    def getCNP(self):
        return self.__CNP

    def getEmail(self):
        return self.__email
    def getNumarinchirieri(self):
        return self.__numar_inchirieri
    def get_random_string(length):
        result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
        print(result_str)


    def setIdClient(self, value):
        self.__idClient = value

    def setNume(self, value):
        self.__nume = value

    def setCNP(self, value):
        self.__CNP = value

    def setEmail(self, value):
        self.__email = value
    def setNumarinchirieri(self,value):
        self.__numar_inchirieri=value
        
    def __eq__(self, other):
        """
        Verifica egalitatea intre clientul curent si clientul other
        :param other:
        :type other: Client
        :return: True daca clientii sunt egali (=au acelasi id si acelasi nume), False altfel
        :rtype: bool
        """
        if self.__idClient == other.getIdClient() and self.__nume == other.getNume():
            return True
        return False

    def __str__(self):
        return f"Id client: {self.__idClient} ; Nume:{ self.__nume}  ; CNP: {self.__CNP} ; Email: { self.__email}; Numar inchirieri : {self.__numar_inchirieri}"

    @staticmethod
    def getNumberOfClientObjects():
        return Client.no_instances


def test_create_client():
    client1 = Client(1, 'Primul Client', 6030405271567, 'email1@yahoo.com',0)
    assert (client1.getIdClient() == 1)
    assert (client1.getNume() == 'Primul Client')
    assert (client1.getCNP() == 6030405271567)
    assert (client1.getEmail() == 'email1@yahoo.com')

    client1.setIdClient(1)
    client1.setNume('Primul Client')
    client1.setCNP(6030405271567)
    client1.setEmail('email1@yahoo.com')

    assert (client1.getIdClient() == 1)
    assert (client1.getNume() == 'Primul Client')
    assert (client1.getCNP() == 6030405271567)
    assert (client1.getEmail() == 'email1@yahoo.com')


def test_equals_client():
    client1 = Client(1, 'Primul Client', 6030405271567, 'email1@yahoo.com',0)
    client2 = Client(1, 'Primul Client', 6030405271567, 'email1@yahoo.com',0)

    assert (client1 == client2)

    client3 = Client(2, 'Alt Client', 6030405271566, 'email3@yahoo.com',0)
    assert (client1 != client3)


class inchiriere:
    no_instances = 0

    def __init__(self, id_client, id_movie):
        """
        Creeaza o noua inchiriere cu id-ul clientului si id-ul filmului inchiriat
        :param id_client: id-ul clientului
        :type id: str
        :param id_movie: id-ul filmului
        :type id_movie: str
        """

        self.__id_client = id_client
        self.__id_movie = id_movie
        inchiriere.no_instances += 1

    def getIdClient(self):
        return self.__id_client

    def getIdMovie(self):
        return self.__id_movie

    def setIdClient(self, id):
        self.__id_client = id

    def setIdMovie(self, id):
        self.__id_movie = id

    def __str__(self):
        return f"Id client: {self.__id_client} ; Id film: {self.__id_movie}"

    @staticmethod
    def getNumberOfInchiruereObjects():
        return inchiriere.no_instances

class returnare:
    no_instances = 0

    def __init__(self, id_client, id_movie):
        """
        Creeaza o noua returnare cu id-ul clientului si id-ul filmului inchiriat
        :param id_client: id-ul clientului
        :type id: str
        :param id_movie: id-ul filmului
        :type id_movie: str
        """

        self.__id_client = id_client
        self.__id_movie = id_movie
        inchiriere.no_instances += 1

    def getIdClient(self):
        return self.__id_client

    def getIdMovie(self):
        return self.__id_movie

    def setIdClient(self, id):
        self.__id_client = id

    def setIdMovie(self, id):
        self.__id_movie = id

    def __str__(self):
        return "Id client: " + str(self.__id_client) + '; Id film: ' + self.__id_movie


    @staticmethod
    def getNumberOfReturnareObjects():
        return returnare.no_instances


test_create_movie()
test_equals_movie()
test_create_client()
test_equals_client()