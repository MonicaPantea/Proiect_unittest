from app.angajat import Angajat


class Test_angajat:

    def setup_method(self):
        print('Se executa la inceput')
        self.angajat = Angajat('Cosma', 'Andrei', 2000)

    def teardown_method(self):
        print('Se executa la final')

    def test_descriere(self):
        assert self.angajat.nume == 'Cosma'
        assert self.angajat.prenume == 'Andrei'
        assert self.angajat.salariu == 2000

    def test_salariu_anual(self):
        assert self.angajat.salariu_anual(2000) == 24000, 'Salariu anual gresit'

    def test_salariu_lunar_dupa_marire_cu_10_la_suta(self):
        assert self.angajat.salariu_lunar_dupa_marire_cu_10_la_suta(2000) == 2200, 'Salariu gresit'
