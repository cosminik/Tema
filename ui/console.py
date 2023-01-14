from termcolor import colored
import random

class Console:
    def __init__(self, srv_m, srv_c, srv_i):
        """
        Initializeaza consola
        :type srv_m: MovieService
        :type srv_c: ClientService
        """
        self.__srvm = srv_m
        self.__srvc = srv_c
        self.__srvi = srv_i

    def __print_all_movies(self):
        """
        Afiseaza toate filmele disponibile

        """
        movie_list = self.__srvm.get_all_movies()
        if len(movie_list) == 0:
            print('Nu exista filme in lista.')
        else:
            print('Lista de filme este:')
            for movie in movie_list:
                print('Id film: ', str(movie.getId()), ' - Titlu: ', str(movie.getTitlu()), ' - Descriere: ', str(movie.getDescriere()), ' - Gen: ', str(movie.getGen()), ' - Numar inchirieri: ', str(movie.getNumarinchirieri()))



    def __add_random_movie(self):
        id = random.randrange(1000)
        titlu = self.__srvm.get_random_string(20)
        descriere = self.__srvm.get_random_string(60)
        gen = self.__srvm.get_random_string(10)
        self.__srvm.get_random_movie(id, titlu, descriere, gen)


    def __add_movie(self):
        """
        Adauga un film cu datele citite de la tastatura
        """
        id = int(input('Id film:'))
        try:
            titlu = input("Titlul filmului:")
        except ValueError:
            print(colored('Titlul trebuie sa aiba mai mult de un caracter.', 'red'))
            return

        descriere = input("Descrierea filmului:")
        gen = input("Genul filmului:")

        try:
            added_movie = self.__srvm.add_movie(id, titlu, descriere, gen)
            print('Filmul ' + added_movie.getTitlu() + ' a fost adaugat cu succes.')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __delete_movie(self):
        id = int(input('Identificatorul filmului de sters:'))
        try:
            deleted_movie = self.__srvm.delete_movie(id)
            print('Filmul ' + deleted_movie.getTitlu() + ' a fost sters cu succes (ID=' + str(deleted_movie.getId()) + ').')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __update_movie(self):
        id = int(input('Id film:'))
        try:
            titlu = input("Titlul filmului:")
        except ValueError:
            print(colored('Titlul trebuie sa aiba mai mult de un caracter.', 'red'))
            return

        descriere = input("Descrierea filmului:")
        gen = input("Genul filmului:")

        try:
            modified_movie = self.__srvm.update_movie(id, titlu, descriere, gen)
            print('Filmul ' + modified_movie.getTitlu() +  ' a fost modificat cu succes.')
        except ValueError as ve:
            print(colored(str(ve), 'red'))


    def __search_movie(self):
        id = int(input('Identificatorul filmului cautat:'))
        try:
            searched_movie = self.__srvm.search_movie(id)
            print('Id film: ', colored(searched_movie.getId(), 'cyan'), ' - Titlu: ', colored(str(searched_movie.getTitlu()), 'cyan'), ' - Descriere: ', colored(str(searched_movie.getDescriere()), 'cyan'), ' - Gen: ', colored(str(searched_movie.getGen()), 'cyan'))
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __add_client(self):
        """
        Adauga un client cu datele citite de la tastatura
        """
        id = int(input('Id client:'))
        try:
            nume = input("Numele clientului: ")
        except ValueError:
            print(colored('Numele este prea scurt.', 'red'))
            return
        try:
            CNP = int(input("CNP-ul clientului: "))
        except ValueError:
            print(colored('CNP-ul trebuie sa aiba 13 cifre.', 'red'))
            return
        try:
            email = input("Emailul clientului: ")
        except ValueError:
            print(colored('Email-ul trebuie sa aiba structura "email@email.domeniu".'))
            return
        try:
            added_client = self.__srvc.add_client(id, nume, CNP, email)
            print('Clientul ' + added_client.getNume() + ' a fost adaugat cu succes.')
        except ValueError as ve:
            print(colored(str(ve), 'red'))


    def __add_random_client(self):
        id = random.randrange(1000)
        nume = self.__srvc.get_random_string(20)
        CNP = random.randrange(1000000000000, 10000000000000)
        email = (self.__srvc.get_random_string(8)+"@"+self.__srvc.get_random_string(8)+"."+self.__srvc.get_random_string(6)).lower()
        self.__srvc.get_random_client(id, nume, CNP, email)


    def __print_all_clients(self):
        """
        Afiseaza toti clientii disponibili

        """
        client_list = self.__srvc.get_all_clients()
        if len(client_list) == 0:
            print('Nu exista clienti in lista.')
        else:
            print('Lista de clienti este:')
            for client in client_list:
                print('Id client: ', colored(client.getIdClient(), 'cyan'), ' - Nume: ', colored(str(client.getNume()), 'cyan'), ' - CNP: ', colored(client.getCNP(), 'cyan'), ' - Email: ', colored(str(client.getEmail()), 'cyan'))

    def __delete_client(self):
        id = int(input('Identificatorul clientului de sters:'))
        try:
            deleted_client = self.__srvc.delete_client(id)
            print('Clientul ' + deleted_client.getNume() + ' a fost sters cu succes (ID=' + str(deleted_client.getIdClient()) + ').')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __update_client(self):
        id = int(input('Id client:'))
        try:
            nume = input("Numele clientului: ")
        except ValueError:
            print(colored('Numele este prea scurt.', 'red'))
            return
        try:
            CNP = int(input("CNP-ul clientului: "))
        except ValueError:
            print(colored('CNP-ul trebuie sa aiba 13 cifre.', 'red'))
            return
        try:
            email = input("Emailul clientului: ")
        except ValueError:
            print(colored('Email-ul trebuie sa aiba structura "email@email.domeniu".'))
            return

        try:
            modified_client = self.__srvc.update_client(id, nume, CNP, email)
            print('Clientul ' + modified_client.getNume() +' a fost modificat cu succes.')
        except ValueError as ve:
            print(colored(str(ve), 'red'))


    def __search_client(self):
        id =int(input('Identificatorul clientului cautat:'))
        try:
            searched_client = self.__srvc.search_client(id)
            print('Id client: ', colored(searched_client.getIdClient(), 'cyan'), ' - Nume: ', colored(str(searched_client.getNume()), 'cyan'), ' - Descriere: ', colored(searched_client.getCNP(), 'cyan'), ' - Gen: ', colored(str(searched_client.getEmail()), 'cyan'))
        except ValueError as ve:
            print(colored(str(ve), 'red'))


    def __inchiriere_noua(self):
        id_client = int(input('Id client:'))

        id_movie = int(input("Id film: "))

        added_inchiriere = self.__srvi.new_inchiriere(id_client, id_movie)
        self.__srvm.increasenumarinchirieri(id_movie)
        print('Inchiriere - ', added_inchiriere, 'adaugata cu succes')


    def __print_all_inchirieri(self):

        inchirieri_list = self.__srvi.get_all_inchirieri()
        if len(inchirieri_list) == 0:
            print('Nu exista inchirieri in lista.')
        else:
            print('Lista de inchirieri este:')
            for inchiriere in inchirieri_list:
                print('Id Client: ', inchiriere.getIdClient(), ' - Id film: ', inchiriere.getIdMovie())

    def __returnare(self):
        id_client = int(input('Identificatorul clientului: '))
        id_movie =int(input('Identificatorul filmului: '))
        film_returnat = self.__srvi.returnare(id_client, id_movie)



    def movie_ui(self):
        while True:
            print('Comenzi disponibile: add_random_movie, add_random_client, show_all_movies, add_movie, delete_movie, update_movie, search_movie, show_all_clients, add_client, delete_client, update_client, search_client, inchiriere_film, returnare_film, exit')
            cmd = input('Comanda este:')
            cmd = cmd.lower().strip()
            if cmd == 'add_random_movie':
                self.__add_random_movie()
            elif cmd == 'add_random_client':
                self.__add_random_client()
            elif cmd == 'add_movie':
                self.__add_movie()
            elif cmd == 'add_client':
                self.__add_client()
            elif cmd == 'show_all_movies':
                self.__print_all_movies()
            elif cmd == 'show_all_clients':
                self.__print_all_clients()
            elif cmd == 'delete_movie':
                self.__delete_movie()
            elif cmd == 'delete_client':
                self.__delete_client()
            elif cmd == 'update_movie':
                self.__update_movie()
            elif cmd == 'update_client':
                self.__update_client()
            elif cmd == 'search_movie':
                self.__search_movie()
            elif cmd == 'search_client':
                self.__search_client()
            elif cmd == 'inchiriere_noua':
                self.__inchiriere_noua()
            elif cmd == 'show_all_inchirieri':
                self.__print_all_inchirieri()
            elif cmd == 'returnare':
                self.__returnare()
            elif cmd == 'exit':
                return
            else:
                print(colored('Comanda invalida.', 'red'))