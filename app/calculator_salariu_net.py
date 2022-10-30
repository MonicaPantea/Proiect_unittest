class Calculator_salariu_net:

    def __init__(self, salariu_brut):
        self.salariu_brut = salariu_brut

    def calcul_contributie_asigurari_sociale(self, salariu_brut):
        return salariu_brut * 0.25
        pass

    def calcul_contributie_asigurari_sociale_de_sanatate(self, salariu_brut):
        return salariu_brut * 0.1
        pass

    def calcul_contributie_asiguratorie_pentru_munca(self, salariu_brut):
        return salariu_brut * 0.0225
        pass

    def calcul_impozit_pe_venit(self, salariu_brut):
        return salariu_brut * 0.1
        pass

    def valoare_salariu_net(self, salariu_brut):
        total_contributii = (salariu_brut * 0.25) + (salariu_brut * 0.1) + (salariu_brut * 0.0225) + (
                    salariu_brut * 0.1)
        return salariu_brut - total_contributii
        pass
