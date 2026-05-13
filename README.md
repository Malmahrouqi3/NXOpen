## Overview

```
Parameters
      │
      ▼
 Generate .exp file  ──►  NX: Expressions → Import Expressions
      │                            │
      │                            ▼
      │                    Geometry updates automatically
      │
      └── Modify one value → re-run → new geometry in seconds
```

## Scripts

### `Expressions.py`
Core formatter and writer for NX expression files.

```python
from Expressions import format_exp, write_exp_file, write_txt_file

# Format a single expression
expr = format_exp("Wing_xShift", t="number", val=0, u="MilliMeter")

# Write a list of expressions to an .exp file
write_exp_file(expressions_list, "wing_params")

# Write a .txt with only expression names (useful for NX references)
write_txt_file(expressions_list, "wing_names")
```

**In NX:** `Expressions → Import Expressions → Open .exp file`

---

### `Airfoil.py`
Generates expressions from a `.dat` file, where each point gets position, airfoil-level, and part-level shift expressions, so individual airfoils and whole assemblies can be repositioned.

```python
from Airfoil import Airfoil_XY

Airfoil_XY(
    Part_Name="Wing_001",
    Airfoil_Name="Airfoil0",
    filename="NACA2412.dat",
    Unit="MilliMeter"
)
```
---

## Files

```
NXOpen/
├── Expressions.py            # Core .exp formatter and writer
├── Airfoil.py                # Airfoil expression generator
├── Airfoil_Intrapolation.py  # Wing section interpolation
├── cst_para.py               # CST airfoil parametrization
├── Read_Dat.py               # .dat file reader
├── dat_to_txt_file.py        # .dat → .txt converter
├── Wing.vspscript            # OpenVSP cross-validation script
├── Hyperion/                 # Sample project: Hyperion vehicle
└── Sample Cases/             # Example .dat files and outputs
```
