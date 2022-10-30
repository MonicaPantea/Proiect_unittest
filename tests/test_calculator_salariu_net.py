from app.calculator_salariu_net import Calculator_salariu_net


class Test_calculator_salariu_net:

    def setup_method(self):
        print('Se executa la inceput')
        self.calculator_salariu_net = Calculator_salariu_net(9875)

    def teardown_method(self):
        print('Se executa la final')

    def test_calcul_contributie_asigurari_sociale(self):
        assert self.calculator_salariu_net.calcul_contributie_asigurari_sociale(9875) == 2468.75

    def test_calcul_contributie_asigurari_sociale_de_sanatate(self):
        assert self.calculator_salariu_net.calcul_contributie_asigurari_sociale_de_sanatate(9875) == 987.5

    def test_calcul_contributie_asiguratorie_pentru_munca(self):
        assert self.calculator_salariu_net.calcul_contributie_asiguratorie_pentru_munca(9875) == 222.1875

    def test_calcul_impozit_pe_venit(self):
        assert self.calculator_salariu_net.calcul_impozit_pe_venit(9875) == 987.5

    def test_valoare_salariu_net(self):
        assert self.calculator_salariu_net.valoare_salariu_net(9875) == 5209.0625


