
"""Module containing properties for the different CLT panels"""
import CLT_classes as CLT


class CatalogueCLT:

    thicknesses = {}

    E_parallel = {}

    E_perpendicular = {}

    fb_parallel = {}

    fb_perpendicular = {}

    fc_parallel = {}

    fc_perpendicular = {}

    fs_parallel = {}

    fs_perpendicular = {}

    G_parallel = {}

    G_perpendicular = {}


    @classmethod
    def get_catalogue_panel(cls, depth):
        panel = CLT.CLT(cls.thicknesses[depth],
                        1000,
                        cls.E_parallel[depth],
                        cls.E_perpendicular[depth],
                        cls.G_parallel[depth],
                        cls.G_perpendicular[depth],
                        cls.fb_parallel[depth],
                        cls.fb_perpendicular[depth],
                        cls.fc_parallel[depth],
                        cls.fc_perpendicular[depth],
                        cls.fs_parallel[depth],
                        cls.fs_perpendicular[depth],
                        k1=0.8,
                        k4=1.0,
                        k6=1.0,
                        k9=1.0,
                        k12=1.0)

        return panel


class Custom(CatalogueCLT):

    thicknesses = {520: [42.5, 35, 35, 35, 35, 35, 42.5, 42.5, 35, 35, 35, 35, 35, 42.5]}

    E_parallel = {520: [10000, 0, 6000, 0, 6000, 0, 10000, 10000, 0, 6000, 0, 6000, 0, 10000]}

    E_perpendicular = {520: [0, 6000, 0, 6000, 0, 6000, 0, 0, 6000, 0, 6000, 0, 6000, 0]}

    fb_parallel = {520: [17, 0, 10, 0, 10, 0, 17, 17, 0, 10, 0, 10, 0, 17]}

    fb_perpendicular = {520: [0, 10, 0, 10, 0, 10, 0, 0, 10, 0, 10, 0, 10, 0]}

    fc_parallel = {520: [18, 8.9, 10, 8.9, 10, 8.9, 18, 18, 8.9, 10, 8.9, 10, 8.9, 18]}

    fc_perpendicular = {520: [10, 15, 8.9, 15, 8.9, 15, 10, 10, 15, 8.9, 15, 8.9, 15, 10]}

    fs_parallel = {520: [3.8, 1.2, 3.8, 1.2, 3.8, 1.2, 3.8, 3.8, 1.2, 3.8, 1.2, 3.8, 1.2, 3.8]}

    fs_perpendicular = {520: [1.2, 3.8, 1.2, 3.8, 1.2, 3.8, 1.2, 1.2, 3.8, 1.2, 3.8, 1.2, 3.8, 1.2]}

    G_parallel = {520: [670, 29, 400, 29, 400, 29, 670, 670, 29, 400, 29, 400, 29, 670]}

    G_perpendicular = {520: [45, 400, 29, 400, 29, 400, 45, 45, 400, 29, 400, 29, 400, 45]}

    density = 5  # kN/m3


class XLam(CatalogueCLT):
    """Class containing all base layer properties of XLam CLT panels.
    Note that where properties are denoted as 'parallel', this refers to properties parallel to the primary SPAN direction.
    This does NOT indicate properties parallel to the grain of individual layers.
    Similar notation applies to properties denoted as 'perpendicular'."""

    thicknesses = {165: [45, 20, 35, 20, 45],
                   240: [32.5, 35, 35, 35, 35, 35, 32.5],
                   260: [42.5, 35, 35, 35, 35, 35, 42.5],
                   270: [42.5, 35, 35, 45, 35, 35, 42.5],
                   290: [42.5, 35, 45, 45, 45, 35, 42.5],
                   310: [42.5, 45, 45, 45, 45, 45, 42.5]}

    E_parallel = {165: [8000, 0, 6000, 0, 8000],
                  240: [10000, 0, 6000, 0, 6000, 0, 10000],
                  260: [10000, 0, 6000, 0, 6000, 0, 10000],
                  270: [10000, 0, 6000, 0, 6000, 0, 10000],
                  290: [10000, 0, 6000, 0, 6000, 0, 10000],
                  310: [10000, 0, 6000, 0, 6000, 0, 10000]}

    E_perpendicular = {165: [0, 6000, 0, 6000, 0],
                       240: [0, 6000, 0, 6000, 0, 6000, 0],
                       260: [0, 6000, 0, 6000, 0, 6000, 0],
                       270: [0, 6000, 0, 6000, 0, 6000, 0],
                       290: [0, 6000, 0, 6000, 0, 6000, 0],
                       310: [0, 6000, 0, 6000, 0, 6000, 0]}

    fb_parallel = {165: [12, 0, 10, 0, 12],
                   240: [17, 0, 10, 0, 10, 0, 17],
                   260: [17, 0, 10, 0, 10, 0, 17],
                   270: [17, 0, 10, 0, 10, 0, 17],
                   290: [17, 0, 10, 0, 10, 0, 17],
                   310: [17, 0, 10, 0, 10, 0, 17]}

    fb_perpendicular = {165: [0, 10, 0, 10, 0],
                        240: [0, 10, 0, 10, 0, 10, 0],
                        260: [0, 10, 0, 10, 0, 10, 0],
                        270: [0, 10, 0, 10, 0, 10, 0],
                        290: [0, 10, 0, 10, 0, 10, 0],
                        310: [0, 10, 0, 10, 0, 10, 0]}

    fc_parallel = {165: [18, 8.9, 10, 8.9, 18],
                   240: [18, 8.9, 10, 8.9, 10, 8.9, 18],
                   260: [18, 8.9, 10, 8.9, 10, 8.9, 18],
                   270: [18, 8.9, 10, 8.9, 10, 8.9, 18],
                   290: [18, 8.9, 10, 8.9, 10, 8.9, 18],
                   310: [18, 8.9, 10, 8.9, 10, 8.9, 18]}

    fc_perpendicular = {165: [10, 10, 8.9, 10, 10],
                        240: [10, 15, 8.9, 15, 8.9, 15, 10],
                        260: [10, 15, 8.9, 15, 8.9, 15, 10],
                        270: [10, 15, 8.9, 15, 8.9, 15, 10],
                        290: [10, 15, 8.9, 15, 8.9, 15, 10],
                        310: [10, 15, 8.9, 15, 8.9, 15, 10]}

    fs_parallel = {165: [3.8, 1.2, 3.8, 1.2, 3.8],
                   240: [3.8, 1.2, 3.8, 1.2, 3.8, 1.2, 3.8],
                   260: [3.8, 1.2, 3.8, 1.2, 3.8, 1.2, 3.8],
                   270: [3.8, 1.2, 3.8, 1.2, 3.8, 1.2, 3.8],
                   290: [3.8, 1.2, 3.8, 1.2, 3.8, 1.2, 3.8],
                   310: [3.8, 1.2, 3.8, 1.2, 3.8, 1.2, 3.8]}

    fs_perpendicular = {165: [1.2, 3.8, 1.2, 3.8, 1.2],
                        240: [1.2, 3.8, 1.2, 3.8, 1.2, 3.8, 1.2],
                        260: [1.2, 3.8, 1.2, 3.8, 1.2, 3.8, 1.2],
                        270: [1.2, 3.8, 1.2, 3.8, 1.2, 3.8, 1.2],
                        290: [1.2, 3.8, 1.2, 3.8, 1.2, 3.8, 1.2],
                        310: [1.2, 3.8, 1.2, 3.8, 1.2, 3.8, 1.2]}

    G_parallel = {165: [533, 40, 400, 40, 533],
                  240: [670, 29, 400, 29, 400, 29, 670],
                  260: [670, 29, 400, 29, 400, 29, 670],
                  270: [670, 29, 400, 29, 400, 29, 670],
                  290: [670, 29, 400, 29, 400, 29, 670],
                  310: [670, 29, 400, 29, 400, 29, 670]}

    G_perpendicular = {165: [53, 400, 40, 400, 53],
                       240: [45, 400, 29, 400, 29, 400, 45],
                       260: [45, 400, 29, 400, 29, 400, 45],
                       270: [45, 400, 29, 400, 29, 400, 45],
                       290: [45, 400, 29, 400, 29, 400, 45],
                       310: [45, 400, 29, 400, 29, 400, 45]}

    density = 5  # kN/m3

    def get_clt_properties(self):
        pass


class Hasslacher:
    pass


class StoraEnso:
    pass

