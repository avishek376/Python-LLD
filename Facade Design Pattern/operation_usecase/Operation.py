from Sensor import Sensor
from Lights import Lights
from Smoke import Smoke


class Client:
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


if __name__ == '__main__':
    client = Client()
    client.emergency(True)
    client.emergency(False)
