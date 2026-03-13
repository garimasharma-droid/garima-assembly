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

assembly= Compound([

    bottom_part,

    top_part,

    top_holes_part
])


# ---------------------------
# EXPORT FINAL ASSEMBLY
# ---------------------------

export_stl(assembly, "garry_assembly.stl")

print("Assembly exported successfully")