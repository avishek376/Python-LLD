from BulletFlyweight import BulletFlyweight


class BulletRegistry:
    bullet_registry = {}

    @staticmethod
    def get_bullet(bullet_type, bullet_image):
        if bullet_type not in BulletRegistry.bullet_registry:
            BulletRegistry.bullet_registry[bullet_type] = BulletFlyweight(bullet_image)
        return BulletRegistry.bullet_registry[bullet_type]
