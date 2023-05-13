#Funcional
class Bibliotecario:
    def __init__(self,nome,CPF,senha):
        self.nome = nome
        self.CPF = CPF
        self.senha = senha

    def __str__(self) -> str:
        return f"Bibliotecario {self.nome} cadastrado sob CPF de n°: {self.CPF}."
#Funcional
class Aluno:
    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
        self.qtd_livros_posse = 0
        self.livro_posse = ""
        self.periodo_devolucao = "00-00-0000"
    
    def Adcionar_Livro(self,nome_livro, devolucao):
        self.livro_posse = nome_livro
        self.periodo_devolucao = devolucao
        
    def __str__(self) -> str:
        return f"Aluno {self.nome} cadastrado sob matricula de n°: {self.matricula}."    
    
#Funcional
class Livros_Cadastrados:
    def __init__(self,nome_livro,autor_livro,editora,qtd_livros):
        self.nome_livro = nome_livro
        self.autor_livro = autor_livro
        self.editora = editora
        self.qtd_livros = qtd_livros
        
    def __str__(self):
        return f"Livro: {self.nome_livro} \nAutor: {self.autor_livro} \nEditora: {self.editora}."

BibliotecariosCadastrados = [Bibliotecario("Marcus",514851,1234), Bibliotecario("Angelo",606702,1234)]
AlunosCadastrados = [Aluno("Luan",1234)]
LivrosCadastrados = []
LivrosAlugados = []

#Funcional               
def Cadastro_Bibliotecario():
    nome = input("Digite o nome do Bibliotecario a ser cadastrado: ")
    CPF = int(input("Digite o n° de CPF do bibliotecario sem pontuação: "))
    senha = int(input("Digite uma senha numerica: "))

    for bibliotecario in BibliotecariosCadastrados: #Verifica se o usuario esta cadastrado
        if (CPF == bibliotecario.CPF):
            return print("Bibliotecario já cadastrado.")
        
    bibliotecario = Bibliotecario(nome,CPF,senha)
    BibliotecariosCadastrados.append(bibliotecario)

#Funcional
def Validar_Senha(CPF):
    for bibliotecario in BibliotecariosCadastrados:
        if (CPF == bibliotecario.CPF):
            for i in range(3):
                if ( i == 0):
                    senha = int(input("Digite a senha: "))
                    if ( senha == bibliotecario.senha ):
                        return True
                else: 
                    senha = int(input("Senha Incorreta, digite a senha novamente: "))
                    if ( senha == bibliotecario.senha ):
                        return True
            return False
    
#Funcional
def Imprimir_Bibliotecarios():
    for bibliotecario in BibliotecariosCadastrados:
        print(bibliotecario)

#Funcional               
def Cadastro_Aluno():
    nome = input("Digite o nome do Aluno a ser cadastrado: ")
    matricula = int(input("Digite o n° de matricula do Aluno sem pontuação: "))

    for aluno in AlunosCadastrados: #Verifica se o usuario esta cadastrado
        if (matricula == aluno.matricula):
            return print("Aluno já cadastrado.")
        
    aluno = Aluno(nome,matricula)
    AlunosCadastrados.append(aluno)

#Funcional
def Imprimir_Alunos():
    for aluno in AlunosCadastrados:
        print(aluno)


#Funcional
def Cadastro_Livro():
    CPF_encontrado = False
    
    CPF = int(input("Digite o numero do CPF do Bibliotecario: "))
    if ( Validar_Senha(CPF) == True ):
        nome = input("Digite o nome do Livro a ser cadastrado: ")
        autor = input("Digite o nome do autor do livro: ")
        editora = input("Digite o nome da editora do livro: ")
        qtd_livros = int(input("Digite a quantidade de livros que possuem na biblioteca: "))

        Livro = Livros_Cadastrados(nome,autor,editora,qtd_livros)
        Livros.append(Livro)
        CPF_encontrado = True
                          
    if (CPF_encontrado == False):
        print("CPF não Cadastrado")

#Funcional
def Imprimir_Livro():
    for livro in Livros:
        print(livro)

def Aluguel_livro():
    CPF_encontrado = False
    Imprimir_Livro()

    CPF = int(input("Digite o numero do CPF do Bibliotecario: "))
    
    if ( Validar_Senha(CPF) == True):
        nome = input("Digite o nome do Livro que deseja Alugar: ")
        for livro in Livros:
            if ( nome.upper() ==  )
            qtd_livros = int(input("Digite a quantidade de livros que possuem na biblioteca: "))

            Livro = Livros_Cadastrados(nome,autor,editora,qtd_livros)
            Livros.append(Livro)
            CPF_encontrado = True
                        
    if (CPF_encontrado == False):
        print("CPF não Cadastrado")


Imprimir_Bibliotecarios()
A = AlunosCadastrados[0]
A.Adcionar_Livro("Harry","21-03-2921")
print(A.livro_posse)