class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.faturas = []

    def adicionar_fatura(self, fatura):
        self.faturas.append(fatura)

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'


class Fatura:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor

    def __str__(self):
        return f'Descrição: {self.descricao}, Valor: R$ {self.valor:.2f}'


class Casa:
    def __init__(self, endereco):
        self.endereco = endereco
        self.moradores = []

    def adicionar_morador(self, pessoa):
        self.moradores.append(pessoa)

    def __str__(self):
        return f'Endereço: {self.endereco}, Moradores: {[pessoa.nome for pessoa in self.moradores]}'

# Exemplo de uso:

# Criando algumas pessoas
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)
pessoa3 = Pessoa("Carol", 35)

# Criando algumas faturas
fatura1 = Fatura("Aluguel", 1000)
fatura2 = Fatura("Eletricidade", 150)
fatura3 = Fatura("Água", 50)

# Adicionando faturas às pessoas
pessoa1.adicionar_fatura(fatura1)
pessoa2.adicionar_fatura(fatura2)
pessoa3.adicionar_fatura(fatura3)

# Criando uma casa e adicionando moradores
casa = Casa("123 Main Street")
casa.adicionar_morador(pessoa1)
casa.adicionar_morador(pessoa2)
casa.adicionar_morador(pessoa3)

# Imprimindo informações
print("Informações da Casa:")
print(casa)
print("\nMoradores e suas Faturas:")
for morador in casa.moradores:
    print(morador)
    for fatura in morador.faturas:
        print(fatura)
