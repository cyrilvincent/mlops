class Cart:

    def __init__(self):
        self.items = []

class CartService:

    def __init__(self, cart):
        self.cart = cart

    def add(self, id):
        service = AssemblypartService()
        assemblypart = service.getById(id)
        self.cart.items.append(assemblypart)

class Assemblypart:

    def __init__(self, id=0, product = "", lot="", wafer="", device="", img=None):
        self.id = id
        self.product = product
        self.lot = lot
        self.wafer = wafer
        self.device = device
        self.img = img

class AssemblypartService:

    def getById(self, id):
        return [a for a in assembliesMock if a.id == id][0]

    def create(self, id, product, lot, wafer, device):
        a = Assemblypart(id, product, lot, wafer, device, "")
        assembliesMock.append(a)

class Product:

    def __init__(self, filiere, name):
        self.filiere = filiere
        self.name = name

assembliesMock = [
    Assemblypart(1,"iris","t512208","12","s203","img/1.jpg"),
    Assemblypart(2,"iris","t512209","13","s204","img/2.jpg"),
]

productsMock = [
    Product("empire","CT100"),
    Product("iris","CT400")
]
