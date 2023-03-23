import random
import requests
from Clases.Constructor import Constructor
from Clases.Pilot import Pilot
from Clases.Race import Race
from Clases.Circuit import Circuit
from Clases.ClientGeneral import ClientGeneral as General
from Clases.ClientVIP import ClientVIP as Vip
from Clases.Ticket import Ticket
from Clases.Restaurant import Restaurant
from Clases.ProductDrink import ProductDrink as Drink
from Clases.ProductFood import ProductFood as Food

class AppMA:
    """
    En esta parte, hice dos listas para cada db,
    una es para appendear de forma ordena la info a los .txt
    y la otra es para generar los objetos a partir de los .txt con los que voy a seguir trabajando.
    """
    def __init__(self):
        self.constructors=[]
        self.pilots=[]
        self.races=[]
        self.circuits=[]

        self.aux_constructors=[]
        self.aux_pilots=[]
        self.aux_races=[]
        self.aux_circuits=[]
    
    #LISTAS MODULO II
        self.entradas=[]
        self.general=[]
        self.vip=[]

        self.aux_entradas=[]
        
    #LISTAS MODULO IV
        self.restaurants=[]
        self.productos_food=[]
        self.productos_drinks=[]
        self.productos=[]

        self.aux_restaurants=[]

    def load_data(self):

        """
        Aquí bajo la info de las API
        """

        url_constructores='https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/constructors.json'
        response_c=requests.request("GET", url_constructores)

        url_pilots='https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json'
        response_p=requests.request("GET", url_pilots)

        url_races='https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json'
        response_r=requests.request("GET", url_races)

        """
        Appendeo la info de las API a las listas auxiliares.
        """
        self.aux_constructors= []
        for c in response_c.json():
            x=[]
            for p in response_p.json():
                if c["id"]==p["team"]:
                    x.append(p["firstName"])
            constructor= Constructor(c["name"], c["id"], c["nationality"],x)
            self.aux_constructors.append(constructor)

        self.aux_pilots= []
        for i in response_p.json():
            piloto= Pilot (i["firstName"], i["lastName"], i["dateOfBirth"], i["nationality"], i["permanentNumber"], i["team"])
            self.aux_pilots.append(piloto)
        
        self.aux_races= []
        for i in response_r.json():
            race= Race (i["name"], i["round"], i["date"], i["circuit"]["name"], {}, False) #FALTA PODIUM
            self.aux_races.append(race)
            circuit= Circuit(i["circuit"]["name"],i["circuit"]["location"]["country"], i["circuit"]["location"]["locality"],i["circuit"]["location"]["lat"], i["circuit"]["location"]["long"])
            self.aux_circuits.append(circuit)
        
        #LISTAS AUXILIARES MODULO II
        self.aux_entradas= []
        for carrera in response_r.json():
            entrada= Ticket(carrera["name"],carrera["map"]["general"][0]*carrera["map"]["general"][1],carrera["map"]["vip"][0]*carrera["map"]["vip"][1])
            self.aux_entradas.append(entrada)
        
        #LISTAS AUXILIARES MODULO IV
        
        with open("c:/Users/ivana/OneDrive/Documentos/Universidad/II Trimestre/Algoritmos y Programación/PROYECTO/TXT/Modulo IV/Restaurant.txt","w") as f:
            for restaurant in response_r.json():
                res=restaurant["name"]
                for r in restaurant["restaurants"]:
                    x=''
                    y=r["name"]
                    for i in r["items"]:
                        x+=f'{i["name"]}-'
                    
                    f.write(f"{y}|{res}|{x}|\n")
        
        with open("c:/Users/ivana/OneDrive/Documentos/Universidad/II Trimestre/Algoritmos y Programación/PROYECTO/TXT/Modulo IV/ProductDrink.txt","w") as f:
            for race in response_r.json():
                for restaurant in race["restaurants"]:
                    res=restaurant["name"]
                    for drink in restaurant["items"]:
                        if drink["type"]=="drink:alcoholic":
                            f.write(f'{drink["name"]}|{drink["price"]}|{res}|SI|\n')
                        elif drink["type"]=="drink:not-alcoholic":
                            f.write(f'{drink["name"]}|{drink["price"]}|{res}|NO|\n')

        with open("c:/Users/ivana/OneDrive/Documentos/Universidad/II Trimestre/Algoritmos y Programación/PROYECTO/TXT/Modulo IV/ProductFood.txt","w") as f:
            for race in response_r.json():
                for restaurant in race["restaurants"]:
                    res=restaurant["name"]
                    for food in restaurant["items"]:
                        if food["type"]=="food:restaurant":
                            f.write(f'{food["name"]}|{food["price"]}|{res}|Restaurant|\n')
                        elif food["type"]=="food:fast":
                            f.write(f'{food["name"]}|{food["price"]}|{res}|Fast|\n')

        """
        Llevo la info de las listas auxiliares a los .txt.
        """
    def from_api_to_txt(self):
        directory="c:/Users/ivana/OneDrive/Documentos/Universidad/II Trimestre/Algoritmos y Programación/PROYECTO/TXT/Modulo I/"

        file_name_cons="Constructor.txt"
        with open(directory+file_name_cons, "w") as f:
            for constructor in self.aux_constructors:
                f.write(f"{constructor.constructor_name},{constructor.constructor_id},{constructor.constructor_nationality},{constructor.constructor_pilots[0]},{constructor.constructor_pilots[1]},\n")
                
        file_name_p="Pilot.txt"
        with open(directory+file_name_p, "w") as f:
            for pilot in self.aux_pilots:
                f.write(f"{pilot.pilot_name},{pilot.pilot_last_name},{pilot.pilot_birth_date},{pilot.pilot_birth_place},{pilot.pilot_number},{pilot.pilot_team},\n")
        
        filen_name_r="Race.txt"
        with open(directory+filen_name_r,"w") as f:
            for race in self.aux_races:
                f.write(f"{race.race_name},{race.race_number},{race.race_date},{race.race_circuit},{race.race_podium},{race.race_end},\n")#FALTA PODIUM
        
        file_name_cir="Circuit.txt"
        with open(directory+file_name_cir, "w") as f:
            for circuit in self.aux_circuits:
                f.write(f"{circuit.circuit_name},{circuit.circuit_country},{circuit.circuit_locality},{circuit.circuit_lat},{circuit.circuit_long},\n")
        
        #.TXT MODULO II 
        directory="c:/Users/ivana/OneDrive/Documentos/Universidad/II Trimestre/Algoritmos y Programación/PROYECTO/TXT/Modulo II/"

        file_name="Ticket.txt"
        with open(directory+file_name, "w") as f:
            for entrada in self.aux_entradas:
                f.write(f"{entrada.race_name}, {entrada.general}, {entrada.vip},\n")
        
    
    """
    Llevo la info de los .txt a las listas de objetos que seguiré usando.
    """
    def read_files(self):
        directory="c:/Users/ivana/OneDrive/Documentos/Universidad/II Trimestre/Algoritmos y Programación/PROYECTO/TXT/Modulo I/"
        
        self.constructors= []
        file_name_cons="Constructor.txt"
        with open(directory+file_name_cons) as f:
            for line in f:
                x=[line.split(",")[3],line.split(",")[4]]
                constructor= Constructor(line.split(",")[0],line.split(",")[1],line.split(",")[2],x)
                self.constructors.append(constructor)

        self.pilots= []
        file_name_p="Pilot.txt"
        with open(directory+file_name_p) as f:
            for line in f:
                pilot= Pilot(line.split(",")[0],line.split(",")[1],line.split(",")[2],line.split(",")[3],line.split(",")[4], line.split(",")[5])
                self.pilots.append(pilot)
                

        self.races= []
        file_name_r="Race.txt"
        with open(directory+file_name_r) as f:
            for line in f:
                if line.split(",")[5]=="True":
                    x=True
                else:
                    x=False

                race= Race(line.split(",")[0],line.split(",")[1],line.split(",")[2],line.split(",")[3],line.split(",")[4],x)
                self.races.append(race)
                
        
        self.circuits= []
        file_name_cir='Circuit.txt'
        with open(directory+file_name_cir) as f:
            for line in f:
                circuit= Circuit(line.split(",")[0],line.split(",")[1],line.split(",")[2],line.split(",")[3],line.split(",")[4])
                self.circuits.append(circuit)

        #MODULO II
        directory="c:/Users/ivana/OneDrive/Documentos/Universidad/II Trimestre/Algoritmos y Programación/PROYECTO/TXT/Modulo II/"
        
        self.entradas= []
        file_name="Ticket.txt"
        with open(directory+file_name) as f:
            for line in f:
                x=int(line.split(",")[1])
                y=int(line.split(",")[2])
                entrada= Ticket(line.split(",")[0],x,y)
                self.entradas.append(entrada)
        
        #MODULO IV
 
        self.productos=[]
        self.productos_drinks=[]
        with open("c:/Users/ivana/OneDrive/Documentos/Universidad/II Trimestre/Algoritmos y Programación/PROYECTO/TXT/Modulo IV/ProductDrink.txt") as f:
            for line in f:
                drink= Drink(line.split("|")[0],float(line.split("|")[1]),line.split("|")[2],line.split("|")[3])
                self.productos_drinks.append(drink)
                self.productos.append(drink)
        
        self.productos_food=[]
        with open("c:/Users/ivana/OneDrive/Documentos/Universidad/II Trimestre/Algoritmos y Programación/PROYECTO/TXT/Modulo IV/ProductFood.txt") as f:
            for line in f:
                food= Food(line.split("|")[0],float(line.split("|")[1]),line.split("|")[2],line.split("|")[3])
                self.productos_food.append(food)
                self.productos.append(food)

        self.restaurants=[]
        with open("c:/Users/ivana/OneDrive/Documentos/Universidad/II Trimestre/Algoritmos y Programación/PROYECTO/TXT/Modulo IV/Restaurant.txt") as f:
            for line in f:
                x=[]
                x.append(line.split("|")[2].split("-"))

            

                    

                restaurant= Restaurant(line.split("|")[0],line.split("|")[1],x)
                self.restaurants.append(restaurant)

        for restaurante in self.restaurants:
            print(restaurante.products)
    

        """En esta funcion genero la busqueda de constructores por país de origen.
        """
    def finish_race(self): 

        with open("c:/Users/ivana/OneDrive/Documentos/Universidad/II Trimestre/Algoritmos y Programación/PROYECTO/TXT/Modulo I/Race.txt") as f:
            for line in f:
                if line.split(",")[5]=="False":
                    for race in self.aux_races:
                        if line.split(",")[0]==race.race_name:

                                print(f"\nLa siguiente carrera es: {race.race_name}. ¿La quieres terminar?")
                                option=input("1. Finalizar carrera.\n2. Finalizar siguiente carrera.\n3. Volver.\n>>> ")

                                while option!="1" and option!="2" and option!="3":
                                    option=input("ERRROR: Ingreso inválido, intente nuevamente: ")

                                if option=="1":
                                    race.race_end=True


                                    pilots=self.pilots
                                    random.shuffle(pilots)
                                    podium_=pilots[0:10]

                                    podium=""

                                    print("\nGANADORES\n")
                                    for i, pilot in enumerate(podium_):
                                        print(f"{i+1}. {pilot.pilot_name} {pilot.pilot_last_name}")
                                        
                                    self.from_api_to_txt()
                                    self.read_files()

                                elif option=="3":
                                    break
                                

    def search_constructors_by_country(self):#LISTO
        print("Buscar constructores por país.")
        """Cree una lista para mostrar las nacionalidades de los constructores numeradas.
        """
        countries=[]
        for constructor in self.constructors:
            countries.append(constructor.constructor_nationality)
        """Saque los países que se repetian convirtiendo la lista en un set y luego nuevamente en una lista, y las ordené por orden alfabético.
        """

        countries=list(set(countries))
        countries.sort()
        """Imprimo la lista y pido un input para seleccionar los equipos que se desean visualizar.
        """
        print("")
        print("Selecciona la nacionalidad del constructor que estas buscando:\n")
        for i, country in enumerate(countries):
            print(f'{i+1}. {country} teams.')
        while True:
            try:
                country=int(input(">>> "))
                while not country in range(1, len(countries)+1):
                    raise Exception
                break
            except:
                print("ERROR: Ingreso iválido, intente nuevamene: ")

        """Generé una lista para guardar los equipos del país seleccionado, ya que hay algunos países con más de un equipo.
        """
        teams=[]        
        for constructor in self.constructors:
            if constructor.constructor_nationality==countries[country-1]:
                teams.append(constructor)

        """Pido un input para seleccionar el equipo que se desea visualizar en caso de que en la lista haya más de un equipo.
        """
        if len(teams)>1:
            print("Seleccione el equipo: ")
            for i, team in enumerate(teams):
                print(f'{i+1}. {team.constructor_name}')
            while True:
                try:
                    x=int(input(">>> "))
                    while not x in range(1,len(teams)+1):
                        raise Exception
                    break
                except:
                    print("ERROR: Ingreso inválido intente nuevamente: ")
            teams[x-1].show_attr()
        else:
            teams[0].show_attr()
    
    def search_pilots_by_constructor(self): #TODO NO LISTO
        print("Buscar a los pilotos por constructor.")
        
        """MUESTRO DE FORMA NUMERADA EL NOMBRE DE CADA CONSTRUCTOR.
        """
        for i, t in enumerate(self.constructors):
            print(f'{i+1}. {t.constructor_name}.')
        while True:
            try:
                t=int(input(">>> "))
                while not t in range(1, len(self.constructors)+1):
                    raise Exception
                break
            except:
                print("ERROR: Ingreso inválido, intente de nuevo: ")
        
        """MUESTRO LOS ATRIBUTOS DEL PILOTO SELECCIONADO.
        """
        equipo=(self.constructors[t-1].constructor_id)
        print(equipo)

        for pilot in self.pilots:
            if equipo==pilot.pilot_team:
                pilot.show_attr()
        
    def race_by_circuit_country(self): #LISTO

        countries=[]
        for pais in self.circuits:
            countries.append(pais.circuit_country)
        
        for country in countries:
            print(country)

        countries=list(set(countries))
        
        countries.sort()

        print("Escoja el pais cuyas carreras desea visualizar: ")
        for i, p in enumerate(countries):
            print(f'{i+1}. {p}.')
        while True:
            try:
                p=int(input(">>> "))
                while not p in range(1,len(self.circuits)+1):
                    raise Exception
                break
            except:
                print("ERROR: El ingreso ha sido inválido, intente nuevamente: ")
        
        pais=countries[p-1]

        circuitos=[]

        for circuit in self.circuits:
            if pais==circuit.circuit_country:
                circuitos.append(circuit.circuit_name)
        
        for i, circuito in enumerate(circuitos):
            for circuit in self.circuits:    
                if circuitos[0]==circuit.circuit_name:
                    circuit.show_attr()
                
        
    def race_by_month(self): #LISTO
        print("Busqueda de carrera por mes: \n")
        while True:
            try:
                mes=input("Ingrese el mes de la carrera que buscar: ")
                while not mes.isnumeric():
                    raise Exception
                while int(mes) not in range(1,13):
                    raise Exception
                while len(mes)!=2:
                    raise Exception
                break
            except:
                print("Error, ingreso inválido.\nEjemplo de ingreso:\nSi el mes es julio el input es 07.\n ")
        
        x=False

        for race in self.races:
            if race.race_date.split("-")[1]== mes:
                x=True
                race.show_attr()

        if x==False:
            print("En este mes no hay carreras.")

    
    def search_race(self):
        while True:
            print("")
            print("BUSQUEDA DE CARRERAS🔍")
            x=input("1. Buscar los constructores por país.\n2. Buscar los pilotos por constructor.\n3. Buscar a las carreras por país del circuito.\n4. Buscar todas las carreras que ocurran en un mes.\n5. Volver.\n>>> ")
            while not x.isnumeric() or int(x) not in range(1,6):
                x=input("Ingreso inválido intente nuevamente: ")
           
            if x=="1":
                self.search_constructors_by_country()
            elif x=="2":
                self.search_pilots_by_constructor()
            elif x=="3":
                self.race_by_circuit_country()
            elif x=="4":
                self.race_by_month()
            elif x=="5":
                break

    def race_team_management(self):
        while True:
            print("\n🏁MÓDULO DE GESTIÓN DE CARRERAS Y EQUIPOS🏁")
            option=input("1. Búsqueda de carreras.\n2. Finalizar carrera.\n3. Volver.\n>>> ")

            while not option.isnumeric() or int(option) not in range(1,4):
                option=input("Ingreso inválido intente nuevamente: ")

            if option=="1":
                self.search_race()
            elif option=="2":
                self.finish_race()
            else:
                break
#MODULO 2######################################################################################################################################
    def regisgter(self): #todo restar entradas de tiket

        print("\nSelecciones la carrera a la que desea asistir: ")
        for i, race in enumerate(self.races):
            print(f"{i+1}. {race.race_name}")

        option=input(">>> ")
        while not option.isnumeric() or int(option) not in range(len(self.races)+1):
            option=("ERROR: Ingreso inválido, intente nuevamente: ")
        
        option=int(option)
        option-=1

        carrera=self.entradas[option].race_name
        print(carrera)

        for race in self.races:
            if race.race_name==carrera:
                if race.race_end==True:
                    print("Es carrera ya finalizó, no puede comprar más entradas.")
                else:
                    tipo=input("Ingrese el tipo de entradad que desea (G)eneral o (V)IP: ").capitalize()
                    while tipo!="G" and tipo!="V":
                        tipo=input("Ingreso inválido, escribe la letra G si desea una entrada general o la letra V si desea una entrada VIP: ")
                    if tipo=="G":
                        print(f"El número de entradas disponibles es de: {self.entradas[option].general}")
                        if self.entradas[option].general==0:
                            print("Lo sentimos, no hay entradas generales disponibles.")
                            break
                        else:
                            num_entrada=input("Ingrese el número de entradas que desea: ")
                            while not num_entrada.isnumeric() or int(num_entrada) not in range(self.entradas[option].general): #####
                                num_entrada=input("El número de entradas se sale del rango de entradas disponibles, intente nuevamente: ")
                            for i in range(int(num_entrada)):
                                nombre=input("Ingrese su nombre: ")
                                cedula=input("Ingrese su número de cédula: ")
                                while not cedula.isnumeric():
                                    cedula=input("Ingreso inválido, intente nuevamente: ")
                                #ONDULADO
                                cedula=int(cedula)
                                ondulado=False
                                if len(str(cedula))<3:
                                    ondulado=True
                                elif (len(str(cedula))%2==0):
                                    str_id= str(cedula)[0:2]
                                    if (cedula%int(str_id))==0:
                                        ondulado=True
                                else:
                                    str_id=str(cedula)[0:2]
                                    new_str_id= str(id)+str_id[1]
                                    if(int(new_str_id)) % int(str_id)==0:
                                        ondulado=True

                                edad=input("Ingrese su edad: ")###########################
                                while not edad.isnumeric() or int(edad)<0:
                                    edad=input("Ingreso inválido, intente nuevamente: ")
                                
                                #VALIDAR COMPRA FINAL
                                validar=input("Desea continuar con su compra: (S)í, (N)o: ").capitalize()
                                while validar!="S" and validar!="N":
                                    validar=input("Ingreso inválido, escriba N para no y S para sí: ")
                                
                                if validar=="S":
                                    cliente= General(nombre,cedula,edad,carrera,ondulado,i,False)
                                    self.general.append(cliente)
    
                    elif tipo=="V":
                        print(f"El número de entradas disponibles es de: {self.entradas[option].vip}")
                        if self.entradas[option].vip==0:
                            print("Lo sentimos, no hay entradas generales disponibles.")
                            break
                        else:
                            num_entrada=input("Ingrese el número de entradas que desea: ")
                            while not num_entrada.isnumeric() or int(num_entrada) not in range(self.entradas[option].general): #####
                                num_entrada=input("El número de entradas se sale del rango de entradas disponibles, intente nuevamente: ")
                            for i in range(int(num_entrada)):
                                nombre=input("Ingrese su nombre: ")
                                cedula=input("Ingrese su número de cédula: ")
                                while not cedula.isnumeric():
                                    cedula=input("Ingreso inválido, intente nuevamente: ")

                                #ONDULADO
                                cedula=int(cedula)
                                ondulado=False
                                if len(str(cedula))<3:
                                    ondulado=True
                                elif (len(str(cedula))%2==0):
                                    str_id= str(cedula)[0:2]
                                    if (cedula%int(str_id))==0:
                                        ondulado=True
                                else:
                                    str_id=str(cedula)[0:2]
                                    new_str_id= str(id)+str_id[1]
                                    if(int(new_str_id)) % int(str_id)==0:
                                        ondulado=True

                                edad=input("Ingrese su edad: ")
                                while not edad.isnumeric() or int(edad)<0:
                                    edad=input("Ingreso inválido, intente nuevamente: ")
                                
                                #VALIDAR COMPRA FINAL
                                validar=input("Desea continuar con su compra: (S)í, (N)o: ").capitalize()
                                while validar!="S" and validar!="N":
                                    validar=input("Ingreso inválido, escriba N para no y S para sí: ")
                                
                                if validar=="S":

                                    cliente= Vip(nombre,cedula,edad,carrera,ondulado,i, False)
                                    self.vip.append(cliente)

        

        with open("c:/Users/ivana/OneDrive/Documentos/Universidad/II Trimestre/Algoritmos y Programación/PROYECTO/TXT/Modulo II/ClientGeneral.txt") as f:
            for entrada in self.general:
                f.write(f"{entrada.name},{entrada.dni},{entrada.age},{entrada.race},{entrada.ondulado},{entrada.n_ticket},{entrada.validado},\n")
        
        with open("c:/Users/ivana/OneDrive/Documentos/Universidad/II Trimestre/Algoritmos y Programación/PROYECTO/TXT/Modulo II/ClientVIP.txt") as f:
            for entrada in self.vip:
                f.write(f"{entrada.name},{entrada.dni},{entrada.age},{entrada.race},{entrada.ondulado},{entrada.n_ticket},{entrada.validado},\n")
#MODULO 3#######################################################################################################################################
    def validar_entradas(self):
        pass
#MODULO 4#######################################################################################################################################
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
