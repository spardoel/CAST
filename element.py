

class Element:
    def __init__(self, id:str = None, name:str=None, value:str=None, family:str=None, connectable:bool=None):
        self.id = id # check id format ? 
        self.name = name
        self.value = value
        self.family = family
        self.connectable = connectable



        self.next = None

    @property
    def event(self):
        #Getter 
        return self._decode_id()[0]
    
    @property
    def group(self):
        #Getter 
        return self._decode_id()[1]
    
    @property
    def box_number(self):
        #Getter 
        return self._decode_id()[2]
    
    def _decode_id(self):
        """ Breaks the id down into event, group, and box number. Assuming format FX-3-123"""
        # TODO extracting all 3 every time one is needed is not efficient. 
        id_components = self.id.split('-')
        event = id_components[0]
        group = int(id_components[1])
        box_number = int(id_components[2])
        return event, group, box_number
