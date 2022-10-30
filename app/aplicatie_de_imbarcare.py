class Aplicatie_de_imbarcare:

    def __init__(self, varsta, tara_de_calatorie_UE, pasaport,
                 insotit_de_mama, insotit_de_tata, act_permisiunea_mama, act_permisiunea_tata):

        self.varsta = varsta
        self.tara_de_calatorie_UE = tara_de_calatorie_UE
        self.pasaport = pasaport
        self.insotit_de_mama = insotit_de_mama
        self.insotit_de_tata = insotit_de_tata
        self.act_permisiunea_mama = act_permisiunea_mama
        self.act_permisiunea_tata = act_permisiunea_tata

    def te_poti_imbarca(self, varsta, tara_de_calatorie_UE, pasaport,
                        insotit_de_mama, insotit_de_tata, act_permisiunea_mama, act_permisiunea_tata):

        if varsta > 18 and tara_de_calatorie_UE == 'da':
            return 'Te poti imbarca!'
            pass
        elif varsta > 18 and tara_de_calatorie_UE == 'nu' and pasaport == 'da':
            return 'Te poti imbarca!'
            pass
        elif varsta < 18 and tara_de_calatorie_UE == 'da' and insotit_de_tata == 'da' and act_permisiunea_mama == 'da':
            return 'Te poti imbarca!'
            pass
        elif varsta < 18 and tara_de_calatorie_UE == 'da' and insotit_de_mama == 'da' and act_permisiunea_tata == 'da':
            return 'Te poti imbarca!'
            pass
        elif varsta < 18 and tara_de_calatorie_UE == 'da' and insotit_de_mama == 'da' and insotit_de_tata == 'da':
            return 'Te poti imbarca!'
            pass
        elif varsta < 18 and tara_de_calatorie_UE == 'nu' and pasaport == 'da' and insotit_de_tata == 'da' and \
                act_permisiunea_mama == 'da':
            return 'Te poti imbarca!'
            pass
        elif varsta < 18 and tara_de_calatorie_UE == 'nu' and pasaport == 'da' and insotit_de_mama == 'da' and \
                act_permisiunea_tata == 'da':
            return 'Te poti imbarca!'
            pass
        elif varsta < 18 and tara_de_calatorie_UE == 'nu' and pasaport == 'da' and \
                insotit_de_mama == 'da' and insotit_de_tata == 'da':
            return 'Te poti imbarca!'
            pass

    def nu_te_poti_imbarca(self, varsta, tara_de_calatorie_UE, pasaport,
                           insotit_de_mama, insotit_de_tata, act_permisiunea_mama, act_permisiunea_tata):

        if varsta > 18 and tara_de_calatorie_UE == 'nu' and pasaport == 'nu':
            return 'Nu te poti imbarca!'
            pass
        elif varsta < 18 and tara_de_calatorie_UE == 'da' and insotit_de_tata == 'da' and act_permisiunea_mama == 'nu':
            return 'Nu te poti imbarca!'
            pass
        elif varsta < 18 and tara_de_calatorie_UE == 'da' and insotit_de_mama == 'da' and act_permisiunea_tata == 'nu':
            return 'Nu te poti imbarca!'
            pass
        elif varsta < 18 and tara_de_calatorie_UE == 'nu' and pasaport == 'da' and insotit_de_tata == 'da' and \
                act_permisiunea_mama == 'nu':
            return 'Nu te poti imbarca!'
            pass
        elif varsta < 18 and tara_de_calatorie_UE == 'nu' and pasaport == 'da' and insotit_de_mama == 'da' and \
                act_permisiunea_tata == 'nu':
            return 'Nu te poti imbarca!'
            pass
        elif varsta < 18 and tara_de_calatorie_UE == 'nu' and pasaport == 'nu':
            return 'Nu te poti imbarca!'
            pass

