"""
Plot results from the master dataset.

Reads 03_data/processed/measurements.csv and writes figures to 04_images/figures/.
Designed to run even when the dataset is only partly filled in — it skips plots it
has no data for, so I can run it from day one and watch figures appear as data lands.

Usage (from project root):
    python 05_code/analysis/plot_results.py
"""

import os
import csv

import matplotlib
matplotlib.use("Agg")  # no display needed; just save files
import matplotlib.pyplot as plt


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DATA = os.path.join(ROOT, "03_data", "processed", "measurements.csv")
FIGS = os.path.join(ROOT, "04_images", "figures")


def load_rows():
    with open(DATA, newline="") as f:
        return list(csv.DictReader(f))


def as_float(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def pairs(rows, xcol, ycol):
    """Return (x, y) lists for rows where both columns parse as numbers."""
    xs, ys = [], []
    for r in rows:
        x, y = as_float(r.get(xcol)), as_float(r.get(ycol))
        if x is not None and y is not None:
            xs.append(x)
            ys.append(y)
    return xs, ys


def scatter(rows, xcol, ycol, xlabel, ylabel, title, fname):
    xs, ys = pairs(rows, xcol, ycol)
    if len(xs) < 2:
        print(f"[skip] {title}: need >=2 points, have {len(xs)}")
        return
    plt.figure(figsize=(6, 4))
    plt.scatter(xs, ys, s=60, edgecolor="black")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    out = os.path.join(FIGS, fname)
    plt.savefig(out, dpi=150)
    plt.close()
    print(f"[ok]   wrote {out}")


def main():
    os.makedirs(FIGS, exist_ok=True)
    rows = load_rows()
    print(f"Loaded {len(rows)} rows from {DATA}\n")

    # Each of these renders only once the relevant measurements exist.
    scatter(rows, "target_voltage_V", "mean_gray_intensity",
            "Anodizing voltage (V)", "Mean gray intensity (darker = more dye)",
            "Color uptake vs. voltage", "color_vs_voltage.png")

    scatter(rows, "anodize_time_min", "mean_gray_intensity",
            "Anodizing time (min)", "Mean gray intensity",
            "Color uptake vs. time", "color_vs_time.png")

    scatter(rows, "grit", "contact_angle_deg",
            "Surface prep grit", "Water contact angle (deg)",
            "Wettability vs. surface prep", "angle_vs_grit.png")

    scatter(rows, "bath_temp_C", "mean_gray_intensity",
            "Bath temperature (C)", "Mean gray intensity",
            "Color uptake vs. bath temperature", "color_vs_temp.png")

    print("\nDone. Empty plots above just mean that data isn't collected yet.")


if __name__ == "__main__":
    main()
