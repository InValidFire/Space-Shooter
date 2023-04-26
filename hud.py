from game_lib import TextBox, GameObject, LEFT, CENTERED, TOP, RIGHT, Game

import pyxel as px


class HUD(GameObject):
    def __init__(self, game: Game) -> None:
        super().__init__(game)
        self.score_box = TextBox(game, f"Score: {self.game.player.score}", 11)
        self.lives_box = TextBox(game, f"Lives: {self.game.player.lives}", 11)
        self.version_box = TextBox(game, self.game.version, 11)

        self.lives_box.place(LEFT, TOP)
        self.score_box.place(CENTERED, TOP)
        self.version_box.place(RIGHT, TOP)

        self.game.add_obj(self.lives_box, True, True)
        self.game.add_obj(self.score_box, True, True)
        self.game.add_obj(self.version_box, True, True)
        self.tick_task(self.update_lives)
        self.tick_task(self.update_score)
        self.game.add_obj(self, False, True, Game.TICKED)

    def update_score(self):
        if int(self.score_box.text.split()[1]) != self.game.player.score:
            self.score_box.place(CENTERED, TOP)
            self.score_box.text = f"Score: {self.game.player.score}"

    def update_lives(self):
        if int(self.lives_box.text.split()[1]) != self.game.player.lives:
            self.lives_box.place(LEFT, TOP)
            self.lives_box.text = f"Lives: {self.game.player.lives}"

    def game_over(self):
        self.game.debug_objs = [self]
        self.game.ticked_objs = [self]
        self.game.drawn_objects = [self.version_box]
        text = f"Game Over\nScore: {self.game.player.score}" \
            "\nPress SPACE to restart"
        game_over_box = TextBox(self.game, text, 11)
        game_over_box.place(CENTERED, CENTERED)
        self.game.add_obj(game_over_box)
        self.tick_task(self.restart_game)

    def restart_game(self):
        if px.btnp(px.KEY_SPACE):
            self.untick_task(self.restart_game)
            self.game.setup()
