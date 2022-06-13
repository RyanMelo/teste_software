class Hospital:
    def __init__(self):
        self.enfermariaUti = []

    def realizaInternacao(self, paciente):
        if len(self.enfermariaUti) < 3:
            self.enfermariaUti.append(paciente)
            return "Paciente internado com sucesso"
        else:
            return "Nao a leitos disponiveis"

    def realizarAlta(self, paciente):
        if paciente in self.enfermariaUti:
            self.enfermariaUti.remove(paciente)
            return "Paciente teve alta"
        else:
            return "Este paciente nao foi encontrado"



class Paciente:
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome