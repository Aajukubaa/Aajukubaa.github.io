"""Helpers for defining and validating the portfolio's bento grids."""

from html import escape


SIZES = {
    "sm": (1, 1),
    "wide": (2, 1),
    "tall": (1, 2),
    "big": (2, 2),
    "full": (4, 1),
}

_TWO_COLUMN_SIZES = {
    "sm": (1, 1),
    "wide": (2, 1),
    "tall": (1, 2),
    "big": (2, 2),
    "full": (2, 1),
}


class BentoLayoutError(ValueError):
    """Raised when a bento layout contains unfilled grid cells."""


def tile(size, html, *, href=None, cls="", style=""):
    return {
        "size": size,
        "html": html,
        "href": href,
        "cls": cls,
        "style": style,
    }


def _dimensions(size, cols):
    if size not in SIZES:
        raise BentoLayoutError(f"Unknown bento size: {size}")
    if cols == 1:
        return 1, 1
    dimensions = _TWO_COLUMN_SIZES if cols == 2 else SIZES
    width, height = dimensions[size]
    return min(width, cols), height


def place(tiles, cols):
    """Return a dense row-major occupancy matrix of tile indexes and holes."""
    if cols < 1:
        raise ValueError("cols must be at least 1")
    grid = []
    for index, item in enumerate(tiles):
        width, height = _dimensions(item["size"], cols)
        row = column = 0
        while True:
            if column + width > cols:
                row += 1
                column = 0
                continue
            fits = all(
                target_row >= len(grid)
                or target_column >= len(grid[target_row])
                or grid[target_row][target_column] is None
                for target_row in range(row, row + height)
                for target_column in range(column, column + width)
            )
            if fits:
                break
            column += 1
            if column >= cols:
                row += 1
                column = 0
        while len(grid) < row + height:
            grid.append([None] * cols)
        for target_row in range(row, row + height):
            for target_column in range(column, column + width):
                grid[target_row][target_column] = index
    return grid


def validate(name, tiles):
    """Ensure the 4- and 2-column grids have no holes."""
    failures = []
    for cols in (4, 2):
        grid = place(tiles, cols)
        if any(cell is None for row in grid for cell in row):
            rows = [" ".join("." if cell is None else str(cell) for cell in row) for row in grid]
            failures.append(f"{cols} columns:\n" + "\n".join(rows))
    if failures:
        raise BentoLayoutError(
            f"Bento layout '{name}' has holes:\n" + "\n".join(failures)
        )
    return True


def render(tiles):
    """Render tile definitions to the HTML consumed by the detail modal."""
    rendered = []
    for item in tiles:
        classes = ["bento-tile"]
        if item.get("href"):
            classes.append("bento-tile-link")
        classes.append(f"size-{item['size']}")
        if item.get("cls"):
            classes.extend(item["cls"].split())
        class_attr = escape(" ".join(classes), quote=True)
        style_attr = f' style="{escape(item["style"], quote=True)}"' if item.get("style") else ""
        if item.get("href"):
            href = escape(item["href"], quote=True)
            rendered.append(
                f'<a href="{href}" target="_blank" rel="noopener" class="{class_attr}"{style_attr}>'
                f'{item["html"]}</a>'
            )
        else:
            rendered.append(
                f'<div class="{class_attr}"{style_attr}>{item["html"]}</div>'
            )
    return "\n".join(rendered)
