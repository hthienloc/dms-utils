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
