import pickle,json

class Veiculo :
    def __init__(self, marca , color) -> None:
        self.marca = marca
        self.color = color
    
    def __str__(self) -> str:
    
        return f'la marca {self.marca} el color {self.color}' 
    
class Conversor:
    def __init__(self, path) -> None:
        self.path = path

    def WriteFilepickle(self, object) -> None:
        """
            Convierte un objeto pickle
        """
        f = open(self.path, 'wb')
        pickle.dump(object, f)
        f.close()

    def ReadFilepickle(self) -> object:
        """
           convertir el objeto pickle 
        """
        f = open(self.path, 'rb')
        object = pickle.loads(f)
        f.close()
        return object

    def WriteFileJson(self,object) -> None:
        with open(self.path, "w") as write_file:
            json.dump(object.__dict__, write_file)
        

    def ReadFileJson (self) ->object :
        with open(self.path, "r") as read_file:
            data = json.load(read_file)
        return data