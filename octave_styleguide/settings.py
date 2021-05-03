from django.conf import settings

ICON_DIR = settings.OCTAVE_STYLEGUIDE_ICON_DIR
COLORS_CONFIG_FILE = settings.OCTAVE_STYLEGUIDE_COLORS_CONFIG_FILE

default_template_routes = [
    'colors',
    'icons',
    'typography',
]
