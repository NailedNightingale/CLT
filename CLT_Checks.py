
# Simple checks for CLT to design guide

import CLT_classes as CLT
from CLT_catalogue import XLam, Custom
from CalculationReport import *

clt_panel = XLam.get_catalogue_panel(260)

Z_perp = clt_panel.get_Z_perp()
Z_par = clt_panel.get_Z_par()

bending_capacity_par = clt_panel.get_design_bending_capacity_par()
bending_capacity_perp = clt_panel.get_design_bending_capacity_perp()

inputs = [f"CLT Layer Thicknesses (mm): {clt_panel.layer_thickness_list}",
          f"CLT E Values (Parallel Span): {clt_panel.E_parallel_list}",
          f"CLT E Values (Perpendicular Span) : {clt_panel.E_perpendicular_list}",
          f"phi Value: {clt_panel.phi}",
          f"Bending Strength (Outer Layers): {clt_panel.fb_par_list[0]} MPa",
          f"Bending Strength (Inner Layers): {clt_panel.fb_perp_list[1]} MPa"]

calculations = [f"EI (Parallel Span): {clt_panel.get_EI_par():.4} N.mm2",
                f"EI (Perpendicular Span): {clt_panel.get_EI_perp():.4} N.mm2",
                f"Zeff (Parallel Span): {clt_panel.get_Z_par():.4} mm3",
                f"Zeff (Perpendicular Span): {clt_panel.get_Z_perp():.4} mm3",
                f"Design Bending Capacity (Parallel Span): {clt_panel.phi} * {clt_panel.fb_par_list[0]} * {Z_par:.4} = {bending_capacity_par / 1_000_000:.4} kN.m",
                f"Design Bending Capacity (Perpendicular Span): {clt_panel.phi} * {clt_panel.fb_perp_list[1]} * {Z_perp:.4} = {bending_capacity_perp / 1_000_000:.4} kN.m"]

comments = ["1.  Methodology for calculating Zeff based on FP Innovations Design Guide.",
            "2.  Material properties taken from XLam Australia and New Zealand 2020 Structural Design Guide"]

set_project(270830, "BGH")
generate_title_block("Custom Panel Check")
generate_inputs(inputs)
generate_calcs(calculations)
generate_comments(comments)
end_report()


