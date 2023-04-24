import pyxel as py
from player import Player
from enemy import Enemy
from lib import Screen


class Game:
    def __init__(self):
        self._fps = 60
        self.delta_time = 0
        self.time = 0
        self._previous_time = 0

        self.screen = Screen(640, 480)
        self.player = Player(self)

        self.is_debug = False
        self._debug_index = 0
        self.game_objs = [self.player]
        self.debug_objs = [self, self.screen, self.player]

        py.init(self.screen.width, self.screen.height,
                fps=self._fps, title="Pixel Playground")
        Enemy.setup(self)
        py.mouse(True)
        py.run(self.update, self.draw)

    def add_obj(self, obj, debug: bool = False, on_top: bool = True):
        if not on_top:
            self.game_objs.insert(0, obj)
        else:
            self.game_objs.append(obj)
        if debug:
            self.debug_objs.append(obj)

    def remove_obj(self, obj):
        if obj in self.game_objs:
            self.game_objs.remove(obj)
        if obj in self.debug_objs:
            self.debug_objs.remove(obj)

    def update(self):
        self.time = py.frame_count * 1/self._fps
        self.delta_time = self.time - self._previous_time
        self._previous_time = self.time

        for obj in self.game_objs:
            obj.update()
        if self.is_debug and py.btnp(py.KEY_F1):
            self._debug_index -= 1
        if self.is_debug and py.btnp(py.KEY_F2):
            self._debug_index += 1
        if self._debug_index >= len(self.debug_objs):
            self._debug_index = 0
        if self._debug_index < 0:
            self._debug_index = len(self.debug_objs) - 1
        if py.btnp(py.KEY_F3):
            self.is_debug = not self.is_debug
        if py.btnp(py.KEY_ESCAPE):
            py.quit()
        if py.btnp(py.KEY_F11):
            py.fullscreen(not py.is_fullscreen)

    def draw(self):
        py.cls(0)
        for obj in self.game_objs:
            obj.draw()
        if self.is_debug:
            self.screen.draw_debug(self.debug_objs[self._debug_index])


Game()
