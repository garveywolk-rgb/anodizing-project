"""
720 Rule helper for anodizing.

The 720 Rule: 720 amp-minutes per square foot of surface area produces 1 mil
(0.001 in / 25.4 microns) of anodic oxide. It is essentially Faraday's Law of
electrolysis with unit conversions baked in, and gives a good estimate for
sulfuric-acid anodizing regardless of alloy or bath concentration.

    thickness_mil = (current_density_ASF * time_min) / 720

Use this before each run to figure out either the time needed or the current to
target for a desired oxide thickness, and to fill in surface_area_ft2 in the dataset.

Run directly for an example:  python anodizing_720.py
"""


def coupon_area_ft2(length_in, width_in, both_sides=True):
    """Surface area of a flat rectangular coupon in square feet.

    both_sides=True counts front and back faces (current anodizes all wetted
    surface). Edges are small and usually ignored for a thin coupon.
    """
    faces = 2 if both_sides else 1
    area_in2 = length_in * width_in * faces
    return area_in2 / 144.0  # 144 sq in per sq ft


def time_for_thickness(thickness_mil, current_density_asf):
    """Minutes needed to reach a target oxide thickness at a given current density."""
    return 720.0 * thickness_mil / current_density_asf


def target_current_amps(current_density_asf, area_ft2):
    """The actual current (amps) to set, given a target current density and part area."""
    return current_density_asf * area_ft2


def thickness_reached(current_density_asf, time_min):
    """Oxide thickness (mils) produced after a run."""
    return current_density_asf * time_min / 720.0


def plan_run(length_in, width_in, current_density_asf=12.0, target_mil=0.5):
    """Print a full run plan for one coupon geometry."""
    area = coupon_area_ft2(length_in, width_in)
    t = time_for_thickness(target_mil, current_density_asf)
    amps = target_current_amps(current_density_asf, area)
    print(f"Coupon {length_in}x{width_in} in  |  area (both faces) = {area:.4f} ft^2")
    print(f"Target: {target_mil} mil oxide at {current_density_asf} ASF")
    print(f"  -> anodize for {t:.1f} min")
    print(f"  -> set ~{amps:.3f} A (constant current)")
    return {"area_ft2": area, "time_min": t, "current_A": amps}


if __name__ == "__main__":
    # Example: standard 1 x 3 in coupon, 12 ASF, 0.5 mil target
    plan_run(3.0, 1.0, current_density_asf=12.0, target_mil=0.5)
