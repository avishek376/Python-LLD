from Lights import Lights
from Smoke import Smoke
from Sensor import Sensor


class Operations:
    def __init__(self):
        self._sensor = Sensor()
        self._lights = Lights()
        self._smoke = Smoke()

    def emergency(self, status):
        if status:
            self._sensor.sensorOn()
            self._lights.lightsOn()
            self._smoke.smokeOn()
        else:
            self._sensor.sensorOff()
            self._lights.lightsOff()
            self._smoke.smokeOff()
