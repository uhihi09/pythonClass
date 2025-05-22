class Car:
    def __init__(self,displ,drv):
        self.displ = displ
        self.drv = drv
    
    def info(self):
        print(f"자동차 정보{self.displ},{self.drv}")

car_obj = Car(3000,'4륜')
car_obj.Info()