import pyxel as px

from . import Screen, Shape

__all__ = ["Game"]


class Game:
    TICKED = -1
    DRAWN = 1
    BOTH = 0

    def __init__(self, resources: str = None, fps: int = 60,
                 screen: Screen = Screen(320, 240)):
        self._fps = fps
        self.delta_time = 0
        self.time = 0
        self._previous_time = 0
        self.screen = screen
        self.is_debug = False
        self._debug_index = 0
        self.reset()
        if resources is not None:
            px.load(resources)
        px.run(self.update, self.draw)

    def add_obj(self, game_object, debug: bool = False, on_top: bool = True,
                obj_type: int = BOTH):
        def add_to_list(obj_list: list, obj=game_object):
            if not on_top:
                obj_list.insert(0, obj)
            else:
                obj_list.append(obj)

        if game_object.shape is not None:
            add_to_list(self.drawn_objects, game_object.shape)
        if obj_type == Game.BOTH:
            add_to_list(self.ticked_objs)
            add_to_list(self.drawn_objects)
        elif obj_type == Game.TICKED:
            add_to_list(self.ticked_objs)
        elif obj_type == Game.DRAWN:
            add_to_list(self.drawn_objects)
        if debug:
            self.debug_objs.append(game_object)

    def remove_obj(self, obj):
        if obj in self.ticked_objs:
            self.ticked_objs.remove(obj)
        if obj in self.drawn_objects:
            self.drawn_objects.remove(obj)
            self.drawn_objects.remove(obj.shape)
        if obj in self.debug_objs:
            self.debug_objs.remove(obj)

    def update(self):
        self.time = px.frame_count * 1/self._fps
        self.delta_time = self.time - self._previous_time
        self._previous_time = self.time

        for obj in self.ticked_objs:
            obj.update()
        if self.is_debug and px.btnp(px.KEY_F1):
            self._debug_index -= 1
        if self.is_debug and px.btnp(px.KEY_F2):
            self._debug_index += 1
        if self._debug_index >= len(self.debug_objs):
            self._debug_index = 0
        if self._debug_index < 0:
            self._debug_index = len(self.debug_objs) - 1
        if px.btnp(px.KEY_F9):
            Shape.force_visible = not Shape.force_visible
        if px.btnp(px.KEY_F3):
            self.is_debug = not self.is_debug
        if px.btnp(px.KEY_F5):
            self.reset()
        if px.btnp(px.KEY_ESCAPE):
            px.quit()
        if px.btnp(px.KEY_F11):
            px.fullscreen(not px.is_fullscreen)

    def reset(self):
        self.ticked_objs = []
        self.drawn_objects = []
        self.debug_objs = [self, self.screen]
        self.setup()

    def draw(self):
        px.cls(0)
        for obj in self.drawn_objects:
            obj.draw()
        if self.is_debug:
            self.screen.draw_debug(self.debug_objs[self._debug_index])

    def setup(self):
        pass
