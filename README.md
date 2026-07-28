# dms-utils

DankMaterialShell utility scripts.

## extract_dms_theme.py

Extract the current auto-generated DMS theme (`dms-colors.json`) into a custom theme JSON file.

```bash
python3 extract_dms_theme.py
python3 extract_dms_theme.py -o ~/my-theme.json
python3 extract_dms_theme.py -n "Jade Theme"
```

Edit the output file, then load in DMS: Settings → Theme Color → Custom.

## fcitx5/ — Fcitx5 DMS Theme

Dynamic Fcitx5 theme that syncs with DMS/Matugen colors and layout.

```bash
cd fcitx5 && ./install.sh
```

See `fcitx5/README.md` for details.
