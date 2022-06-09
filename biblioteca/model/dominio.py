class Biblioteca:

    def __init__(self):
        self.livros = []
        self.funcionario = []
        self.emprestimos = []

    def cadastrarLivro(self, livro):
        self.livros.append(livro)

    def cadastrarFuncionario(self, funcionario):
        self.funcionario.append(funcionario)

    def validarFuncionario(self, funcionario):
        for func in self.funcionario:
            if func.cpf == funcionario.cpf:
                return True
        return False

    def realizarEmprestimo(self, funcionario, livro, usuario):
        if self.validarFuncionario(funcionario):
            emprestimo = Emprestimo(usuario, livro)
            if len(self.emprestimos) < 3:
                self.emprestimos.append(emprestimo)
                return "Emprestimo realizado com sucesso"
            else:
                return "Seu limite de emprestimos foi atingido"
        return "Funcionario invalido"

    def realizarDevolucao(self, funcionario, livro):
        if self.validarFuncionario(funcionario):
            for emprestimo in self.emprestimos:
                if livro.id == emprestimo.livro.id:
                    self.emprestimos.remove(emprestimo)
                    return "Devolucao realizada com sucesso"
            return "Devolucao nao realizada pois o livro nao encontra-se emprestado"
        return "Funcionario invalido"

    def buscarLivro(self, livro):
        if livro in self.livros:
            return f"{livro} encotrado"
        else:
            return f"O livro {livro} nao esta cadastrado em nossa biblioteca"


class Livro:

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Funcionario:

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

class Usuario:

    def __init__(self, nome):
        self.nome = nome

class Emprestimo:

    def __init__(self, usuario: Usuario, livro: Livro):
        self.usuario = usuario
        self.livro = livro