from BulletRegistry import BulletRegistry


class Bullet:
    """This class is the Bullet class, extrinsic data is passed as arguments"""

    def __init__(self, name, bullet_type, bullet_weight, bullet_speed, bullet_damage, bullet_image):
        self._name = name
        self._bullet_type = bullet_type
        self._bullet_weight = bullet_weight
        self._bullet_speed = bullet_speed
        self._bullet_damage = bullet_damage
        self._bullet = BulletRegistry.get_bullet(bullet_type, bullet_image)

    def bullet_description(self):
        return f"Name: {self._name}, Bullet Type: {self._bullet_type}, Bullet Weight: {self._bullet_weight}, Bullet Speed: {self._bullet_speed}, Bullet Damage: {self._bullet_damage}"
