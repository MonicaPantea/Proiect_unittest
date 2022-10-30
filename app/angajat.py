class Angajat:

    def __init__(self, nume, prenume, salariu):

        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu



    def descriere(self):
        pass

    def salariu_anual(self, salariu):
        return salariu * 12
        pass

    def salariu_lunar_dupa_marire_cu_10_la_suta(self, salariu):
        return salariu + (salariu * 0.1)
        pass

