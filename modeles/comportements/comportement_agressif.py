from modeles.comportement import Comportement


class ComportementAgressif(Comportement):

    def agir(self, ennemi) -> str:
        return "attaque"