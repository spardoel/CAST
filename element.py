

class Element:
    def __init__(self, *args, **kwargs):
        self.next = None

        ### Default attributes ###
        expected_attributes = ['name', 'family', 'connectable']
        for attr in expected_attributes:
            setattr(self, attr, None)   # Set attributes to None by default

        ### Parse arguments ###
        if args:
            if isinstance(args[0], dict):  # If args exists and first argument is a dictionary
                kwargs.update(args[0])  # Merge it with kwargs

        # Now, kwargs contains all keyword arguments, whether passed as a dict or kwargs. Set the args as attributes
        for key, value in kwargs.items():
            setattr(self, key, value)


    def __str__(self):
        return str(self.__dict__)


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
    
    def printElement(self):
        if self.name == None:
            print(self.id)
        else:   
            print(self.name)

    def _decode_id(self):
        """ Breaks the id down into event, group, and box number. Assuming format FX-3-123"""
        # TODO extracting all 3 every time one is needed is not efficient. 
        id_components = self.id.split('-')
        event = id_components[0]
        group = int(id_components[1])
        box_number = int(id_components[2])
        return event, group, box_number
