class Animal():
    
    def __init__(self,animal_name,species,age,gender):
        self.animal_name = animal_name
        self.species = species
        self.age = age
        self.gender = gender
        self.food = "Unknow"
        
    def eat(self):
        user_input = input(f"Enter habitat for {self.animal_name} (Forest,Water,Home)as(F,W,H): ").lower()
        if user_input == ("forest","F,f"):
            self.food = "Grass","Meat"
        elif user_input == ('w','W',"water"):
            self.food = "fish"
        elif user_input == ('home','h','H'):
            self.food = "Pet Food"
        else:
            self.food = "Anithing"
        return 
    
    def speek(self):
        return f"Animal Speek."
    
    
    def sleep(self):
        return f"Animal is sleeping." 
    
    def animal_details(self):
        return f"""
    
    Animal Name : {self.animal_name}
    Animal Species : {self.species}
    Animal Age : {self.age}
    Animal Gender : {self.gender}
    Animal Eat : {self.eat()}
    Animal Sleep : {self.sleep()}
    Animal Speek : {self.speek()}
    
    """
    
class dog(Animal):
    
    def __init__(self,name,species,age,gender):
        super().__init__(name,species,age,gender)
    
    def speek(self):
        parent_sound = super().speek()
        return  f"Barking: Woof Woof!"
    
    def animal_details(self):
        all = super().animal_details()
        return  all 
    
    
animal1 = Animal("Sheru","Germen Shepherd",5,"M")
animal2 = dog('Tommy','PetBull',3,'M')

print(animal1.animal_details())
print(animal2.animal_details())
