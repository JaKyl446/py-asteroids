import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rnd = random.uniform(20, 50)
        v1 = self.velocity.rotate(rnd)
        v2 = self.velocity.rotate(-rnd)
        r = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, r)
        a2 = Asteroid(self.position.x, self.position.y, r)
        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2
