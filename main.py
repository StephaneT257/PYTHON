class cars: 
    def __init__(self, brand, engine) -> None:
        self.wheels = 4
        self.brand = brand
        self.engine = engine 
        
    def wheelmulti(self):
        self.wheels *= 2 

# brand = input("input car brand")
# engine = input("input car engine")

car1 = cars(brand ="peugot", engine= 4)        

car1.wheelmulti()

print(f"your car is a  {car1.brand} it has {car1.wheels} wheels, and a {car1.engine}l engine" )



