class Bibliotecario:
    def __init__(self,nome,CPF,senha):
        self.nome = nome
        self.CPF = CPF
        self.senha = senha

    def __str__(self) -> str:
        return f"Bibliotecario {self.nome} cadastrado sob CPF de n°: {self.CPF}."

class Livros_Cadastrados:
    def __init__(self,nome_livro,autor_livro,editora,qtd_livros):
        self.nome_livro = nome_livro
        self.autor_livro = autor_livro
        self.editora = editora
        self.qtd_livros = qtd_livros
    def __str__(self) -> str:
        return f"Livro: {self.nome} \nAutor: {self.CPF} \nEditora: {self.editora}."

Livros = []
BibliotecariosCadastrados = [Bibliotecario("Marcus",514851,1234), Bibliotecario("Angelo",606702,1234)]
                         
def Cadastro_Bibliotecario():
    nome = input("Digite o nome do Bibliotecario a ser cadastrado: ")
    CPF = int(input("Digite o n° de CPF do bibliotecario sem pontuação: "))
    senha = int(input("Digite uma senha numerica: "))

    for bibliotecario in BibliotecariosCadastrados: #Verifica se o usuario esta cadastrado
        if (CPF == bibliotecario.CPF):
            return print("Bibliotecario já cadastrado.")
        
    bibliotecario = Bibliotecario(nome,CPF,senha)
    BibliotecariosCadastrados.append(bibliotecario)

def Imprimir_Bibliotecarios():
    for bibliotecario in BibliotecariosCadastrados:
        print(bibliotecario)

def Cadastro_Livro():
    global BibliotecariosCadastrados
    global Livros
    CPF_encontrado = False
    
    CPF = int(input("Digite o numero do CPF do Bibliotecario: "))
    for bibliotecario in BibliotecariosCadastrados:
        if (CPF == bibliotecario.CPF):
            senha = int(input("Digite a senha: "))
            for i in range(2):
                if ( senha == bibliotecario.senha):
                    nome = input("Digite o nome do Livro a ser cadastrado: ")
                    autor = input("Digite o nome do autor do livro: ")
                    editora = input("Digite o nome da editora do livro: ")
                    qtd_livros = int(input("Digite a quantidade de livros que possuem na biblioteca: "))

                    Livro = Livros_Cadastrados(nome,autor,editora,qtd_livros)
                    Livros.append(Livro)
                    CPF_encontrado = True
                    break

                else:
                    int(input("Senha incorreta, digite a senha novamente: "))
                    
    if (CPF_encontrado == False):
        print("CPF não Cadastrado")

                    
                

def Imprimir_Livro():
    for livro in Livros:
        print(livro)

Imprimir_Bibliotecarios()
Cadastro_Livro()
Imprimir_Livro()