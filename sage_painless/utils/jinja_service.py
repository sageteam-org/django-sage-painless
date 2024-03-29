"""
django-sage-painless - Jinja Templating Main Class

:author: Mehran Rahmanzadeh (mrhnz13@gmail.com)
"""
from jinja2 import Environment


class JinjaHandler:
    env = Environment(autoescape=False, optimized=False)

    def load_template(self, template_path):
        """
        load jinja template from template_path
        """
        with open(template_path, 'r', encoding='utf8') as t:
            template = self.env.from_string(t.read())
        return template

    def stream_to_template(self, output_path, template_path, data=None):
        """
        generate output file using template and data
        """
        template = self.load_template(template_path)
        with open(output_path, 'w', encoding='utf8') as o:
            if data:
                template.stream(
                    **data
                ).dump(o)
            else:
                template.stream().dump(o)
