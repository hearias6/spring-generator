
class Columna: 
    
    def __init__(self, nombre_columna='', atributo='', type='', pk='N', fk='N', reference=''): 
         self._nombre_columna = nombre_columna
         self._atributo = atributo
         self._type = type
         self._pk = pk
         self._fk = fk
         self._reference = reference
      
    # getter method 
    def get_nombre_columna(self): 
        return self._nombre_columna 

    def get_atributo(self): 
        return self._atributo

    def get_type(self): 
        return self._type

    def get_pk(self): 
        return self._pk        

    def get_fk(self): 
        return self._fk

    def get_reference(self): 
        return self._reference
      
    # setter method 
    def set_nombre_columna(self, nombre_columna): 
        self._nombre_columna = nombre_columna

    def set_atributo(self, atributo): 
        self._atributo = atributo
        
    def set_type(self, type): 
        self._type = type        

    def set_pk(self, pk): 
        self._pk = pk

    def set_fk(self, fk): 
        self._fk = fk

    def set_reference(self, reference): 
        self._reference = reference