class Album: 
    discografia = []
    
    def __init__(self,nome,elemento,ano):
        self._nome = nome.upper()
        self._elemento = elemento.title()
        self._ano = ano
        self._lancado = True 
        Album.discografia.append(self)
        
    def __str__(self):
        return f"{self._nome} | {self._elemento} | {self._ano}"
    
    @classmethod
    def lista_albums (cls): 
        print("--- Discografia ---")
        print(f"{'Nome do Album'.ljust(15)} | {'Elemento'.ljust(15)} | {'Ano'.ljust(15)} | {'Lançamento'.ljust(15)}")
        for album in cls.discografia:
            print(f"{album._nome.ljust(15)} | {album._elemento.ljust(15)} | {str(album._ano).ljust(15)} | {album.lancado.ljust(15)}")
            
    @property
    def lancado(self): 
        return "☑" if self._lancado else "⌧"
            
album_lobos = Album("Lobos", "Terra", 2018)
album_antiheroi = Album("Anti-herói", "AR", 2019)
album_pirata = Album("Pirata","Água", 2021)
album_super = Album("Super", "Fogo", 2023)
album_supernova = Album("Supernova", " ", 2024)
        
Album.lista_albums()