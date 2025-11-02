class Restaurante:
    nome = ""
    categoria = ""
    ativo = False
    
restaurante_praca = Restaurante()
restaurante_praca.nome = "Praça"
restaurante_praca.categoria = "Italiana" #Exercício 1: Atribua o valor 'Italiana' ao atributo categoria
# -------------------------

#Exercício 2: Acesse o valor do atributo nome da instância restaurante_praca 
print(f"Qual o nome do restaurante_pizza: {restaurante_praca.nome}")

#-------------------------
 
# Exercício 3: Verifique o valor inicial do atributo ativo
if (restaurante_praca.ativo): 
    print("O restaurante está ativo.")
else: 
    print("O restaurante está inativo")

# -------------------------
# Exercício 4: Acessar Atributo de CLASSE
# Para acessar o valor do molde, usamos o nome da Classe (Restaurante)
categoria = Restaurante.categoria 
# Note: o valor que 'categoria' armazena é "", que é o valor PADRÃO da Classe.
print(f"Valor do atributo de CLASSE 'categoria': {categoria}")

# -------------------------
# Exercício 5: Alterar Atributo de INSTÂNCIA
# Usamos a notação de ponto no objeto específico (restaurante_praca)
restaurante_praca.nome = "Bistrô"
print(f"Novo nome do restaurante Praça: {restaurante_praca.nome}")

# -------------------------
# Exercício 6: Criação e Atribuição de Nova Instância
restaurante_pizza = Restaurante ()
restaurante_pizza.nome = "Pizza Place"
restaurante_pizza.categoria = "Fast Food"

# -------------------------
# Exercício 7: Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
if (restaurante_pizza.categoria == "Fast Food"): 
    print("A categoria é Fast Food.")
else: 
    print("A categoria não é Fast Food")

# -------------------------
# Exercício 8: Mudança de Estado (Ativo)
restaurante_pizza.ativo = True
if(restaurante_pizza.ativo):
    print("O status do Restaurante Pizza Place Ativo")
else: 
    print("O status do Restaurante Pizza Place Inativo")

# -------------------------
# Exercício 9: Impressão de Múltiplos Atributos
print(f"O restaurante {restaurante_praca.nome} é do segmento {restaurante_praca.categoria}")
    