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