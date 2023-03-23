from Clases.Product import Product

class ProductFood(Product):
    tipo="alimento"
    def __init__(self, name, price, restaurant, food_type):
        super().__init__(name, price, restaurant)

        self.food_type=food_type
    
    def show_attr(self):
            print(f"""
Nombre: {self.name}
Precio: {self.price}
Restaurant: {self.restaurant}
Tipo de alimento: {self.food_type}""")

