class Restaurante:
    def __init__(self, nome,categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        
    def __str__(self):
        return f"{self.nome} | {self.categoria}"
    
restaurante_praca = Restaurante("Praça", "Italiana")
restaurante_pizza = Restaurante ("Pizza Place", "Fast Food")

print(f"Informações do Restaurante: {restaurante_pizza}")
print(f"Informações do Restaurante: {restaurante_praca}")

class Cliente: 
    
    def __init__(self, nome, email,telefone):
        self.nome = nome 
        self.email = email 
        self.telefone = telefone
        self.membro_vibe = False
        
cliente_eliza = Cliente ("Eliza", "eliza.antonucci@gmail.com", 11942900)
cliente_alex = Cliente ("Alex", "Alex.lima@gmail.com", 1165432)
cliente_jenny = Cliente ("jennifer", "jennifer.araujo@gmail.com", 1154398)
    
print(vars(cliente_eliza))
#-----------------
# Modificação de Estado Cliente (ativo)
cliente_alex.membro_vibe = True
print(vars(cliente_alex))
    
print("----" * 20)

#-------------------------
 
# Verifique o valor inicial do atributo ativo
if (restaurante_praca.ativo): 
    print("O restaurante está ativo.")
else: 
    print("O restaurante está inativo")

# -------------------------
#Alterar Atributo de INSTÂNCIA
# Usamos a notação de ponto no objeto específico (restaurante_praca)
restaurante_praca.nome = "Bistrô"
print(f"Novo nome do restaurante Praça: {restaurante_praca.nome}")

# -------------------------
#  Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
if (restaurante_pizza.categoria == "Fast Food"): 
    print("A categoria é Fast Food.")
else: 
    print("A categoria não é Fast Food")

# -------------------------
#  Mudança de Estado Restaurante (Ativo)
restaurante_pizza.ativo = True
if(restaurante_pizza.ativo):
    print("O status do Restaurante Pizza Place Ativo")
else: 
    print("O status do Restaurante Pizza Place Inativo")

