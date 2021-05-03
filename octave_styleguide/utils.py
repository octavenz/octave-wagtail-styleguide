import re
import os
from pathlib import Path

from django.utils.text import capfirst
from django.template.loaders.app_directories import get_app_template_dirs
from django.conf import settings

from .settings import ICON_DIR, COLORS_CONFIG_FILE, default_template_routes


def get_icons():
    return [path.stem for path in Path(ICON_DIR).glob('**/*.svg')]


def parse_color_from_line(line):
    match_re = r"[\"']?([\w\-_]+)[\"']?\s*:\s*([\w#\"'\-(),\.\s]+),.*$"

    matches = re.search(match_re, line.strip(), re.IGNORECASE)

    if matches:
        return matches[1], matches[2]

    return None, None


def parse_colors():
    colors = {}

    with open(COLORS_CONFIG_FILE, "r") as f:
        in_colors_dict = False

        for line in f:
            # $colors variable name indicates start of dict
            if '$colors' in line:
                in_colors_dict = True
                continue

            if in_colors_dict:
                # semicolon indicates end of the dict so exit here.
                if ';' in line:
                    break

                name, value = parse_color_from_line(line)

                if name and value:
                    colors[name] = value

        return colors


def get_routes_from_templates():
    template_dir_list = []
    template_list = []

    for template_dir in get_app_template_dirs('templates'):
        if settings.ROOT_DIR in template_dir:
            template_dir_list.append(template_dir)

    for template_dir in template_dir_list:
        for base_dir, dirnames, filenames in os.walk(template_dir):
            if 'templates/styleguide' in base_dir:
                for filename in filenames:
                    template_list.append(filename.replace('.html', ''))

    return template_list


def get_styleguide_routes():
    all_routes = get_routes_from_templates()
    all_routes = [r for r in all_routes if r not in default_template_routes]
    all_routes.sort()

    # default items at top
    return default_template_routes + all_routes


def as_title(slug):
    title = slug.replace('_', ' ').replace('-', ' ')
    return capfirst(title)


def get_styleguide_menu():
    menu = []
    for item in get_styleguide_routes():
        menu.append({
            'title': as_title(item),
            'url': f'/styleguide/{item}/',
            'id': item
        })
    return menu

