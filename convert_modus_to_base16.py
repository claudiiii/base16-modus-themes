#!/usr/bin/env python3
"""
Convert Modus themes palettes to base16 color schemes.
"""

import re
import yaml
from pathlib import Path

def parse_palette(file_path, palette_name):
    """Extract color palette from an elisp theme file."""
    with open(file_path, 'r') as f:
        content = f.read()

    # Find the palette definition
    pattern = rf'\(defconst {palette_name}\s*\(append\s*\'?\(\s*(.*?)\)\s*modus-themes-common-palette-mappings\)'
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return None

    palette_content = match.group(1)

    # Extract color definitions (name "#hexcolor")
    color_pattern = r'\(\s*([a-zA-Z0-9_-]+)\s+"(#[0-9a-fA-F]{6})"\s*\)'
    colors = {}

    for match in re.finditer(color_pattern, palette_content):
        name = match.group(1)
        hex_value = match.group(2).lower()
        colors[name] = hex_value

    return colors

def map_to_base16(colors, theme_type):
    """
    Map modus theme colors to base16 specification.

    theme_type: 'dark' or 'light'
    """
    if theme_type == 'dark':
        # For dark themes, go from darkest to lightest
        return {
            'base00': colors.get('bg-main', '#000000'),           # Default Background
            'base01': colors.get('bg-dim', '#1e1e1e'),            # Lighter Background
            'base02': colors.get('bg-active', '#303030'),         # Selection Background
            'base03': colors.get('fg-dim', '#989898'),            # Comments
            'base04': colors.get('fg-alt', '#c0c0c0'),            # Dark Foreground
            'base05': colors.get('fg-main', '#ffffff'),           # Default Foreground
            'base06': colors.get('blue-faint', '#82b0ec'),        # Light Foreground (rarely used)
            'base07': colors.get('cyan-faint', '#9ac8e0'),        # Lightest Foreground (rarely used)
            'base08': colors.get('red', '#ff5f59'),               # Variables, Tags
            'base09': colors.get('yellow-warmer', '#fec43f'),     # Integers, Constants
            'base0A': colors.get('yellow', '#d0bc00'),            # Classes, Bold
            'base0B': colors.get('green', '#44bc44'),             # Strings
            'base0C': colors.get('cyan', '#00d3d0'),              # Support, Regex
            'base0D': colors.get('blue', '#2fafff'),              # Functions
            'base0E': colors.get('magenta', '#feacd0'),           # Keywords
            'base0F': colors.get('red-cooler', '#ff7f86'),        # Deprecated
        }
    else:  # light
        # For light themes, colors go from lightest to darkest
        return {
            'base00': colors.get('bg-main', '#ffffff'),           # Default Background
            'base01': colors.get('bg-dim', '#f2f2f2'),            # Lighter Background
            'base02': colors.get('bg-active', '#c4c4c4'),         # Selection Background
            'base03': colors.get('fg-dim', '#595959'),            # Comments
            'base04': colors.get('fg-alt', '#193668'),            # Dark Foreground
            'base05': colors.get('fg-main', '#000000'),           # Default Foreground
            'base06': colors.get('blue-faint', '#003497'),        # Darker Foreground (rarely used)
            'base07': colors.get('cyan-faint', '#005077'),        # Darkest Foreground (rarely used)
            'base08': colors.get('red', '#a60000'),               # Variables, Tags
            'base09': colors.get('yellow-warmer', '#884900'),     # Integers, Constants
            'base0A': colors.get('yellow', '#6f5500'),            # Classes, Bold
            'base0B': colors.get('green', '#006800'),             # Strings
            'base0C': colors.get('cyan', '#005e8b'),              # Support, Regex
            'base0D': colors.get('blue', '#0031a9'),              # Functions
            'base0E': colors.get('magenta', '#721045'),           # Keywords
            'base0F': colors.get('red-cooler', '#a0132f'),        # Deprecated
        }

def create_base16_scheme(theme_name, scheme_name, author, base16_colors):
    """Create a base16 scheme dictionary."""
    return {
        'system': 'base16',
        'name': scheme_name,
        'author': author,
        'variant': 'dark' if 'vivendi' in theme_name.lower() else 'light',
        'palette': {
            f'base{i:02X}': base16_colors[f'base{i:02X}']
            for i in range(16)
        }
    }

def main():
    modus_dir = Path('/tmp/modus-themes')
    output_dir = Path('/home/user/base16-modus-themes')
    output_dir.mkdir(exist_ok=True)

    themes = [
        ('modus-operandi', 'modus-themes-operandi-palette', 'Modus Operandi', 'light'),
        ('modus-operandi-tinted', 'modus-themes-operandi-tinted-palette', 'Modus Operandi Tinted', 'light'),
        ('modus-operandi-deuteranopia', 'modus-themes-operandi-deuteranopia-palette', 'Modus Operandi Deuteranopia', 'light'),
        ('modus-operandi-tritanopia', 'modus-themes-operandi-tritanopia-palette', 'Modus Operandi Tritanopia', 'light'),
        ('modus-vivendi', 'modus-themes-vivendi-palette', 'Modus Vivendi', 'dark'),
        ('modus-vivendi-tinted', 'modus-themes-vivendi-tinted-palette', 'Modus Vivendi Tinted', 'dark'),
        ('modus-vivendi-deuteranopia', 'modus-themes-vivendi-deuteranopia-palette', 'Modus Vivendi Deuteranopia', 'dark'),
        ('modus-vivendi-tritanopia', 'modus-themes-vivendi-tritanopia-palette', 'Modus Vivendi Tritanopia', 'dark'),
    ]

    for theme_name, palette_var, scheme_name, theme_type in themes:
        print(f"Processing {theme_name}...")

        # Parse the palette
        colors = parse_palette(modus_dir / 'modus-themes.el', palette_var)

        if not colors:
            print(f"  Warning: Could not find palette {palette_var}")
            continue

        print(f"  Found {len(colors)} colors")

        # Map to base16
        base16_colors = map_to_base16(colors, theme_type)

        # Create scheme
        scheme = create_base16_scheme(
            theme_name,
            scheme_name,
            'Protesilaos Stavrou (adapted to base16)',
            base16_colors
        )

        # Write YAML file
        output_file = output_dir / f'base16-{theme_name}.yaml'
        with open(output_file, 'w') as f:
            f.write('# Base16 ' + scheme_name + '\n')
            f.write('# Author: ' + scheme['author'] + '\n\n')
            f.write('scheme: "' + scheme['name'] + '"\n')
            f.write('author: "' + scheme['author'] + '"\n')

            # Write colors
            for i in range(16):
                key = f'base{i:02X}'
                value = scheme['palette'][key]
                f.write(f'{key}: "{value}"\n')

        print(f"  Created {output_file}")

    print("\nDone! Created base16 schemes for all Modus themes.")

if __name__ == '__main__':
    main()
