#!/usr/bin/env python3
"""Generate Spicetify theme from DMS auto-generated colors.

Reads ~/.cache/DankMaterialShell/dms-colors.json and produces a Spicetify color.ini.

Usage:
  python3 generate_spicetify_theme.py                              # dark mode, install + apply
  python3 generate_spicetify_theme.py --mode light                 # light mode
  python3 generate_spicetify_theme.py --name "dms"                # theme folder name
  python3 generate_spicetify_theme.py --stdout                    # print to stdout only
  python3 generate_spicetify_theme.py --skip-apply                # install but don't run spicetify apply
"""

import argparse
import json
import os
import subprocess
import sys

DMS_COLORS_PATH = os.path.expanduser("~/.cache/DankMaterialShell/dms-colors.json")
SPICETIFY_THEMES_DIR = os.path.expanduser("~/.config/spicetify/Themes")

COLOR_INI_TEMPLATE = """[color]
text = {on_surface}
subtext = {on_surface_variant}
main = {surface}
sidebar = {surface_container}
player = {surface_container}
card = {surface_container_high}
shadow = 000000
selected-row = {surface_container_highest}
highlight = {primary}
button = {primary}
button-active = {primary_container}
button-disabled = {outline_variant}
tab-active = {primary}
notification = {tertiary}
notification-error = {error}
misc = {secondary}
"""


def read_dms_colors(path):
    with open(path) as f:
        return json.load(f)


def strip_hash(h):
    return h.lstrip("#")


def extract_colors(dms_data, mode="dark"):
    colors = dms_data.get("colors", {}).get(mode, {})
    return {
        "surface": strip_hash(colors.get("surface", "#1a1c1e")),
        "surface_container": strip_hash(colors.get("surface_container", "#1e2023")),
        "surface_container_low": strip_hash(colors.get("surface_container_low", "#181a1d")),
        "surface_container_high": strip_hash(colors.get("surface_container_high", "#292b2f")),
        "surface_container_highest": strip_hash(colors.get("surface_container_highest", "#343740")),
        "on_surface": strip_hash(colors.get("on_surface", "#e3e8ef")),
        "on_surface_variant": strip_hash(colors.get("on_surface_variant", "#c4c7c5")),
        "primary": strip_hash(colors.get("primary", "#42a5f5")),
        "primary_container": strip_hash(colors.get("primary_container", "#0d47a1")),
        "secondary": strip_hash(colors.get("secondary", "#8ab4f8")),
        "tertiary": strip_hash(colors.get("tertiary", "#efb8c8")),
        "error": strip_hash(colors.get("error", "#F2B8B5")),
        "outline": strip_hash(colors.get("outline", "#8e918f")),
        "outline_variant": strip_hash(colors.get("outline_variant", colors.get("surface_variant", "#44464f"))),
    }


def generate_theme(colors):
    return COLOR_INI_TEMPLATE.format(**colors)


def install_theme(theme_dir, content):
    os.makedirs(theme_dir, exist_ok=True)
    path = os.path.join(theme_dir, "color.ini")
    with open(path, "w") as f:
        f.write(content)
    print(f"Written: {path}")
    return path


def spicetify_apply():
    try:
        subprocess.run(["spicetify", "apply"], check=True)
        print("Spicetify: applied.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Spicetify apply failed: {e}", file=sys.stderr)
        return False
    except FileNotFoundError:
        print("spicetify not found on PATH.", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="Generate Spicetify theme from DMS colors")
    parser.add_argument("-m", "--mode", choices=["dark", "light"], default="dark",
                        help="Color mode (default: dark)")
    parser.add_argument("-n", "--name", default="dms",
                        help="Theme directory name (default: dms)")
    parser.add_argument("--stdout", action="store_true", help="Print color.ini to stdout")
    parser.add_argument("--skip-apply", action="store_true",
                        help="Install but don't run spicetify apply")
    args = parser.parse_args()

    if not os.path.exists(DMS_COLORS_PATH):
        print(f"Error: {DMS_COLORS_PATH} not found.", file=sys.stderr)
        sys.exit(1)

    dms_data = read_dms_colors(DMS_COLORS_PATH)
    colors = extract_colors(dms_data, args.mode)
    ini = generate_theme(colors)

    if args.stdout:
        print(ini, end="")
        return

    theme_dir = os.path.join(SPICETIFY_THEMES_DIR, args.name)
    install_theme(theme_dir, ini)

    print(f"\nTo activate:\n  spicetify config current_theme {args.name}\n  spicetify apply")

    if not args.skip_apply:
        resp = input("\nRun spicetify apply now? (y/N): ").lower()
        if resp == "y":
            spicetify_apply()


if __name__ == "__main__":
    main()
