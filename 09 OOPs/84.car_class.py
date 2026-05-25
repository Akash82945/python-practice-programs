class car():
    
    def __init__(self,brand,model,fuel_type):
        self.brand = brand
        self.model = model
        self.fule_type = fuel_type
        self.__speed = 0
        self.is_start = False
        
        
    def start_engine(self):
        if self.is_start == True:
            # print("Car is allready Start.")
            return True
        else:
            self.is_start = True
            # print("Car is Start.")
            return True
    
      
    def accelerate_car(self,increase):
        if self.is_start == False:
            print("Oops! Engine OFF.")
            user = input("Do you want to Start Engine? yes/no: ").lower()
            if user == "yes":
                self.start_engine = self.start_engine()
            else:
                return False
            # print("Error: Start Car first.")
            # return False
        
        self.__speed = self.__speed + increase
        
        if self.__speed >= 180:
            self.__speed = 180
        else:
            pass# print(f"Speed of car {self.__speed}")
        return True

    def car_break(self):
        if self.__speed > 0:
            self.__speed = 0
            # print("Break apply (Car Stopped.)")
        else:
            # print("Car stopped already.")
            pass
        
        return True
    
    def car_details(self):
        status = "ON" if self.is_start is True else "OFF"
        return f'''
    ===CAR DETIAILS==
    Car Brand : {self.brand}
    Car Model : {self.model}
    Car Fuel_Type : {self.fule_type}
    Car Star or Not : {status}
    Car Speed : {self.__speed} km/h
    '''
    
    
    


class ElectricCar(car):
    def __init__(self,brand,model,fuel_type):
        super().__init__(brand,model,fuel_type)
        self.battery = 100      
          
    def accelerate_car(self, increase):
        if self.battery <= 5:
            return "Battery Low! Please Charge."
        
        success = super().accelerate_car(increase)
        
        if success:
            self.battery = self.battery - 5
            return True
        return False
    
    def car_details(self):
        basic =  super().car_details()
        return basic + f"Battery Life : {self.battery}"



class DesialCar(car):
    
    def __init__(self,brand,model,fuel_type):
        super().__init__(brand,model,fuel_type)
        self.fuel = 100
        
    def accelerate_car(self, increase):
        if self.fuel <= 0:
            self.start_engine == False
            return "NO Fuel!"
        
        tank = super().accelerate_car(increase)
        
        if tank:
            self.fuel = self.fuel - 10
            if self.fuel <= 0:
                self.car_break()
                self.is_start = False
            return True
        return False
        
    def car_details(self):
        normal = super().car_details()
        return normal + f"Fuel In tank : {self.fuel}"





car1 = DesialCar("BMW","BMW 43","Desiol")
car2 = ElectricCar("Audi","AUDI 54", "Elsctric")

# car1.start_engine()
print("===CAR 1 DETAILS===")
while True:
    user_input = input("\nEnter [" "] space to accelerate or Enter[n] to stop :").lower()
    
    if user_input == "n":
        print("Driving Finished")
        break
    else:
        status = car1.accelerate_car(34)
        print(car1.car_details())
        
        if status == "NO Fuel!" or car1.fuel <= 0:
            print("NO Fuel.")
            break


print("\n===CAR 2 DETAILS===")
# car2.start_engine()
while True:
    user_input = input("\nEnter [" "] to accelerate or Enter [q] to stop : ").lower()
    
    if user_input == "q":
        print("Fenished Trip.")
        break
    else:
        status = car2.accelerate_car(54)
        print(car2.car_details())
        if status == "Battery Low! Please Charge." or car2.battery <=5 :
            print("Battery Low.")
            break