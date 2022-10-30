from app.aplicatie_de_imbarcare import Aplicatie_de_imbarcare


class Test_aplicatie_de_imbarcare:

    def setup_method(self):
        print('Se executa la inceput')
        self.aplicatie_de_imbarcare = Aplicatie_de_imbarcare(15, 'da', 'da', 'da', 'da', 'da', 'da')

    def teardown_method(self):
        print('Se executa la final')

    def test_te_poti_imbarca(self):    #trece testul
        assert self.aplicatie_de_imbarcare.te_poti_imbarca(15, 'da', 'da', 'da', 'da', 'da', 'da') == 'Te poti imbarca!'

    def test_nu_te_poti_imbarca(self):  #nu trece testul
        assert self.aplicatie_de_imbarcare.nu_te_poti_imbarca(15, 'da', 'da', 'da', 'da', 'da', 'da') ==\
               'Nu te poti imbarca!'

    def test_nu_te_poti_imbarca2(self):  #trece testul
        assert self.aplicatie_de_imbarcare.nu_te_poti_imbarca(15, 'nu', 'nu', 'da', 'da', 'da', 'da') ==\
               'Nu te poti imbarca!'
