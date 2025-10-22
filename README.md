# Base16 Modus Themes

Base16 color schemes based on the excellent [Modus themes](https://github.com/protesilaos/modus-themes) for GNU Emacs by Protesilaos Stavrou.

## About

The Modus themes are highly accessible themes that conform with the highest standard for color contrast accessibility between background and foreground values (WCAG AAA). These base16 adaptations preserve the carefully chosen color palettes while mapping them to the base16 specification.

## Available Schemes

### Light Themes (Operandi variants)
- **modus-operandi** - Elegant theme with a white background
- **modus-operandi-tinted** - Operandi with a slightly tinted background
- **modus-operandi-deuteranopia** - Optimized for deuteranopia (red-green color blindness)
- **modus-operandi-tritanopia** - Optimized for tritanopia (blue-yellow color blindness)

### Dark Themes (Vivendi variants)
- **modus-vivendi** - Elegant theme with a black background
- **modus-vivendi-tinted** - Vivendi with a slightly tinted background
- **modus-vivendi-deuteranopia** - Optimized for deuteranopia (red-green color blindness)
- **modus-vivendi-tritanopia** - Optimized for tritanopia (blue-yellow color blindness)

## Base16 Color Mapping

The Modus theme colors are mapped to base16 as follows:

### Background/Foreground Colors
- **base00**: Default background (`bg-main`)
- **base01**: Lighter/darker background for status bars (`bg-dim`)
- **base02**: Selection background (`bg-active`)
- **base03**: Comments and secondary text (`fg-dim`)
- **base04**: Dark foreground for UI elements (`fg-alt`)
- **base05**: Default foreground text (`fg-main`)
- **base06**: Light foreground (rarely used, same as base05)
- **base07**: Lightest foreground (rarely used, same as base05)

### Accent Colors
- **base08**: Variables, XML tags, markup lists (`red`)
- **base09**: Integers, booleans, constants (`yellow-warmer`)
- **base0A**: Classes, bold markup, search highlights (`yellow`)
- **base0B**: Strings, inherited classes, inserted diffs (`green`)
- **base0C**: Support, regular expressions, escape chars (`cyan`)
- **base0D**: Functions, methods, headings (`blue`)
- **base0E**: Keywords, storage, selectors (`magenta`)
- **base0F**: Deprecated, special tags (`red-cooler`)

## Usage

These schemes follow the [base16 specification](https://github.com/tinted-theming/home/blob/main/styling.md) and can be used with any base16-compatible template system.

### With base16 Builders

Use these YAML files with base16 template builders like:
- [base16-builder-go](https://github.com/tinted-theming/base16-builder-go)
- [base16-builder-python](https://github.com/base16-project/base16-builder-python)

### Manual Installation

Each YAML file contains the complete color scheme definition that can be used to generate themes for various applications including:
- Terminal emulators (iTerm2, Alacritty, kitty, etc.)
- Text editors (Vim, Neovim, Emacs, VS Code, etc.)
- Shell prompts and other CLI tools

## Color Authenticity

All colors in these schemes are taken directly from the original Modus themes - no colors have been invented or modified. This ensures the same careful color contrast and accessibility considerations that make the original Modus themes exceptional.

## Credits

- **Modus Themes**: Created by [Protesilaos Stavrou](https://protesilaos.com/)
- **Base16 System**: Created by [Chris Kempson](https://github.com/chriskempson)
- **Adaptation**: base16 mapping and conversion

## License

The Modus themes are part of GNU Emacs and are licensed under the GNU General Public License v3.0 or later.

These base16 adaptations are provided under the same terms to maintain compatibility with the original work.

## Links

- [Modus Themes Repository](https://github.com/protesilaos/modus-themes)
- [Modus Themes Documentation](https://protesilaos.com/emacs/modus-themes)
- [Base16 Specification](https://github.com/tinted-theming/home/blob/main/styling.md)
- [Tinted Theming Project](https://github.com/tinted-theming)
