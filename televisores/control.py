class Control:
    def __init__(self):

        self._tv=None
    def enlazar(self,teve):
        self._tv=teve
        self._tv.setControl(self)
    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()
    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown()
    def volumenUp(self):
        self._tv.volumenUp()
    def volumenDown(self):
        self._tv.volumenDown()
    def setCanal(self,chanel):
        self._tv.setCanal(chanel)
    def setVolumen(self, vol):
        self._tv.setVolumen(vol)
    def setTv(self,teve):
        self._tv=teve
    def getTv(self):
        return self._tv