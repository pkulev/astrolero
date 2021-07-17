from __future__ import annotations

import re
from typing import Tuple

from eaf import State, Vec3
from xo2 import Application
from xo2.render import ObjectRenderer3D, Renderable


class PerspectiveCamera:
    def __init__(self, fov=50, aspect=1, near=0.1, far=2000):
        self.fov = fov
        self.aspect = aspect
        self.near = near
        self.far = far

        self.zoom = 1
        self.focus = 10


class Node:

    def __init__(self, *args, name="new node", **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.parent = None
        self.nodes = []

    def add(self, node: Union[Node, List[Node]]):
        node.parent = self
        self.nodes.append(node)

    def add_many(self, *nodes: Tuple[Node]):
        for node in nodes:
            self.add(node)

    def traverse(self):
        def rec(node, acc):
            if not node.nodes:
                return acc + [node]

            return acc + [n.traverse() for n in node.nodes]

        return rec(self, [])

    def __str__(self):
        return f"{self.name} ({id(self)})"

    __repr__ = __str__


n = Node()
print(n.traverse())
n.add_many(Node(), Node())
n.nodes[1].add(Node())
print(n.traverse())

exit()


from dataclasses import dataclass


@dataclass
class Object:
    name = "unnamed"
    vertices = []
    faces = []
    normals = []


class ObjFile:

    def __init__(self):
        self._objects = []

    @classmethod
    def load(cls, objfile):
        objects = []
        object_re = re.compile("^o (-?.*)$")
        vertex_re = re.compile("^v (-?\d+.\d+) (-?\d+.\d+) (-?\d+.\d+)")
        face_re = re.compile("^f ")

        current = Object()

        with open(objfile) as fh:
            for line in fh:
                if match := vertex_re.search(line):
                    current.vertices.append(Vec3(*map(float, match.groups())))
                elif match := face_re.search(line):
                    pass
                elif match := object_re.match(line):
                    objects.append(current)
                    current = Object()
                    current.name = match.group(1)

        obj = cls()
        obj.objects = objects
        return obj

    def __iter__(self):
        return iter(self._objects)


class Object3D(Renderable, Node):

    def __init__(self, pos, vertices):

        super().__init__(pos)

        self.vertices = []
        self.s = []

    @classmethod
    def from_obj(cls, pos, objfile):
        objects = ObjFile.load(objfile)
        o = cls(pos, [])
        for obj in objects:
            oo = cls(Vec3(), [])
            oo.parent = o
            oo.vertices = obj.vertices[:]
            o.vertices += oo.vertices[:]
            o.nodes.append(oo)

        return o


class Glock(Object3D):

    def __init__(self, pos, vertices):

        super().__init__(pos, vertices)

        self._vertices = vertices

        import pygame
        self.vertex_color = pygame.Color(255, 255, 255, 255)

        self.dx = 0
        self.dy = 0


    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, val):
        self._vertices = val

    def update(self, dt):
        self.pos.x += self.dx
        self.pos.y += self.dy


class GameState(State):

    def postinit(self):
        # self.actor = Camera(0, 0)
        self.actor = Glock.from_obj(Vec3(0, 0), "glock17.obj")
        self.add(self.actor)

        self.dx = 0
        self.dy = 0

    def events(self):
        # self.app.input_manager
        import pygame
        pygame.key.set_repeat(50, 50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.stop()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.app.stop()

                if event.key == pygame.K_d:
                    self.actor.dx += 3
                elif event.key == pygame.K_a:
                    self.actor.dx -= 3
                elif event.key == pygame.K_w:
                    self.actor.dy -= 3
                elif event.key == pygame.K_s:
                    self.actor.dy += 3

    def render(self):
        import pygame
        self.app.renderer.clear()

        self.app.renderer.line(400, 0, 400, 600, pygame.Color(0, 0, 255, 255))
        self.app.renderer.line(0, 300, 800, 300, pygame.Color(255, 0, 0, 255))

        self.app.renderer.render_objects(self._objects)

        self.app.renderer.present()


class App(Application):

    pass


app = App((800, 600))
app.register(GameState)
app._renderer = ObjectRenderer3D(app.renderer.screen)

app.start()
