from build123d import *

# ---------------------------
# IMPORT STL PARTS
# ---------------------------

bottom_part = import_stl("Bottom.stl")
top_part = import_stl("Top.stl")
top_holes_part = import_stl("Top-holes.stl")

# ---------------------------
# CREATE ASSEMBLY
# ---------------------------

assembly = Compound([
    bottom_part,
    top_part,
    top_holes_part
])

# ---------------------------
# OPERATION COUNT
# ---------------------------

volumetric_operations = 0
symmetry_operations = 0

# ---------------------------
# EXPORT FINAL ASSEMBLY
# ---------------------------

export_stl(assembly, "garry_assembly.stl")

# ---------------------------
# OUTPUT RESULTS
# ---------------------------

print("Assembly exported successfully")
print("Volumetric Operations:", volumetric_operations)
print("Symmetry Operations:", symmetry_operations)