import unittest
import dominio

class casosDeTeste(unittest.TestCase):

    #verificar livro ja emprestado
    def teste_verificaLivroJaEmprestado(self):
        biblioteca = dominio.Biblioteca()
        livro01 = dominio.Livro("#01", "O Poder do Habito")
        funcionario01 = dominio.Funcionario("544.789.998-65", "Ryan")
        usuario01 = dominio.Usuario("Irvayne")

        biblioteca.realizarEmprestimo(funcionario01, livro01, usuario01)

        biblioteca.cadastrarLivro(livro01)
        biblioteca.cadastrarFuncionario(funcionario01)

        verefEmprestado = ""
        verefEmprestado = biblioteca.realizarEmprestimo(funcionario01, livro01, usuario01)
        self.assertEqual(verefEmprestado, "Emprestimo realizado com sucesso")

    #buscar livro nao cadastrado na biblioteca
    def teste_buscaLivroNaoCadastrado(self):
        biblioteca = dominio.Biblioteca()
        livro = dominio.Livro("#01", "Pai Rico Pai Pobre")

        buscaLivro = biblioteca.buscarLivro(livro.nome)
        self.assertEqual(buscaLivro, f"O livro {livro.nome} nao esta cadastrado em nossa biblioteca")

    #devolver um livro nao emprestado
    def teste_devolverLivroNaoEmprestado(self):
        biblioteca = dominio.Biblioteca()
        livro = dominio.Livro("#01", "Senhor dos aneis")
        funcionario = dominio.Funcionario("544.789.998-65", "Ryan")

        biblioteca.cadastrarLivro(livro)
        biblioteca.cadastrarFuncionario(funcionario)

        devolucaoLivro = biblioteca.realizarDevolucao(funcionario, livro)
        self.assertEqual(devolucaoLivro, "Devolucao nao realizada pois o livro nao encontra-se emprestado")

    #limitar emprestimo de no maximo 3 livros
    def teste_limiteDeEmprestimo(self):
        biblioteca = dominio.Biblioteca()
        livro01 = dominio.Livro("#01", "Senhor dos aneis")
        livro02 = dominio.Livro("#02", "Pai Rico Pai Pobre")
        livro03 = dominio.Livro("#03", "O Poder do Habito")
        livro04 = dominio.Livro("#04", "o homem mais rico da babilonia")

        funcionario = dominio.Funcionario("544.789.998-65", "Ryan")

        usuario = dominio.Usuario("Irvayne")
        biblioteca.cadastrarLivro(usuario)

        biblioteca.cadastrarLivro(livro01)
        biblioteca.cadastrarLivro(livro02)
        biblioteca.cadastrarLivro(livro03)
        biblioteca.cadastrarLivro(livro04)

        biblioteca.cadastrarFuncionario(funcionario)

        verefEmprestimo = ""

        biblioteca.realizarEmprestimo(funcionario, livro01, usuario)
        biblioteca.realizarEmprestimo(funcionario, livro02, usuario)
        biblioteca.realizarEmprestimo(funcionario, livro03, usuario)

        verefEmprestimo = biblioteca.realizarEmprestimo(funcionario, livro04, usuario)
        self.assertEqual(verefEmprestimo, "Seu limite de emprestimos foi atingido")

    #solicitar emprestimo com funcionario invalido
    def teste_solicitaEmprestimoFuncionarioInvalido(self):
        biblioteca = dominio.Biblioteca()
        usuario = dominio.Usuario("Irvayne")
        livro = dominio.Livro("#01", "Senhor dos aneis")
        funcionario = dominio.Funcionario("544.789.998-65", "Ryan")

        biblioteca.cadastrarLivro(usuario)
        biblioteca.cadastrarLivro(livro)

        solicitaEmprestimo = biblioteca.realizarEmprestimo(funcionario, livro, usuario)
        self.assertEqual(solicitaEmprestimo, "Funcionario invalido")