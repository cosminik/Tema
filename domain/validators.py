import re

from domain.entities import Movie, Client


class MovieValidator:
    def validate(self, Movie):
        errors = []
        if len(Movie.getTitlu()) < 2:
            errors.append('Titlul filmului trebuie sa aiba mai mult de 2 caractere. Filmul nu a fost adaugat')

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

def test_movie_validator():
    test_validator = MovieValidator()
    movie1 = Movie(1, 'The Notebook', 'un prim film frumos', 'romance',0)
    test_validator.validate(movie1)
    movie2 = Movie(2, 'T', 'un film frumos', 'drama',0)

    try:
        test_validator.validate(movie2)
        assert False
    except ValueError:
        assert True


class ClientValidator:
    def validatec(self, Client):
        errors = []
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if len(Client.getNume()) < 6:
            errors.append('Numele clientului trebuie sa aiba mai mult de 6 caractere')
        if Client.getCNP()>10000000000000 or Client.getCNP()<1000000000000:
            errors.append('CNP-ul nu este valid. Clientul nu a fost adaugat.')
        if (re.fullmatch(regex, Client.getEmail())):
            pass
        else:
            errors.append('Email-ul introdus nu este valid. Clientul nu a fost adaugat.')

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

def test_client_validator():
    test_validator = ClientValidator()
    client1 = Client(1, 'Primul Client', 6030405271567, 'email1@yahoo.com',0)
    test_validator.validatec(client1)
    client2 = Client(2, 'Alt Client', 6030405271567, 'email',0)

    try:
        test_validator.validatec(client2)
        assert False
    except ValueError:
        assert True

    client3 = Client(3, 'Nou Client', 603040527156, 'email3@yahoo.com',0)
    try:
        test_validator.validatec(client3)
        assert False
    except ValueError:
        assert True

    client4 = Client(4, 'Nou', 603040527156, 'email3@yahoo.com',0)
    try:
        test_validator.validatec(client4)
        assert False
    except ValueError:
        assert True

test_movie_validator()
test_client_validator()