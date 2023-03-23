import requests
import os
from Clases.Restaurant import Restaurant
from Clases.ProductDrink import ProductDrink as Drink
from Clases.ProductFood import ProductFood as Food
from Clases.ClientVIP import ClientVIP as VIP
from Clases.Factura import Factura

class AppME():
    def __init__(self):
        self.restaruants=[]
        self.clients=[]

        self.restaurants=[]
        self.productos_food=[]
        self.productos_drinks=[]

    
    def auxiliary_clients(self):
        pass
    
    def donwload_api(self):
        url_races='https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json'
        response_r=requests.request("GET", url_races)

        directory = os.getcwd()+"/TXT/Modulo IV/"
        file_name = "Restaurant.txt"
        with open(directory + file_name,"w") as f:
            for restaurant in response_r.json():
                res=restaurant["name"]
                for r in restaurant["restaurants"]:
                    x=[]
                    y=r["name"]
                    for i in r["items"]:
                        c=i["name"]
                        x.append(c)
                    
                    f.write(f"{y}|{res}|{x}\n")
        
        file_name = "ProductDrink.txt"
        with open(directory + file_name,"w") as f:
            for race in response_r.json():
                for restaurant in race["restaurants"]:
                    res=restaurant["name"]
                    for drink in restaurant["items"]:
                        if drink["type"]=="drink:alcoholic":
                            f.write(f'{drink["name"]}|{drink["price"]}|{res}|SI|\n')
                        elif drink["type"]=="drink:not-alcoholic":
                            f.write(f'{drink["name"]}|{drink["price"]}|{res}|NO|\n')

        file_name = "ProductFood.txt"
        with open(directory + file_name,"w") as f:
            for race in response_r.json():
                for restaurant in race["restaurants"]:
                    res=restaurant["name"]
                    for food in restaurant["items"]:
                        if food["type"]=="food:restaurant":
                            f.write(f'{food["name"]}|{food["price"]}|{res}|Restaurant|\n')
                        elif food["type"]=="food:fast":
                            f.write(f'{food["name"]}|{food["price"]}|{res}|Fast|\n')
        
    def from_txt_to_list(self):
        directory= os.getcwd()+"/TXT/Modulo IV/"
        self.restaurants=[]
        file_name='Restaurant.txt'
        with open(directory+file_name) as f:
            for line in f:
                restaurant= Restaurant(line.split("|")[0],line.split("|")[1],line.split("|")[2])
                self.restaurants.append(restaurant)
        
        
        self.productos_drinks=[]
        file_name='ProductDrink.txt'
        with open(directory+file_name) as f:
            for line in f:
                drink= Drink(line.split("|")[0],float(line.split("|")[1]),line.split("|")[2],line.split("|")[3])
                self.productos_drinks.append(drink)
        
        self.productos_food=[]
        file_name='ProductFood.txt'
        with open(directory+file_name) as f:
            for line in f:
                food= Food(line.split("|")[0],float(line.split("|")[1]),line.split("|")[2],line.split("|")[3])
                self.productos_food.append(food)

    #MODULO 4
    def search_pro_name(self):
        print("\nBÚSQUEDA POR TIPO DE PRODUCTO")
        restaurantes=[]
        for restaurant in self.restaurants:
            restaurantes.append(restaurant.nombre)

        for i, restaurant in enumerate(restaurantes):
            print(f"{i+1}. {restaurant}")

        while True:
            try:
                op=int(input("Ingrese el número del restaruante que desea ver: "))
                while op not in range(len(restaurantes)):
                    raise Exception
                break
            except: 
                print("Ingreso inválido, intente nuevamente: ")

        r=restaurantes[op-1]
        productos=[]
        for alimento in self.productos_food:
            if r==alimento.restaurant:
                productos.append(alimento)
        
        for bebida in self.productos_drinks:
            if r==bebida.restaurant:
                productos.append(bebida)
        
        for i, product in enumerate(productos):
            print(f"{i+1}. {product.name}")
        
        option=input('Seleccione el producto que desea visualizar: ')
        while not option.isnumeric() or int(option) not in range(len(productos)+1):
            option=input("Error: ingreso inválido, intente nuevamente.")
        
        productos[int(option)-1].show_attr()
        
    def search_pro_type(self):
        print("\nBÚSQUEDA POR TIPO DE PRODUCTO")
        alcoholica=[]
        no_alcoholica=[]
        restaurant=[]
        fast=[]

        for drink in self.productos_drinks:
            if drink.drink_type=="SI":
                alcoholica.append(drink)
            elif drink.drink_type=="NO":
                no_alcoholica.append(drink)
        
        for food in self.productos_food:
            if food.food_type=="Restaurant":
                restaurant.append(food)
            elif food.food_type=="Fast":
                fast.append(food)
        
        print("\nEscoja el tipo de producto que desea ver:")
        option=input("\n1.Bebidas.\n2.Alimentos.\n>>> ")

        while option!="1" and option!="2":
            option=input("Ingreso inválido, intente nuevamente: ")
        
        if option=="1":
            print("Escoja el tipo de bebida que desea visualizar: ")
            option_b=input("\n1.Alcohólicas.\n2.No alcohólicas.\n>>> ")
            while option_b!="1" and option_b!="2":
                option_b=input("Ingreso inválido, intente nuevamente. ")
            if option_b=="1":
                for i, drink in enumerate(alcoholica):
                    print(f"{i+1}. {drink.name}")

                while True:
                    try:
                        option_c=int(input("Seleccione la bebida que desea visualizar: "))
                        while option_c not in range(len(alcoholica)+1):
                            raise Exception
                        break
                    except:
                        print("Ingreso inválido, intente nuevamente: ")

                alcoholica[option_c-1].show_attr()

            if option_b=="2":
                for i, drink in enumerate(no_alcoholica):
                        print(f"{i+1}. {drink.name}")

                while True:
                    try:
                        option_c=int(input("Seleccione la bebida que desea visualizar: "))
                        while option_c not in range(len(no_alcoholica)+1):
                            raise Exception
                        break
                    except:
                        print("Ingreso inválido, intente nuevamente: ")

                no_alcoholica[option_c-1].show_attr()

        if option=="2":
            print("Escoja el tipo de alimento que desea visualizar: ")
            option_b=input("\n1.Restaurant.\n2.Fast.\n>>> ")

            while option_b!="1" and option_b!="2":
                option_b=input("Ingreso inválido, intente nuevamente. ")

            if option_b=="1":
                for i, food in enumerate(restaurant):
                    print(f"{i+1}. {food.name}")

                while True:
                    try:
                        option_c=int(input("Seleccione la bebida que desea visualizar: "))
                        while option_c not in range(len(restaurant)+1):
                            raise Exception
                        break
                    except:
                        print("Ingreso inválido, intente nuevamente: ")

                restaurant[option_c-1].show_attr()
            
            if option_b=="2":
                for i, food in enumerate(fast):
                    print(f"{i+1}. {food.name}")

                while True:
                    try:
                        option_c=int(input("Seleccione la bebida que desea visualizar: "))
                        while option_c not in range(len(fast)+1):
                            raise Exception
                        break
                    except:
                        print("Ingreso inválido, intente nuevamente: ")

                fast[option_c-1].show_attr()

        
    def search_pro_range(self):
        print("BÚSQUEDA DE PRODUCTOS POR RANGO")
        productos=[]

        for alimento in self.productos_food:
            productos.append(alimento)
        for bebida in self.productos_drinks:
            productos.append(bebida)

        while True:
            try:
                num_1=float(input("Ingrese el primer número del rango de precios en el que desea buscar: "))
                while num_1<0:
                    print("No tenemos productos con precios tan bajos.")
                    raise Exception
                num_2=float(input("Ingrese el segundo número del rango de precios en el que desea buscar: "))
                while num_2<num_1:
                    print("El segundo número debe ser mayor al primero")
                    raise Exception
                break
            except:
                print("Ingreso inválido, intente de nuevo. ")

        products_on_range=[]

        for producto in productos:
            if producto.price>num_1 or producto.price<num_2:
                products_on_range.append(producto)
            else:
                print("No hay existen productos en ese rango de precio")
        
        if len(products_on_range)!=0:
            for i, producto in enumerate(products_on_range):
                print(f"{i+1}. {producto.name}")
            
            op=input("Seleccione el producto que desea ver: ")
            while not op.isnumeric() or int(op) not in range(len(products_on_range)+1):
                op=input("Ingreso inválido, intente nuevamente.")

            products_on_range[int(op)-1].show_attr()


    def search_pro(self):
        while True:
            print("\n🧑‍🍳 BUSQUEDA DE PRODUCTOS DE LOS RESTAURANTES 🧑‍🍳\n")
            option=input("1.Búsqueda de productos por nombre.\n2.Búsqueda de productos por tipo.\n3.Búsqueda de productos por rango de precio.\n4.Volver.\n>>> ")

            while not option.isnumeric() or int(option) not in range(1,5):
                option=input("Ingreso inválido, intente nuevamente: ")
            
            if option=="1":
                self.search_pro_name()
            elif option=="2":
                self.search_pro_type()
            elif option=="3":
                self.search_pro_range()
            elif option=="4":
                break

#MODULO 5

    def restaurant_management(self):
        print("MODULO DE VENTA DE RESTAURANTES")

        for restaurant in self.restaruants:
            print(restaurant)

        dni=input("Ingrese su cedula: ")
        while not dni.isnumeric():
            dni=input("Ingreso no valido, intente de nuevo: ")
        
        for client in self.vip:
            if dni==client.dni:
                client_=client
            else:
                print("No se encontró en la lista de clientes VIP")

        products=[]
        for restaurant in self.restaurants:
            if client_.race==restaurant.race_name:
                if client_.age>18:
                    products.append()
                restaurant_=restaurant

        for food in self.productos_food:
            if restaurant_.nombre==food.restaurant:
                products.append(food)
        
        for drink in self.drinks:
            if restaurant_.nombre==drink.restaurant:
                if client_.age<18:
                    if drink.drink_type=="NO":
                        products.append(drink)
                else:
                    products.append(drink)
            
        
        for i, producto in enumerate(products):
            print(f"PRODUCTO NÚMEOR {i+1}.\n{producto.name}: ${producto.price}")
        
        continuar=input("¿Dese agregar un producto a su carrito?\n1.Si.\n2.No.\n>>> ")
        while continuar!="1" and continuar!="2":
            continuar=("Ingrese una de las opciones numéricas indicadas: ")
        
        car=[]
        costos=[]
        while continuar=="1":

            op=input("Ingrese el producto que desea: ")
            while not op.isnumeric() or int(op) not in range(len(products)):
                op=input("Esa opción de producto no existe.")
            
            producto=products[int(op)-1]
            costos.append(producto.price)

            car.append(producto)


            continuar=input("¿Dese agregar otro producto a su carrito?\n1.Si.\n2.No.\n>>> ")

        
        #NUMERO PERFECTO #TODO
        divisores=[]

        for n in range(1, dni):
            if dni%n==0:
                divisores.append(n)
        
        if sum(divisores)==dni:
            perfecto=True
        else:
            perfecto=False
        
        #SUBTOTAL
        subtotal=sum(costos)

        #DESCUENTO
        if perfecto==True:
            descuento=subtotal*0.15
        
        #TOTAL
        total=subtotal-(descuento)

        print("TOTAL")
        for i, product in enumerate(car):
            print(f"{i+1}. {product.name}")
        print(f"SUBTOTAL={subtotal}\nDESCUENTO={descuento}\nTOTAL= {total}")

        proceder=input('¿Dese proceder con su compra?\n1.Si\n2.No.\n>>> ')
        while proceder!="1" and proceder!="2":
            proceder=input('Ingrese un valor numérico de las opciones: ')
        
        if proceder=="1":
            print("PAGO EXITOSO✅")
            print("")
            print("RESUMEN DE COMPRA")
            for i, product in enumerate(car):
                print(f"{i+1}. {product.name} {product.price}")
            
            print(f"SUBTOTAL={subtotal}\nDESCUENTO={descuento}\nTOTAL= {total}")
        
        factura= Factura(dni,client_.name,car,subtotal,perfecto,descuento,total)
            




        





        


            

        



        



        


        
