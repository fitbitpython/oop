class Pizza:

    nr_of_pizzamade = 0
    default_ingredients = ['mozarella','sos_rosii']
    blaturi = {"Subtire":24,"Normal":22,"Pufos":20,}
    dimensiuni = {"Mare":1.3,"Mic":1}


    def __init__(self, blat,dimensiune,toppings,name):
        self.blat = blat
        self.dimensiune = dimensiune
        self.ingrediente = Pizza.default_ingredients.copy()
        self.addtoping(toppings)
        self.name=name
        self.calculatorpizza()

        Pizza.nr_of_pizzamade+= 1

    def calculatorpizza(self):

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

        self.pret = pret_blat * pret_dimensiune + pret_ingrediente

    def getdescription(self):
        print('Nume',self.name, 'Tip blat:', self.blat,'Dimensiune:', self.dimensiune,'Incrediente:', self.ingrediente,'Pret:', self.pret)

    def addtoping(self,topping):
        self.ingrediente.extend(topping)
        self.calculatorpizza()

    def removetopings(self,toping):
        for x in toping:
            print(x)
            try:
                self.ingrediente.remove(x)
            except:
                print('Topingul',x,'nu se afla pe pizza!')
        self.calculatorpizza()

    def removealltoppings(self):
        self.ingrediente=Pizza.default_ingredients.copy()
        self.calculatorpizza()

pizza1 = Pizza('Subtire', 'Mare', ['x', 'y', 'z'],'margherita')
pizza1.getdescription()
pizza1.addtoping(['sunca', 'carnati', 'porumb'])
#pizza1.calculatorpizza()
pizza1.getdescription()
pizza1.removealltoppings()
pizza1.getdescription()












