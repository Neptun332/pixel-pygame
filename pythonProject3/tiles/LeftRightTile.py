from Directions import Directions
from tiles.MovingTile import MovingTile
from utils.semirandom import randint


class LeftRightTile(MovingTile):
    NAME = "Sand"

    POSSIBLE_MOVEMENT = (Directions.LEFT, Directions.RIGHT)

    def __init__(self, x: int, y: int, world: 'World', velocity):
        super().__init__(
            color=(235 + randint(20), 0 + randint(20), 0 + randint(40)),
            x=x,
            y=y,
            world=world,
            velocity=velocity
        )
        self.current_direction = Directions.LEFT
        self.next_direction = Directions.RIGHT

    def update(self):
        if self.position_should_be_updated and self.active:
            self.color = (255, 0, 0)
            next_position = self.get_next_position(self.current_direction, self.velocity)
            if not self.world.is_position_inside_scene(*next_position):
                self.switch_direction()
                next_position = self.get_next_position(self.current_direction, self.velocity)

            empty_position = self.world.get_tile_at_position(*next_position)
            # if empty_position:
            self.move_to_position(next_position)

    def switch_direction(self):
        temp = self.current_direction
        self.current_direction = self.next_direction
        self.next_direction = temp

    def step_on(self):
        print("GameOver")
