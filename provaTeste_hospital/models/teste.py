import dominio
import unittest

class CasosDeTestes(unittest.TestCase):
    # Realizar internacao
    def teste_realizarInternacao(self):
        hospital = dominio.Hospital()
        paciente = dominio.Paciente("999.999.999-67", "Chico")

        resultInter = hospital.realizaInternacao(paciente)
        self.assertEqual(resultInter, "Paciente internado com sucesso")

    # Realizar alta
    def teste_realizarAlta(self):
        hospital = dominio.Hospital()
        paciente = dominio.Paciente("999.999.999-67", "Chico")

        hospital.realizaInternacao(paciente)

        resultAlta = hospital.realizarAlta(paciente)
        self.assertEqual(resultAlta, "Paciente teve alta")

    #Nao a lietos disponiveis
    def teste_leitosDisponiveis(self):
        hospital = dominio.Hospital()
        paciente01 = dominio.Paciente("999.999.999-67", "Chico")
        paciente02 = dominio.Paciente("999.999.999-63", "Joao")
        paciente03 = dominio.Paciente("999.999.999-65", "Francisco")
        paciente04 = dominio.Paciente("999.999.999-68", "Igo")

        hospital.realizaInternacao(paciente01)
        hospital.realizaInternacao(paciente02)
        hospital.realizaInternacao(paciente03)

        verificaLeitos = hospital.realizaInternacao(paciente04)
        self.assertEqual(verificaLeitos, "Nao a leitos disponiveis")