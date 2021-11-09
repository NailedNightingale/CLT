

class CLTLayer:

    def __init__(self, thickness, width, dist_from_NA,
                 E_par, E_perp,
                 G_par, G_perp,
                 fb_par, fb_perp,
                 fc_par, fc_perp,
                 fs_par, fs_perp):
        self.thickness = thickness
        self.width = width
        self.dist_from_NA = dist_from_NA
        self.E_par = E_par
        self.E_perp = E_perp
        self.G_par = G_par
        self.G_perp = G_perp
        self.fb_par = fb_par
        self.fb_perp = fb_perp
        self.fc_par = fc_par
        self.fc_perp = fc_perp
        self.fs_par = fs_par
        self.fs_perp = fs_perp

    def get_max_flexural_strain_for_layer_par(self, total_depth):
        if self.E_par != 0:
            epsilon_max = self.fb_par * total_depth / (((2 * self.dist_from_NA) + self.thickness) * self.E_par)
        else:
            epsilon_max = 1
        return epsilon_max

    def get_max_min_layer_stress_par(self, top_of_panel_strain, total_depth):
        max_layer_strain = ((self.dist_from_NA + (0.5 * self.thickness)) / (total_depth / 2)) * top_of_panel_strain
        min_layer_strain = ((self.dist_from_NA - (0.5 * self.thickness)) / (total_depth / 2)) * top_of_panel_strain
        max_layer_stress = max_layer_strain * self.E_par
        min_layer_stress = min_layer_strain * self.E_par

        return max_layer_stress, min_layer_stress

    def get_layer_force(self, max_layer_stress, min_layer_stress):
        average_layer_stress = (max_layer_stress + min_layer_stress) / 2
        layer_force = average_layer_stress * self.thickness * self.width
        return layer_force

    def get_layer_moment(self, layer_force):
        layer_moment = self.dist_from_NA * layer_force
        return layer_moment


class CLT:

    def __init__(self, layer_thickness_list,
                 panel_width,
                 E_parallel_list, E_perpendicular_list,
                 G_parallel_list, G_perpendicular_list,
                 fb_par_list, fb_perp_list,
                 fc_par_list, fc_perp_list,
                 fs_par_list, fs_perp_list,
                 k1, k4, k6, k9, k12):
        self.layer_thickness_list = layer_thickness_list
        self.panel_width = panel_width
        self.E_parallel_list = E_parallel_list
        self.E_perpendicular_list = E_perpendicular_list
        self.G_parallel = G_parallel_list
        self.G_perpendicular = G_perpendicular_list
        self.fb_par_list = fb_par_list
        self.fb_perp_list = fb_perp_list
        self.fc_par_list = fc_par_list
        self.fc_perp_list = fc_perp_list
        self.fs_par_list = fs_par_list
        self.fs_perp_list = fs_perp_list
        self.k1 = k1
        self.k4 = k4
        self.k6 = k6
        self.k9 = k9
        self.k12 = k12
        self.char = 70  # TODO: Replace this with an appropriate variable initilaliser in the constructor

        self.total_depth = sum(layer_thickness_list)
        self.elastic_NA_par = self.get_elastic_NA_par()
        # TODO: Create method for calculating the same property for the fire case
        self.layers = [layer for layer in self.gen_clt_layers()]
        # TODO: Create method for generating the layers for the fire case
        # Once the two additional methods above have been completed, the calculations for fire can reeuse the other code
        self.perpendicular_layer_areas = [layer.thickness * self.panel_width for layer in self.layers[1::2]]
        self.perpendicular_layer_total_area = sum(self.perpendicular_layer_areas)
        self.smia_list = self.SMIACalculations.smia_list_calc(self.total_depth, self.panel_width, self.layers)
        self.phi = 0.85
        self.layer_areas = []

    def get_fire_layer_thickness_list(self):
        # Need to generate a new list of thicknesses to account for the
        remaining_char = self.char
        fire_layer_thickness_list = []
        for thickness in self.layer_thickness_list:
            if remaining_char > thickness:
                thickness = 0
                remaining_char -= thickness
            elif 0 < remaining_char < thickness:
                thickness -= abs(remaining_char)
                remaining_char = 0
            else:
                pass
            fire_layer_thickness_list.append(thickness)
        return fire_layer_thickness_list


    def get_elastic_NA_par(self):
        """Function calculates the location of the elastic neutral axis from first principles"""
        # 'i' is the index for keeping track of which layer in the list
        i = 0

        # 'y' is the height of the given layer
        # We initialize to the first layer before iterating
        y = self.layer_thickness_list[0] / 2

        # Sum of the axial stiffnesses of each individual layer
        layer_EA_list = [E * t for E, t in zip(self.E_parallel_list, self.layer_thickness_list)]

        # We iterate through to get the height of each individual layer relative to the 'bottom' of the panel
        # We multiply this height by the axial stiffness to get it's contribution to the flexural stiffness
        layer_EAy_list = []
        for EA, thickness in zip(layer_EA_list, self.layer_thickness_list):
            EAy = EA * y
            layer_EAy_list.append(EAy)
            if i + 1 >= len(self.layer_thickness_list):
                pass
            else:
                y += (self.layer_thickness_list[i] * 0.5) + (self.layer_thickness_list[i + 1] * 0.5)
            i += 1
        sum_EA = sum(layer_EA_list)
        sum_EAy = sum(layer_EAy_list)

        # For the elastic neutral axis, we take the weighted average of height * axial stiffness of each layer
        # Divided by the sum of the axial stiffnesses
        elastic_NA = sum_EAy / sum_EA
        return elastic_NA


    def get_elastic_NA_par_fire(self):
        """Function calculates the location of the elastic neutral axis in the fire case from first principles"""



    def gen_clt_layers(self):
        """Generates the layers of the CLT panel."""
        i = 0  # Represents the index of the current panel layer
        y = self.layer_thickness_list[0] * 0.5  # Represents the current layer height from bottom of panel
        for thickness, E_par, E_perp, G_par, G_perp, fb_par, fb_perp, fc_par, fc_perp, fs_par, fs_perp in \
                zip(self.layer_thickness_list, self.E_parallel_list, self.E_perpendicular_list,
                    self.G_parallel, self.G_perpendicular, self.fb_par_list, self.fb_perp_list,
                    self.fc_par_list, self.fc_perp_list, self.fs_par_list, self.fs_perp_list):
            # Where is the neutral axis??
            layer_dist_from_NA = abs(self.elastic_NA_par - y)
            y += (thickness * 0.5) + (self.layer_thickness_list[i+1] * 0.5)
            if i + 2 >= len(self.layer_thickness_list):
                pass
            else:
                i += 1
            layer = CLTLayer(thickness, self.panel_width, layer_dist_from_NA, E_par, E_perp, G_par, G_perp, fb_par, fb_perp,
                             fc_par, fc_perp, fs_par, fs_perp)
            yield layer

    """STIFFNESS PARAMETERS"""

    class SMIACalculations:
        """Second moment of inertia of area (SMIA, i.e. I value) calculations.
        The 'I' character has been avoided in the namespacing as it was leading to unreadable code."""

        @staticmethod
        def parallel_axis_calc(area, distance):
            I_parax = area * distance**2
            return I_parax

        @staticmethod
        def rectangle_calc(width, depth):
            I_rectangle = width * (depth**3) / 12
            return I_rectangle

        @classmethod
        def smia_layer_calc(cls, rect_width, rect_depth, dist_from_na):
            area = rect_width * rect_depth
            I_rectangle = cls.rectangle_calc(rect_width, rect_depth)
            print(I_rectangle)
            I_parax = cls.parallel_axis_calc(area, dist_from_na)
            print(I_parax)
            smia = I_rectangle + I_parax
            return smia

        @classmethod
        def smia_list_calc(cls, panel_depth, panel_width, panel_layers):
            layer_smia_list = []
            for layer in panel_layers:
                smia_layer = cls.smia_layer_calc(panel_width, layer.thickness, layer.dist_from_NA)
                layer_smia_list.append(smia_layer)
            return layer_smia_list

    def get_EI_par(self):
        EI_parallel_list = [E * I for E, I in zip(self.E_parallel_list, self.smia_list)]
        EI_par_actual = sum(EI_parallel_list)
        return EI_par_actual

    def get_EI_perp(self):
        EI_perpendicular_list = [E * I for E, I in zip(self.E_perpendicular_list, self.smia_list)]
        EI_perp_actual = sum(EI_perpendicular_list)
        return EI_perp_actual

    def get_EA_par(self):
        E_par = [E for E in self.E_parallel_list[0::2]]
        A_par = [self.panel_width * thickness for thickness in self.layer_thickness_list[0::2]]
        EA_par = sum(E * A for E, A in zip(E_par, A_par))
        return EA_par

    def get_EA_perp(self):
        E_perp = [E for E in self.E_parallel_list[1::2]]
        A_perp = [self.panel_width * thickness for thickness in self.layer_thickness_list[1::2]]
        EA_perp = sum(E * A for E, A in zip(E_perp, A_perp))
        return EA_perp

    def get_I_par(self):
        I_par = sum(self.smia_list[::2])
        return I_par

    def get_I_perp(self):
        I_perp = sum(self.smia_list[1::2])
        return I_perp

    def get_Z_par(self):
        """Function to calculate the section modulus based on I/y. This should be treated with caution.
        The section modulus from this expression may not capture the load at first failure.
        Inner layers can fail before outer layers if inner layers are significantly lower grade material.
        This tends to be more problematic with thicker panels."""

        EI_par = self.get_EI_par()
        Z_par = EI_par / (0.5 * self.E_parallel_list[0] * self.total_depth)
        return Z_par

    def get_Z_perp(self):
        """Function to calculate the section modulus based on I/y. This should be treated with caution.
        The section modulus from this expression may not capture the load at first failure.
        Inner layers can fail before outer layers if inner layers are significantly lower grade material.
        This tends to be more problematic with thicker panels."""
        EI_perp = self.get_EI_perp()
        thickness_perp = self.total_depth - (self.layer_thickness_list[0] + self.layer_thickness_list[-1])
        Z_perp = EI_perp / (0.5 * self.E_perpendicular_list[1] * thickness_perp)
        return Z_perp

    """CAPACITY PARAMETERS"""

    def get_design_bending_capacity_par(self):

        # The list below contains the top-of-panel strain required to achieve f'b in each individual layer
        top_strain_for_f_b_list = [layer.get_max_flexural_strain_for_layer_par(self.total_depth) for layer in self.layers]

        # It is assumed that the layer with the minimum top-of-panel strain will govern the flexural capacity
        # (i.e. that layer will break first, leading to failure of the panel)
        top_of_panel_strain = min(top_strain_for_f_b_list)

        # Once the top-of-panel strain is established, use this to calculate the individual layer stresses
        layer_stresses = [layer.get_max_min_layer_stress_par(top_of_panel_strain, self.total_depth) for layer in self.layers]

        # Calculate the corresponding force in each layer from the layer's stresses
        layer_forces = [layer.get_layer_force(stress[0], stress[1]) for layer, stress in zip(self.layers, layer_stresses)]

        # Calculate the corresponding moment about the neutral axis from each layer's force
        layer_moments = [layer.get_layer_moment(force) for layer, force in zip(self.layers, layer_forces)]

        # Sum the moment contributions from the individual layers to get the total moment capacity
        moment_capacity = self.k1 * self.k4 * self.k6 * self.k9 * self.k12 * sum(layer_moments)

        # Apply the phi factor to achieve the design moment capacity
        design_moment_capacity = self.phi * moment_capacity

        return design_moment_capacity

    def get_design_bending_capacity_perp(self):
        design_capacity = self.phi * self.fb_perp_list[1] * self.get_Z_perp()
        return design_capacity

    def get_design_shear_capacity_par(self):
        pass

    def get_design_shear_capacity_perp(self):
        pass

    def get_design_compression_capacity_par(self):
        pass

    def get_design_compression_capacity_perp(self):
        pass

    def get_design_tension_capacity_par(self):
        pass

    def get_design_tension_capacity_perp(self):
        pass


