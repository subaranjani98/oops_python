#Question:1

import math
class circle:


    def __init__(self,list):
       self.list = list

    def area1(self):
       area =[math.pi * r**2 for r in self.list]
       return area

    def circumference1(self):
        circumference =[2 * math.pi * r for r in self.list]
        return circumference

list = [10,501,22,37,100,999,87,351]

output = circle(list)
stage1 = output.area1()
print(f"area:{stage1}")
stage2 = output.circumference1()
print(f"circumference:{stage2}")




#Output :
# area:[314.1592653589793, 788542.8976436916, 1520.53084433746, 4300.840342764427, 31415.926535897932, 3135312.609875267, 23778.714795021144, 387047.3565149161]
# circumference:[62.83185307179586, 3147.8758388969727, 138.23007675795088, 232.4778563656447, 628.3185307179587, 6276.9021218724065, 546.637121724624, 2205.398042820035]

#Question:2

class circle:
    _pi =3.141

    def __init__(self,list):
       self.list = list

    def area1(self):
       area =[self._pi * r**2 for r in self.list]
       return area

    def circumference1(self):
        circumference =[2 * self._pi * r for r in self.list]
        return circumference

list = [10,501,22,37,100,999,87,351]

output = circle(list)
stage1 = output.area1()
print(f"area:{stage1}")
stage2 = output.circumference1()
print(f"circumference:{stage2}")



#Output:
# area:[314.1, 788394.1410000001, 1520.244, 4300.029, 31410.0, 3134721.141, 23774.229, 386974.341]
# circumference:[62.82, 3147.282, 138.204, 232.434, 628.2, 6275.718, 546.534, 2204.982]

#Question:3

class Circle:
    _pi= 3.141

    def __init__(self,r):
        self.r = r

    @classmethod
    def area1(self,r):
        return self._pi * r**2

    @classmethod
    def perimeter1(self,r):
        return 2 * self._pi *r


list1 = [10,501,22,37,100,999,87,351]

for r in list1:
    area = Circle.area1(r)
    perimeter = Circle.perimeter1(r)
    print(f"area:{area}")
    print(f"perimeter:{perimeter}")


#Question:4

##  TV class:

# TVClass - Base class
# LedTV class
# PlasmaTV class

# Part - A

#(1) Create a TV class with properties like brand, channel , price , inches , OnOFF status and volume. Specify brand in a constructor parameter. Channel should be 1 by default. Volume should be 50 by default.

#(2) Add methods to increase and decrease volume. Volume can't never be below 0 or above 100.

#(3) Add a method to set the channel. Let's say the TV has only 50 channels so if you try to set channel 60 the TV will stay at the current channel.

#(4) Add a method to reset TV so it goes back to channel 1 and volume 50. (Hint: consider using it from the constructor).

#(5) It's useful to write a status that returns info about the TV status like: "Panasonic at channel 8, volume 75".

# Part - B :

class TV:

    def __init__(self,brand,channel,price,inches,volume):
        self.brand = brand
        self.channel = channel
        self.price = price
        self.inches = inches
        self.volume = volume


    def increasevolume(self):
        if self.volume < 100:
            self.volume += 1


    def decereasevolume(self):
        if self.volume > 0:
            self.volume -= 1


    def setchannel(self,channel):
        if 1<= channel <= 50:
            self.channel = channel


    def resettv(self):
        self.channel = 1
        self.volume = 50


    def status(self):
        return f"{self.brand}at channel{self.channel},volume{self.volume}"

class LEDTV:

    def __init__(self,brand,channel,price,inches,volume):
        self.brand = brand
        self.channel = channel
        self.price = price
        self.inches = inches
        self.volume = volume


    def increasevolume(self):
        if self.volume < 100:
            self.volume += 1


    def decereasevolume(self):
        if self.volume > 0:
            self.volume -= 1


    def setchannel(self,channel):
        if 1<= channel <= 50:
            self.channel = channel


    def resettv(self):
        self.channel = 1
        self.volume = 50


    def status(self):
        return f"{self.brand}at channel{self.channel},volume{self.volume}"

class PlasmaTV:

    def __init__(self,brand,channel,price,inches,volume):
        self.brand = brand
        self.channel = channel
        self.price = price
        self.inches = inches
        self.volume = volume


    def increasevolume(self):
        if self.volume < 100:
            self.volume += 1


    def decereasevolume(self):
        if self.volume > 0:
            self.volume -= 1


    def setchannel(self,channel):
        if 1<= channel <= 50:
            self.channel = channel


    def resettv(self):
        self.channel = 1
        self.volume = 50


    def status(self):
        return f"{self.brand}at channel{self.channel},volume{self.volume}"

#LEDTV:

class LEDTV:
    def __init(self,screenthickness,energyusage,lifespan,refreshrate):
        self.screenthickness = screenthickness
        self.energyusage = energyusage
        self.lifespan = lifespan
        self.refreshrate = refreshrate

    def viewingangel(self,angel):
        if 180<= angel <= 90:
            self.angel =angel


    def backlight1(self,light):
        self.light = 'pink'


    def displayquality(self,rating):
        self.rating = 'UHD'

    def displaydetail1(self):
        return f"{self.screenthickness}{self.displayquality}"

    # def energyusage(self,currentinvolts):
    #     if 40 <=currentinvolts<=20:
    #       self.currentinvolts =currentinvolts

    def detailedfeatureofTV(self):
        return f"display{self.displaydetail1()},thickness {self.screenthickness},light{self.backlight1},angel{self.viewingangel()},currentconsuption{self.energyusage},durablitytime{self.lifespan},frequency{self.refreshrate}"




#PlasmaTV:


class PlasmaTV:
    def __init(self,screenthickness,energyusage,lifespan,refreshrate):
        self.screenthickness = screenthickness
        self.energyusage = energyusage
        self.lifespan = lifespan
        self.refreshrate = refreshrate

    def viewingangel(self,angel):
        if 180<= angel <= 90:
            self.angel =angel


    def backlight1(self,light):
        self.light = 'pink'


    def displayquality(self,rating):
        self.rating = 'UHD'

    def displaydetail1(self):
        return f"{self.screenthickness}{self.displayquality}"

    # def energyusage(self,currentinvolts):
    #     if 40 <=currentinvolts<=20:
    #       self.currentinvolts =currentinvolts

    def detailedfeatureofTV(self):
        return f"display{self.displaydetail1()},thickness {self.screenthickness},light{self.backlight1},angel{self.viewingangel()},currentconsuption{self.energyusage},durablitytime{self.lifespan},frequency{self.refreshrate}"
