import pyxel as px
from game_lib import TextBox, Game, CENTERED


class GameOverScreen(TextBox):
    def __init__(self, game: Game, score: int) -> None:
        text = f"Game Over\nScore: {score}\nPress SPACE to restart"
        super().__init__(game, text, 10)
        self.place(CENTERED, CENTERED)
        self.game.add_obj(self, True)
        self.tick_task(self.restart_game)

    def restart_game(self):
        if px.btnp(px.KEY_SPACE):
            self.game.remove_obj(self)
            self.game.setup()
