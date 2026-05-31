# Data Dictionary — measurements.csv

One row per coupon. Independent variables are things I set; dependent variables are things I
measure. Blank cells get filled in as the project progresses.

| Column              | Type    | Meaning                                                       |
|---------------------|---------|---------------------------------------------------------------|
| coupon_id           | text    | Unique ID, `<batch>-<replicate>` (e.g. B2-1)                  |
| batch               | text    | Batch group (B0, B1, …)                                       |
| date                | date    | ISO date the coupon was run (YYYY-MM-DD)                      |
| alloy               | text    | Aluminum alloy — held constant at 6061                        |
| length_in           | number  | Coupon length, inches                                         |
| width_in            | number  | Coupon width, inches                                          |
| thickness_in        | number  | Coupon thickness, inches                                      |
| surface_area_ft2    | number  | Wetted area, ft² (both faces). Compute with anodizing_720.py  |
| grit                | number  | Final sanding grit (INDEPENDENT variable)                     |
| acid_pct            | number  | Bath sulfuric concentration, % (held ~constant)               |
| bath_temp_C         | number  | Electrolyte temperature, °C (INDEPENDENT variable)            |
| target_voltage_V    | number  | Voltage I aimed for (INDEPENDENT variable)                    |
| observed_voltage_V  | number  | Voltage actually read during the run                          |
| target_current_A    | number  | Current I aimed for (from 720 rule)                           |
| current_density_ASF | number  | Current per area, amps/ft²                                    |
| anodize_time_min    | number  | Anodizing duration, minutes (INDEPENDENT variable)            |
| target_thickness_mil| number  | Oxide thickness target, mils (from 720 rule)                  |
| dye_color           | text    | Dye used (held constant where possible)                       |
| dye_time_min        | number  | Time in dye, minutes (held constant)                          |
| dye_temp_C          | number  | Dye temperature, °C (held constant)                           |
| seal_time_min       | number  | Time in seal bath, minutes (held constant)                    |
| mean_gray_intensity | number  | DEPENDENT: ImageJ mean intensity of coupon face (color depth) |
| contact_angle_deg   | number  | DEPENDENT: water contact angle, degrees (wettability)         |
| wear_strokes        | number  | Strokes applied in wear test                                  |
| wear_delta          | number  | DEPENDENT: change in intensity/gloss after wear               |
| observations        | text    | Plain-language notes; cross-ref the notebook entry            |

## Notes
- **Don't delete the seed rows** — they encode the planned matrix. Fill them in; add rows for
  any stretch batches.
- `mean_gray_intensity`: lower = darker = more dye uptake (loosely, thicker/more-porous oxide).
- Keep raw ImageJ exports in `03_data/raw/` and transcribe the summary number here.
