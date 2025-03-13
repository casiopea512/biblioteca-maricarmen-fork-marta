from django.core.management.base import BaseCommand
from faker import Faker
from random import choice
from biblioteca.models import Llibre, Llengua, Exemplar, Usuari


faker = Faker(["es_ES", "es_CA", "en_UK", "fr_FR"])

class Command(BaseCommand):

    help = "Crear 10 llibres i 50 usuaris"

    def handle(self, *args, **options):
        idiomes = {
            "es_ES": "Castellà",
            "es_CA": "Català",
            "fr_FR": "Francès",
            "en_UK": "Anglès"
        }
        
        for idioma_code, idioma_nom in idiomes.items():
            try:
                llengua = Llengua.objects.get(nom=idioma_nom)
            except Llengua.DoesNotExist:
                llengua = Llengua.objects.create(nom=idioma_nom)
            
            faker = Faker(idioma_code)
            print(f"S'ha canviat l'idioma del faker a {idioma_code}")

            print(f"Creant 10 llibres en {idioma_nom}")
            for _ in range(10):
                titol = faker.text(max_nb_chars=50)
                autor = faker.name()
                lloc = faker.country()
                
                llibre = Llibre.objects.create(titol=titol, autor=autor, lloc=lloc, llengua=llengua )
                
                print(f"Creat llibre: {titol} de {autor} a l'idioma ({idioma_nom})")
                
                print("Creant els exemplars de cada llibre")
                for _ in range(2):
                    Exemplar.objects.create(cataleg=llibre)
                    print(f"Creat exemplar de: {titol}")

        print("Creant 50 usuaris")
        for _ in range(50):
            
            username = faker.user_name()
            first_name = faker.first_name()
            last_name = faker.last_name()
            email = faker.email()
            password = faker.password()
            
            user = Usuari.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)

            print(f"Usuari creat: {first_name} {last_name} ({username})")

        print("S'han creat 50 usuaris.")