from domain.entities import Movie, Client
from domain.validators import MovieValidator, ClientValidator
from repository.movie_repo import InMemoryRepositoryMovies
from repository.client_repo import InMemoryRepositoryClients
from repository.inchiriere_repo import InMemoryRepositoryInchirieri
from service.movie_service import MovieService
from service.client_service import ClientService
from service.inchiriere_service import InchiriereService
from ui.console import Console

repo_m = InMemoryRepositoryMovies()
repo_c = InMemoryRepositoryClients()
repo_i = InMemoryRepositoryInchirieri()
val_m = MovieValidator()
val_c = ClientValidator()
srvm = MovieService(repo_m, val_m)
srvc = ClientService(repo_c, val_c)
srvi = InchiriereService(repo_i)
ui = Console(srvm, srvc, srvi)
ui.movie_ui()