class autore:
    def __init__(self, birth, death, where_born, where_death ,name, lived_in, desc):
        self.birth = birth
        self.death = death
        self.w_death = where_death
        self.w_born = where_born
        self.name = name
        self.lived_in = lived_in
        self.desc = desc
        
    def __repr__(self):
        
        return f"{self.desc}"
    
    def associa_libri (self):
        pass