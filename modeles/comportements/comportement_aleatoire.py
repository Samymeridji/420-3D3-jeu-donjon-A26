import random
from modeles.comportement import Comportement


class ComportementAleatoire(Comportement):

    def agir(self, ennemi) -> str:
        return random.choice(["attaque", "defend"])