import pyxel as px
from lib import GameObject, Game


class GameOverScreen(GameObject):
    def __init__(self, game: Game, score: int) -> None:
        super().__init__(game)
        self.score = score
        self.game.add_obj(self, True)
        self.tick_task(self.restart_game)

    def draw(self):
        px.text(self.game.screen.width/2, self.game.screen.height/2,
                f"Game Over\nScore: {self.score}\nPress SPACE to restart", 3)

    def restart_game(self):
        if px.btnp(px.KEY_SPACE):
            self.game.remove_obj(self)
            self.game.setup()
