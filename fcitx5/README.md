# Fcitx5 DMS Theme

Dynamic Fcitx5 theme synchronizing with **Dank Material Shell (DMS)** and **Matugen** colors/layout.
Inherits the sleek border style from [Ori-fcitx5](https://github.com/Reverier-Xu/Ori-fcitx5).

## Usage

```bash
python3 ../generate_fcitx5_theme.py
```

Or from repo root:

```bash
python3 generate_fcitx5_theme.py
```

Follow the prompts to install, then select **DMS** in Fcitx5 Configuration → Addons → Classic User Interface → Theme.

## Customization

Edit constants at the top of `generate_fcitx5_theme.py`:
- `HIGHLIGHT_V_PADDING` / `HIGHLIGHT_H_PADDING` — highlight box padding
- `PANEL_BORDER_WIDTH_OVERRIDE` — border thickness override

Template SVGs in `templates/` for further tweaks.
