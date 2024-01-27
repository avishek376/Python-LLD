from Bullet import Bullet

if __name__ == "__main__":
    bullets = []
    bullets.append(Bullet("Bullet 1", "Pistol", 10, 100, 10, "Bullet IMG"))
    bullets.append(Bullet("Bullet 2", "Pistol", 10, 100, 10, "Bullet IMG"))
    bullets.append(Bullet("Bullet 3", "Glock", 10, 100, 10, "Bullet IMG"))
    bullets.append(Bullet("Bullet 1", "Dessert Eagle", 10, 100, 10, "Bullet IMG"))

    for bullet in bullets:
        print(bullet.bullet_description())
