class Pessoa:
    def __init__(self, nome, data_nascimento, codigo, email):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.codigo = codigo
        self.email = email

    def apresentar(self):
        print(f"Olá, sou {self.nome}. Minha data de nascimento é {self.data_nascimento}\n"
              f"e meu código é {self.codigo}. Meu e-mail: {self.email}")
        print("-" * 50)


class Professor(Pessoa):
    def __init__(self, nome, data_nascimento, codigo, email, especialidade, trabalhando=False, especializando=False):
        super().__init__(nome, data_nascimento, codigo, email)
        self.especialidade = especialidade
        self.trabalhando = trabalhando
        self.especializando = especializando
        self.salario = 0
        self.atribuir_salario()

    def atribuir_salario(self):
        if self.trabalhando:
            self.salario = 7400
            if self.especializando:
                self.salario += 1900
        else:
            self.salario = 0

    def apresentar(self):
        print(f"Professor: {self.nome}")
        print(f"Especialidade: {self.especialidade}")
        print(f"Data de nascimento: {self.data_nascimento} | Código: {self.codigo}")
        print(f"Salário: R$ {self.salario:.2f}")
        print(f"Email profissional: {self.email}")
        print("-" * 50)


class Aluno(Pessoa):
    def __init__(self, nome, data_nascimento, codigo, email, turma=None):
        super().__init__(nome, data_nascimento, codigo, email)
        self.turma = turma
        self.notas_por_materia = {}

    def adicionar_nota(self, materia, nota):
        if materia not in self.notas_por_materia:
            self.notas_por_materia[materia] = []
        self.notas_por_materia[materia].append(nota)

    def calcular_media(self, materia=None):
        if materia:
            if materia in self.notas_por_materia:
                notas = self.notas_por_materia[materia]
                return sum(notas) / len(notas) if notas else 0.0 #sum = soma, len = numero de elementos p/ objeto
            return 0.0
        else:  # Média geral em todas as matérias
            todas_notas = [nota for notas in self.notas_por_materia.values() for nota in notas]
            return sum(todas_notas) / len(todas_notas) if todas_notas else 0.0

    def apresentar(self):
        print(f"Aluno: {self.nome}")
        print(f"Data de nascimento: {self.data_nascimento} | Código: {self.codigo}")
        print(f"Email: {self.email}")
        if self.turma:
            print(f"Turma: {self.turma}")
        print("Boletim:")
        for materia, notas in self.notas_por_materia.items():
            media = sum(notas) / len(notas) if notas else 0
            print(f"  Matéria: {materia} | Notas: {notas} | Média: {media:.2f}")
        print(f"Média Geral: {self.calcular_media():.2f}")
        print("-" * 50)


class Turma:
    def __init__(self, nome_turma, ano):
        self.nome_turma = nome_turma
        self.ano = ano
        self.professores = []
        self.alunos = []

    def adicionar_professor(self, professor):
        if isinstance(professor, Professor):
            self.professores.append(professor)
            print(
                f"O professor {professor.nome} foi atribuído à turma {self.nome_turma} para a disciplina {professor.especialidade}.")
        else:
            print("Apenas objetos do tipo Professor podem ser atribuídos como responsáveis pela turma.")

    def adicionar_aluno(self, aluno):
        if isinstance(aluno, Aluno):
            aluno.turma = self.nome_turma
            self.alunos.append(aluno)
            print(f"O aluno {aluno.nome} foi adicionado à turma {self.nome_turma}.")
        else:
            print("Apenas objetos do tipo Aluno podem ser adicionados à turma.")

    def listar_participantes(self):
        print(f"Turma: {self.nome_turma} | Ano: {self.ano}")
        print("-" * 50)
        print("Professores da Turma:")
        for professor in self.professores:
            professor.apresentar()
        print("Alunos da Turma:")
        for aluno in self.alunos:
            aluno.apresentar()

    def calcular_media_turma(self):
        print(f"Média geral por aluno na Turma: {self.nome_turma}")
        for aluno in self.alunos:
            print(f"Aluno: {aluno.nome} | Média Geral: {aluno.calcular_media():.2f}")
        print("-" * 50)







#aqui nois cria os bagulho
Turma = Turma(nome_turma="Turma 3°", ano=2025)


professor1 = Professor(nome="LuckNinja", data_nascimento="10/02/2000", codigo="Professor001", email="luckNinja@professorSenai.com",
                       especialidade="FrontEnd", trabalhando=True, especializando=True)

professor2 = Professor(nome="luciano", data_nascimento="05/05/1995", codigo="Professor002", email="Luciano@professorSenai.com",
                       especialidade="BackEnd", trabalhando=True, especializando=True)

professor3 = Professor(nome="Jean", data_nascimento="26/03/1998", codigo="Professor003", especialidade="Matemática" ,email="Jean@professorSeSi.com", trabalhando=True)

Turma.adicionar_professor(professor1)
Turma.adicionar_professor(professor2)
Turma.adicionar_professor(professor3)

# Criar alunos
aluno1 = Aluno(nome="Gabriel", data_nascimento="01/01/2007", codigo="ALUNO001", email="G.briel@alunoSenai.com")
aluno2 = Aluno(nome="gustavo", data_nascimento="14/03/2007", codigo="ALUNO002", email="Gustavo@alunoSenai.com")
aluno3 = Aluno(nome="guilherme MAMOU", data_nascimento="12/04/2006", codigo="ALUNO003", email="pedeLeite@alunoSenai.com")


aluno1.adicionar_nota("BackEnd", 9.5)
aluno1.adicionar_nota("BackEnd", 10.0)
aluno1.adicionar_nota("FrontEnd", 9.5)
aluno1.adicionar_nota("FrontEnd", 10.0)
aluno1.adicionar_nota("matemática", 10.0)
aluno1.adicionar_nota("matemática", 10.0)

aluno2.adicionar_nota("BackEnd", 8.5)
aluno2.adicionar_nota("BackEnd", 9.0)
aluno2.adicionar_nota("FrontEnd", 9.0)
aluno2.adicionar_nota("FrontEnd", 8.0)
aluno2.adicionar_nota("matemática", 9.0)
aluno2.adicionar_nota("matemática", 10.0)

aluno3.adicionar_nota("BackEnd", 7.5)
aluno3.adicionar_nota("BackEnd", 8.0)
aluno3.adicionar_nota("FrontEnd", 8.3)
aluno3.adicionar_nota("FrontEnd", 7.0)
aluno3.adicionar_nota("matemática", 8.0)
aluno3.adicionar_nota("matemática", 9.0)


Turma.adicionar_aluno(aluno1)
Turma.adicionar_aluno(aluno2)
Turma.adicionar_aluno(aluno3)
