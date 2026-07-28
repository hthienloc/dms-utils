# dms-utils

DankMaterialShell utility scripts.

## extract_dms_theme.py

Extract current auto-generated DMS theme into a custom theme JSON file.

```bash
python3 extract_dms_theme.py
python3 extract_dms_theme.py -o ~/my-theme.json -n "Jade Theme"
```

Edit output, then load in DMS: Settings → Theme Color → Custom.

## generate_fcitx5_theme.py

Generate a Fcitx5 theme that syncs with DMS/Matugen colors and layout.

```bash
python3 generate_fcitx5_theme.py
```

## generate_vesktop_theme.py

Generate a Vesktop/Vencord theme (CSS) from DMS auto-generated colors.

```bash
python3 generate_vesktop_theme.py                          # dark mode → flatpak path
python3 generate_vesktop_theme.py --mode light              # light mode
python3 generate_vesktop_theme.py --stdout                  # print to stdout
```

## generate_spicetify_theme.py

Generate a Spicetify theme (color.ini) from DMS auto-generated colors.

```bash
python3 generate_spicetify_theme.py                        # install + prompt to apply
python3 generate_spicetify_theme.py --name "dms-jade"      # custom theme name
python3 generate_spicetify_theme.py --skip-apply           # install only
python3 generate_spicetify_theme.py --stdout               # print to stdout
```
