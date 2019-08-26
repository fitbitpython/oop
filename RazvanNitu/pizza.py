import datetime
from datetime import date


class Pizza:

    nr_of_pizzamade = 0
    default_ingredients = ['mozarella','sos_rosii']
    blaturi = {"Subtire":24,"Normal":22,"Pufos":20,}
    dimensiuni = {"Mare":1.3,"Mic":1}
    ingrediente_pizza_default = {"Quatro_Stagione":['peperoni','sunca','masline','ciuperci'],
                                 "Prosciuto_Fungi":['prosciuto','funghi'],
                                 "Quatro_Formagi":['branza','branza','branza','branza'],
                                 "Suprema":['sunca','bacon','ananas','porumb','broclli']
                                 }


    def __init__(self, blat,dimensiune,toppings,name):
        self.blat = blat
        self.dimensiune = dimensiune
        self.ingrediente = Pizza.default_ingredients.copy()
        self.addtoping(toppings)
        self.name=name
        self.set_price()
        Pizza.nr_of_pizzamade += 1

    @classmethod
    def pizza_default(cls,nume_pizza,dimensiune,blat):

        if nume_pizza in Pizza.ingrediente_pizza_default:
            ingrediente = Pizza.ingrediente_pizza_default[nume_pizza]
        else:
            print('Nu avem acest tip de pizza')
        pret = (Pizza.blaturi[blat]*Pizza.dimensiuni[dimensiune] + (2*len(Pizza.ingrediente_pizza_default[nume_pizza]))) * Pizza.weekday_price()
        print('Detalii',pret,dimensiune,ingrediente,nume_pizza)

    def set_price(self):

        if self.blat in Pizza.blaturi:
            pret_blat = Pizza.blaturi[self.blat]
        else:
            pret_blat = Pizza.blaturi["Normal"]

        if self.dimensiune in Pizza.dimensiuni:
            pret_dimensiune=Pizza.dimensiuni[self.dimensiune]
        else:
            pret_dimensiune=Pizza.dimensiuni["Mic"]

        if len(self.ingrediente) <= 2:
            pret_ingrediente = 0
        else:
            pret_ingrediente = 2 * (len(self.ingrediente)-2)

        self.pret = (pret_blat * pret_dimensiune + pret_ingrediente) * Pizza.weekday_price()

    @property
    def get_price(self):
        return(self.pret)

    @property
    def getdescription(self):
        return(self.name, self.blat,self.dimensiune,self.ingrediente,self.pret)

    def addtoping(self,topping):
        self.ingrediente.extend(topping)
        self.set_price()

    def removetopings(self,toping):
        for x in toping:
            print(x)
            try:
                self.ingrediente.remove(x)
            except:
                print('Topingul',x,'nu se afla pe pizza!')
        self.set_price()

    def removealltoppings(self):
        self.ingrediente=Pizza.default_ingredients.copy()
        self.set_price()

    @staticmethod
    def weekday_price():
        day = date.today()
        day1 = day.weekday()
        if day1 == 6:
            coeficient = 1.1
        elif day1 == 1:
            coeficient = 0.8
        else:
            coeficient = 1
        return(coeficient)


pizza1 = Pizza('Subtire', 'Mare', ['x', 'y', 'z'],'margherita')
#pizza1.getdescription()
#pizza1.addtoping(['sunca', 'carnati', 'porumb'])
#pizza1.calculatorpizza()
#pizza1.getdescription()
#pizza1.removealltoppings()
#pizza1.getdescription()
pizza3=Pizza.pizza_default('Quatro_Stagione','Mare','Pufos')
pizza4=Pizza.pizza_default('Quatro_Formagi','Mare','Pufos')
pizza4=Pizza.pizza_default('Suprema','Mare','Pufos')

print('Descriere',pizza1.getdescription)





#day1=date.today()
#day = day1.weekday()
#print(day)

#pizza1.weekday(date.today())

#pizza3.weekday(day)















