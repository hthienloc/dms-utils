#!/usr/bin/env python3
"""Extract current DMS auto-generated theme to a custom theme JSON file.

Usage:
  python3 extract_dms_theme.py                         # default: ~/dms-extracted-theme.json
  python3 extract_dms_theme.py -o ~/my-jade-theme.json # custom output path
  python3 extract_dms_theme.py -i 1                    # use matugen second-guess (run matugen with index=1 first)
"""

import argparse
import json
import os
import subprocess
import sys

DMS_COLORS_PATH = os.path.expanduser("~/.cache/DankMaterialShell/dms-colors.json")

MD3_TO_THEME = {
    "primary": "primary",
    "primaryText": "on_primary",
    "primaryContainer": "primary_container",
    "secondary": "secondary",
    "tertiary": "tertiary",
    "surface": "surface",
    "surfaceText": "on_surface",
    "surfaceVariant": "surface_variant",
    "surfaceVariantText": "on_surface_variant",
    "surfaceTint": "surface_tint",
    "background": "background",
    "backgroundText": "on_background",
    "outline": "outline",
    "outlineVariant": "outline_variant",
    "surfaceContainer": "surface_container",
    "surfaceContainerLow": "surface_container_low",
    "surfaceContainerLowest": "surface_container_lowest",
    "surfaceContainerHigh": "surface_container_high",
    "surfaceContainerHighest": "surface_container_highest",
    "surfaceBright": "surface_bright",
    "surfaceDim": "surface_dim",
    "error": "error",
    "errorContainer": "error_container",
    "scrim": "scrim",
    "shadow": "shadow",
    "inverseSurface": "inverse_surface",
    "inverseOnSurface": "inverse_on_surface",
    "inversePrimary": "inverse_primary",
    "primaryFixed": "primary_fixed",
    "primaryFixedDim": "primary_fixed_dim",
    "onPrimaryFixed": "on_primary_fixed",
    "onPrimaryFixedVariant": "on_primary_fixed_variant",
    "secondaryFixed": "secondary_fixed",
    "secondaryFixedDim": "secondary_fixed_dim",
    "onSecondaryFixed": "on_secondary_fixed",
    "onSecondaryFixedVariant": "on_secondary_fixed_variant",
    "tertiaryFixed": "tertiary_fixed",
    "tertiaryFixedDim": "tertiary_fixed_dim",
    "onTertiaryFixed": "on_tertiary_fixed",
    "onTertiaryFixedVariant": "on_tertiary_fixed_variant",
}

HARDCODED = {
    "warning": "#FF9800",
    "info": "#2196F3",
    "success": "#4CAF50",
}


def read_dms_colors(path):
    with open(path) as f:
        return json.load(f)


def extract_mode_colors(dms_data, mode):
    colors = dms_data.get("colors", {}).get(mode, {})
    out = {}
    for theme_key, md3_key in MD3_TO_THEME.items():
        val = colors.get(md3_key)
        if val:
            out[theme_key] = val
    for key, val in HARDCODED.items():
        out[key] = val
    out["name"] = f"Extracted {mode.title()}"
    return out


def extract_theme(dms_data, name=None):
    dark = extract_mode_colors(dms_data, "dark")
    light = extract_mode_colors(dms_data, "light")
    if name:
        dark["name"] = f"{name} Dark"
        light["name"] = f"{name} Light"
    return {"dark": dark, "light": light}


def run_matugen_with_index(source_index=0):
    """Re-run matugen with a different --source-color-index to preview other color candidates."""
    cmd = [
        "matugen", "image",
        "--source-color-index", str(source_index),
        "--type", "scheme-tonal-spot",
        "--json", "hex",
    ]
    print(f"Running: {' '.join(cmd)}", file=sys.stderr)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: matugen failed:\n{result.stderr}", file=sys.stderr)
        sys.exit(1)
    return json.loads(result.stdout)


def main():
    parser = argparse.ArgumentParser(description="Extract DMS auto-generated theme to custom theme JSON")
    parser.add_argument("-o", "--output", default=os.path.expanduser("~/dms-extracted-theme.json"),
                        help="Output path (default: ~/dms-extracted-theme.json)")
    parser.add_argument("-n", "--name", default="My Theme", help="Theme name")
    args = parser.parse_args()

    if not os.path.exists(DMS_COLORS_PATH):
        print(f"Error: {DMS_COLORS_PATH} not found. Run DMS with dynamic theme first.", file=sys.stderr)
        sys.exit(1)

    dms_data = read_dms_colors(DMS_COLORS_PATH)
    theme = extract_theme(dms_data, args.name)

    os.makedirs(os.path.dirname(os.path.abspath(args.output)) or ".", exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(theme, f, indent=2)

    print(f"Theme extracted to: {args.output}")
    print(f"\nTo use:")
    print(f"  1. Edit {args.output} and change colors (e.g. swap primary/secondary to jade green)")
    print(f"  2. In DMS: Settings → Theme Color → Custom → select {args.output}")
    print(f"\nTip: To use matugen's second-guess color instead, run:")
    print(f"    matugen image /path/to/wallpaper --source-color-index 1 --json hex")
    print(f"  Then re-run this script.")


if __name__ == "__main__":
    main()
