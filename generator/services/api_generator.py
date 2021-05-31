import os

from django.conf import settings

from generator.classes.field import Field
from generator.classes.model import Model

from generator.utils.jinja_service import JinjaHandler
from generator.utils.json_service import JsonHandler
from generator.utils.pep8_service import Pep8


class APIGenerator(JinjaHandler, JsonHandler, Pep8):
    """
    Generate API serializers & viewsets
    """

    FIELDS_KEYWORD = 'fields'
    API_DIR = 'api'

    def __init__(self, app_label):
        self.app_label = app_label

    def get_table_fields(self, table):
        """
        extract fields
        """
        return table.get(self.FIELDS_KEYWORD)

    def extract_models(self, diagram):
        """
        extract models
        """
        models = list()
        for table_name in diagram.keys():
            table = diagram.get(table_name)
            fields = self.get_table_fields(table)

            model = Model()
            model.name = table_name
            model_fields = list()

            for field_name in fields.keys():
                model_field = Field()
                model_field.name = field_name
                model_fields.append(model_field)

            model.fields = model_fields
            models.append(model)

        return models

    def create_dir_is_not_exists(self, directory):
        if not os.path.exists(f'{settings.BASE_DIR}/{self.app_label}/{directory}'):
            os.mkdir(f'{settings.BASE_DIR}/{self.app_label}/{directory}')

    def add_urls_to_kernel(self):
        with open(f'{settings.BASE_DIR}/kernel/urls.py', 'a+') as f:
            f.writelines(f'\nurlpatterns.append(path("api/", include("{self.app_label}.{self.API_DIR}.urls")))')

    def generate_api(self, diagram_path):
        """
        stream serializers to app_name/api/serializers.py
        stream viewsets to app_name/api/views.py
        """
        diagram = self.load_json(diagram_path)
        models = self.extract_models(diagram)

        self.create_dir_is_not_exists(self.API_DIR)

        # stream to serializers.py
        self.stream_to_template(
            output_path=f'{settings.BASE_DIR}/{self.app_label}/api/serializers.py',
            template_path=f'{settings.BASE_DIR}/generator/templates/serializers.txt',
            data={
                'app_name': self.app_label,
                'models': models,
            }
        )

        # stream to views.py
        self.stream_to_template(
            output_path=f'{settings.BASE_DIR}/{self.app_label}/api/views.py',
            template_path=f'{settings.BASE_DIR}/generator/templates/views.txt',
            data={
                'app_name': self.app_label,
                'models': models,
            }
        )

        # stream to urls.py
        self.stream_to_template(
            output_path=f'{settings.BASE_DIR}/{self.app_label}/api/urls.py',
            template_path=f'{settings.BASE_DIR}/generator/templates/urls.txt',
            data={
                'app_name': self.app_label,
                'models': models,
            }
        )

        # self.add_urls_to_kernel()  # TODO: might be changed

        self.fix_pep8(f'{settings.BASE_DIR}/{self.app_label}/api/serializers.py')
        self.fix_pep8(f'{settings.BASE_DIR}/{self.app_label}/api/views.py')
        self.fix_pep8(f'{settings.BASE_DIR}/{self.app_label}/api/urls.py')
        # self.fix_pep8(f'{settings.BASE_DIR}/kernel/urls.py')

        return True, 'API Generated Successfully. Changes are in these files:\nserializers.py\nviews.py\nurls.py'
