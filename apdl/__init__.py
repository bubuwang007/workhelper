from .Command import Command
from .Commands import Commands
from .Mac import Mac
from .Segment import Segment
from .Processor import *
from .Array import Array
from .Func import Func
from .Do import Do
from .If import If
from .lib.Math import Math
from .lib.System import System
from .lib.Elements import Elements
from .lib.Selecting import Selecting
from .lib.Aux15 import Aux15
from .lib.Components import Components
from .lib.Graphics import Graphics
from .lib.CrossSections import CrossSections
from .lib.WorkingPlane import WorkingPlane
from .lib.GraphicsPrimitives import GraphicsPrimitives
from .lib.Booleans import Booleans
from .lib.ElementType import ElementType
from .lib.Meshing import Meshing
from .lib.Areas import Areas
from .lib.Keypoints import Keypoints
from .lib.RealConstants import RealConstants
from .lib.Materials import Materials
from .lib.Get import Get
from .lib.Lines import Lines
from .lib.Forces import Forces
from .lib.ConstraintEquations import ConstraintEquations
from .lib.Constraint import Constraint
from .lib.Analysis import Analysis
from .lib.Nodes import Nodes


class Apdl:

    def __init__(self, mac: Mac):
        self.math = Math()
        self.system = System(mac)
        self.elements = Elements(mac)
        self.selecting = Selecting(mac)
        self.aux15 = Aux15(mac)
        self.components = Components(mac)
        self.graphics = Graphics(mac)
        self.cross_sections = CrossSections(mac)
        self.working_plane = WorkingPlane(mac)
        self.graphics_primitives = GraphicsPrimitives(mac)
        self.booleans = Booleans(mac)
        self.element_type = ElementType(mac)
        self.meshing = Meshing(mac)
        self.areas = Areas(mac)
        self.keypoints = Keypoints(mac)
        self.real_constants = RealConstants(mac)
        self.materials = Materials(mac)
        self.get = Get(mac)
        self.lines = Lines(mac)
        self.forces = Forces(mac)
        self.constraint_equations = ConstraintEquations(mac)
        self.constraint = Constraint(mac)
        self.analysis = Analysis(mac)
        self.nodes = Nodes(mac)

        # alias
        self.sys = self.system
        self.el = self.elements
        self.sel = self.selecting
        self.compos = self.components
        self.g = self.graphics
        self.cs = self.cross_sections
        self.wp = self.working_plane
        self.gp = self.graphics_primitives
        self.bool = self.booleans
        self.et = self.element_type
        self.mesh = self.meshing
        self.area = self.areas
        self.kp = self.keypoints
        self.rc = self.real_constants
        self.mat = self.materials
        self.l = self.lines
        self.f = self.forces
        self.ce = self.constraint_equations
        self.c = self.constraint
        self.a = self.analysis
        self.n = self.nodes
