# ImageJ Measurement Notes

ImageJ is how I turn coupon photos into numbers. The whole point is **repeatability** — every
coupon measured the exact same way, or the comparison is meaningless.

## Color (mean intensity) — the core measurement

1. Open the standardized coupon photo (`04_images/coupons/<id>_face_post.jpg`).
2. **Image → Type → 8-bit** (converts to grayscale so I get one intensity number).
3. Select a fixed-size rectangle on a clean part of the coupon face. Keep the selection size
   identical across all coupons — make a note of the pixel dimensions and reuse them.
4. **Analyze → Measure** (or press `M`). Read the **Mean** value.
5. Record that Mean in `measurements.csv` under `mean_gray_intensity`. Save the raw export to
   `03_data/raw/imagej_<id>.csv`.

Lower mean = darker = more dye uptake.

## Contact angle (wettability)

1. Open the side-on droplet photo (`04_images/contact-angle/<id>_angle_post.jpg`).
2. Use the **Angle tool**: click along the surface, then the vertex at the droplet edge, then
   up the tangent of the droplet. Read the angle.
3. There's also a "Contact Angle" plugin if I want to install it — more rigorous, optional.
4. Record under `contact_angle_deg`.

## Repeatability checklist (tape this up)
- Same camera distance, same lighting, same background for every photo.
- Same 8-bit conversion step every time.
- Same selection size for color; note it here once I pick it: __________ px.
- Measure each coupon twice; if the two readings disagree a lot, my setup isn't consistent.

## Setting a measurement macro (optional, once I'm comfortable)
ImageJ can record a macro (**Plugins → Macros → Record**) so the 8-bit + measure steps run
identically with one click. Save any macro here as `measure_color.ijm`.
