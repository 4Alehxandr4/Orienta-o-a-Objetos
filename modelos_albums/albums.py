class Album: 
    discografia = []
    
    def __init__(self,nome,elemento,ano):
        self.nome = nome
        self.elemento = elemento
        self.ano = ano
        self._lancado = True # Atributo de CLASSE (valor padrão)
        Album.discografia.append(self)
        
    def __str__(self):
        return f"{self.nome} | {self.elemento} | {self.ano}"
    
    def lista_albums (): 
        print("--- Discografia ---")
        print(f"{'Nome do Album'.ljust(15)} | {'Elemento'.ljust(15)} | {'Ano'.ljust(15)} | {'Status'.ljust(15)}")
        for album in Album.discografia:
            print(f"{album.nome.ljust(15)} | {album.elemento.ljust(15)} | {str(album.ano).ljust(15)} | {album.lancado.ljust(15)}")
            
    @property
    def lancado(self): 
        return "☑" if self._lancado else "⌧"
            
album_lobos = Album("Lobos", "Terra", 2018)
album_antiheroi = Album("Anti-herói", "AR", 2019)
album_pirata = Album("Pirata","Água", 2021)
album_super = Album("Super", "Fogo", 2023)
album_supernova = Album("Supernova", " ", 2024)
        
Album.lista_albums()