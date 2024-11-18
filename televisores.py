class Marca:
    def __init__(self,nombre):
        self._nombre=nombre
    
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
class TV:
    _numTV=None
    def __init__(self, marca, estado):
        self._marca=marca
        self._estado=estado
        self._canal=1
        self._volumen=1
        self._precio=500
        self._control=None
        self.numTV+=1
    
    def getMarca(self):
        return self.marca
    def setMarca(self,marca):
        self.marca=marca
    def getVolumen(self):
        return self.volumen
    def setVolumen(self,volumen):
        if self._estado==True and (volumen<=7 and volumen >=0):
            self.volumen=volumen
        else:
            return
    def getPrecio(self):
        return self.precio
    def setPrecio(self,price):
        self.precio=price
    def setControl(self,control):
        self.control=control
    def getControl(self):
        return self.control
    def getCanal(self):
        return self.canal
    def setCanal(self,chanel):
        if self._estado==True and (chanel>=1 and chanel<=120):

            self.canal=chanel
        else:
            return
    def setNumTV(self,num):
        self.numTV=num
    def getNumTV(self):
        return self.numTV
    def turnOn(self):
        self._estado=True
    def turnOff(self):
        self._estado=False
    def getEstado(self):
        return self._estado
    def volumenUp(self):
        if self._estado==True and(self._volumen<7):
            self._volumen+=1
        else:
            return
    def volumenDown(self):
        if self._estado==True and (self._volumen>0):
            self._volumen-=1
        else:
            return
    def canalUp(self):
        if self._estado==True and (self._canal<120):
            self._canal+=1
        else:
            return
    def canalDown(self):
        if self._estado==True and (self._canal>1):
            self._canal-=1
        else:
            return
class Control:
    def __init__(self):

        self._tv=None
    def enlazar(self,teve):
        self._tv=teve
        self._tv.setControl(self)
    def turnOn(self):
        self._tv.volumenUp()
    def turnOff(self):
        self._tv.volumenOff()
    def canalUp(self):
        self._tv.volumenUp()
    def canalDown(self):
        self._tv.volumenDown()
    def volumenUp(self):
        self._tv.volumenUp()
    def volumenDown(self):
        self._tv.volumenDown()
    def setCanal(self,chanel):
        self._tv.setCanal(chanel)
    def setVolumen(self, vol):
        self._tv.setVolumen(vol)
    def settv(self,teve):
        self._tv=teve
    def gettv(self):
        return self._tv

