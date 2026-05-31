"""
Validate the master dataset.

Quick sanity checks so I catch data-entry mistakes early:
  - every coupon_id is unique and follows <batch>-<replicate>
  - numeric columns actually contain numbers (where filled)
  - surface_area_ft2 matches the dimensions (within tolerance)

Usage (from project root):
    python 05_code/utils/validate_data.py
"""

import os
import csv
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DATA = os.path.join(ROOT, "03_data", "processed", "measurements.csv")

ID_RE = re.compile(r"^B\d+-\d+$")
NUMERIC_COLS = [
    "length_in", "width_in", "thickness_in", "surface_area_ft2", "grit",
    "acid_pct", "bath_temp_C", "target_voltage_V", "observed_voltage_V",
    "target_current_A", "current_density_ASF", "anodize_time_min",
    "target_thickness_mil", "dye_time_min", "dye_temp_C", "seal_time_min",
    "mean_gray_intensity", "contact_angle_deg", "wear_strokes", "wear_delta",
]


def main():
    with open(DATA, newline="") as f:
        rows = list(csv.DictReader(f))

    problems = []
    seen = set()

    for i, r in enumerate(rows, start=2):  # row 1 is the header
        cid = (r.get("coupon_id") or "").strip()
        if not cid:
            problems.append(f"row {i}: missing coupon_id")
        else:
            if not ID_RE.match(cid):
                problems.append(f"row {i}: coupon_id '{cid}' not <batch>-<replicate>")
            if cid in seen:
                problems.append(f"row {i}: duplicate coupon_id '{cid}'")
            seen.add(cid)

        for col in NUMERIC_COLS:
            val = (r.get(col) or "").strip()
            if val == "":
                continue  # blank is fine; not measured yet
            try:
                float(val)
            except ValueError:
                problems.append(f"row {i}: column '{col}' = '{val}' is not numeric")

        # cross-check area against dimensions if all present
        L = (r.get("length_in") or "").strip()
        W = (r.get("width_in") or "").strip()
        A = (r.get("surface_area_ft2") or "").strip()
        if L and W and A:
            try:
                expected = 2 * float(L) * float(W) / 144.0
                if abs(expected - float(A)) > 0.001:
                    problems.append(
                        f"row {i}: surface_area_ft2 {A} != computed {expected:.4f}")
            except ValueError:
                pass

    print(f"Checked {len(rows)} rows.")
    if problems:
        print(f"\nFound {len(problems)} issue(s):")
        for p in problems:
            print("  -", p)
    else:
        print("No issues found. Data looks clean.")


if __name__ == "__main__":
    main()
