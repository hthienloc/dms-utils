# dms-utils

DankMaterialShell utility scripts.

## Scripts

### extract_dms_theme.py

Extract the current auto-generated DMS theme (`dms-colors.json`) into a custom theme JSON file.

**Usage:**

```bash
python3 extract_dms_theme.py
# outputs to ~/dms-extracted-theme.json

python3 extract_dms_theme.py -o ~/my-theme.json
python3 extract_dms_theme.py -n "Jade Theme"
```

Edit the output file, then load in DMS: Settings → Theme Color → Custom.
