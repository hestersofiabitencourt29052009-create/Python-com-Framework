# # framework -  data science
# # interface 
# # 1 pip install streamlit


# # import streamlit as st


# # carregar  -  streamli run mome.py


# import streamlit as st 




# class Portifolio:
#     def __init__(self):
#         nome  =  st.title('Nome')
#         link =  st.error('https://github.com/bea3853')
#         whats = st.write('231321-1231')
#         email =  st.warning('bea@gmail.com')
#         endereco = st.success('rua x, nº x')
#         image = st.image('img.png')
#         audio = st.audio('au.mp3')
#         button =  st.button('Clique aqui')



## **Exercícios extra com Streamlit…**

# **Classe Livro** – crie uma classe com atributos título, autor, ano. Adicione um método `__str__`. Crie uma subclasse `LivroDigital` que adiciona atributo `formato` e sobrescreva `__str__`.

# class Livro:
#     def __init__(self, titulo, autor, ano):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano = ano

#     def __str__(self):
#         return f"{self.titulo} - {self.autor} ({self.ano})"


# class LivroDigital(Livro):
#     def __init__(self, titulo, autor, ano, formato):
#         super().__init__(titulo, autor, ano)
#         self.formato = formato

#     def __str__(self):
#         return f"{self.titulo} - {self.autor} ({self.ano}) [{self.formato}]"


# # Teste
# livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
# livro2 = LivroDigital("Python Básico", "João Silva", 2024, "PDF")

# print(livro1)
# print(livro2)

# **Classe Abstrata Veiculo** – defina uma classe abstrata com método `mover`. Implemente `Carro` e `Bicicleta` com comportamentos diferentes. Teste o polimorfismo.

# from abc import ABC, abstractmethod


# class Veiculo(ABC):

#     @abstractmethod
#     def mover(self):
#         pass


# class Carro(Veiculo):

#     def mover(self):
#         print("O carro está dirigindo 🚗")


# class Bicicleta(Veiculo):

#     def mover(self):
#         print("A bicicleta está pedalando 🚴")


# # Polimorfismo
# veiculos = [Carro(), Bicicleta()]

# for v in veiculos:
#     v.mover()
# **Sobrecarga de operador** – crie uma classe `Vetor` com atributos x, y e implemente `__add__`, `__sub__`, `__mul__` (escalar).
# class Vetor:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, outro):
#         return Vetor(self.x + outro.x, self.y + outro.y)

#     def __sub__(self, outro):
#         return Vetor(self.x - outro.x, self.y - outro.y)

#     def __mul__(self, escalar):
#         return Vetor(self.x * escalar, self.y * escalar)

#     def __str__(self):
#         return f"({self.x}, {self.y})"


# # Teste
# v1 = Vetor(2, 3)
# v2 = Vetor(1, 4)

# print("Soma:", v1 + v2)
# print("Subtração:", v1 - v2)
# print("Multiplicação:", v1 * 3)

**Classe anônima** – use `type` para criar uma classe dinâmica com um método `saudacao`. Instancie-a.
Criando classe dinâmica
Pessoa = type(
    "Pessoa",
    (),
    {
        "saudacao": lambda self: print("Olá! Eu sou uma classe dinâmica 👋")
    }
)

# Instância
p = Pessoa()

# Chamando método
p.saudacao()

import streamlit as st

# st.title("Exercícios de POO")

# st.header("Classe Livro")

# class Livro:
#     def __init__(self, titulo, autor, ano):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano = ano

#     def __str__(self):
#         return f"{self.titulo} - {self.autor} ({self.ano})"


# livro = Livro("Dom Casmurro", "Machado de Assis", 1899)

# st.write(livro)