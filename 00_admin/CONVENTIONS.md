# Naming Conventions

One convention, used everywhere: data rows, photo filenames, notebook entries. The coupon ID
is the thread that ties a physical piece of aluminum to its data and its pictures.

## Coupon ID

`<batch>-<replicate>`  →  e.g. `B0-1`, `B2-2`

- **batch:** B0 (baseline), B1, B2, … per the experiment matrix.
- **replicate:** 1, 2, … duplicates within a batch.

Scribe this ID into a corner of the physical coupon before any processing.

## Image filenames

`<couponID>_<type>_<stage>.jpg`

| Part   | Values                                             | Example          |
|--------|----------------------------------------------------|------------------|
| type   | `face` (color), `angle` (contact angle), `wear`    | `B2-1_face_post` |
| stage  | `pre`, `post`, `seal`, or a number for wear strokes| `B2-1_wear_200`  |

Examples:
- `B0-1_face_post.jpg`  → finished coupon face, in `04_images/coupons/`
- `B2-2_angle_post.jpg` → droplet photo after anodizing, in `04_images/contact-angle/`
- `B5-1_wear_0.jpg` / `B5-1_wear_200.jpg` → before/after 200 strokes, in `04_images/wear/`
- any ruined coupon → also copy the photo to `04_images/failures/` with a `_FAIL` suffix

## Data files

- Per-session raw capture: `03_data/raw/session_YYYY-MM-DD.csv`
- ImageJ color export:      `03_data/raw/imagej_<couponID>.csv`
- The cleaned master:       `03_data/processed/measurements.csv`

## Notebook entries

- One file per session: `02_lab-notebook/YYYY-MM-DD_session-N.md`
- Always dated, always includes a "Problems / surprises" section.

## Dates

Always ISO format: `YYYY-MM-DD` (e.g. `2026-07-11`). Sorts correctly, never ambiguous.
