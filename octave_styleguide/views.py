from django.template.response import TemplateResponse
from django.views.generic import View

from .utils import get_icons, parse_colors, get_styleguide_menu, as_title


class StyleguideView(View):
    def get(self, request, template_name='typography'):
        return TemplateResponse(
            request,
            self.get_template(template_name),
            self.get_context(template_name),
        )

    def get_context(self, template_name):
        return {
            'ICONS': get_icons(),
            'COLORS': parse_colors(),
            'STYLEGUIDE_MENU': get_styleguide_menu(),
            'page_title': as_title(template_name),
        }

    @staticmethod
    def get_template(template_name):
        return f'styleguide/{ template_name }.html'

