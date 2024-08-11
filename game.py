import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong Game"


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 0.02)
        self.change_x = 4
        self.change_y = 4

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Bounce off the walls
        if self.right >= SCREEN_WIDTH or self.left <= 0:
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = -self.change_y


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.2)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball()
        self.bar = Bar()
        self.score = 0
        self.game_over = False
        self.setup()

    def setup(self):
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 10
        self.score = 0
        self.game_over = False

    def on_draw(self):
        self.clear()
        self.bar.draw()
        self.ball.draw()
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 16)

        if self.game_over:
            game_over_text = "Game Over! Press R to Restart"
            arcade.draw_text(
                game_over_text,
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2,
                arcade.color.WHITE,
                16,
                anchor_x="center",  # Horizontal anchor point
                anchor_y="center"  # Vertical anchor point
            )

    def update(self, delta):
        if not self.game_over:
            if arcade.check_for_collision(self.bar, self.ball):
                self.ball.change_y = -self.ball.change_y
                self.score += 1
            self.ball.update()
            self.bar.update()
            # Check for game over
            if self.ball.bottom <= 0:
                self.game_over = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5
        elif key == arcade.key.LEFT:
            self.bar.change_x = -5
        elif key == arcade.key.R and self.game_over:
            self.setup()

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.RIGHT, arcade.key.LEFT):
            self.bar.change_x = 0


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
