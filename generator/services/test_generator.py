import os

from django.conf import settings

from generator.classes.field import Field
from generator.classes.model import Model
from generator.classes.signal import Signal

from generator.services.jinja_service import JinjaHandler
from generator.services.json_service import JsonHandler
from generator.services.pep8_service import Pep8


class TestGenerator(JinjaHandler, JsonHandler, Pep8):
    """
    Create model/api tests for given diagram
    """

    FIELDS_KEYWORD = 'fields'
    TYPE_KEYWORD = 'type'
    VALIDATORS_KEYWORD = 'validators'
    FUNC_KEYWORD = 'func'
    ARG_KEYWORD = 'arg'
    TESTS_DIR = 'tests'

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
        signals = list()
        for table_name in diagram.keys():
            table = diagram.get(table_name)
            fields = self.get_table_fields(table)

            model = Model()
            model.name = table_name
            model_fields = list()

            for field_name in fields.keys():
                model_field = Field()
                model_field.name = field_name
                field_data = fields.get(field_name)

                for key in field_data.keys():

                    if key == self.TYPE_KEYWORD:
                        model_field.set_type(field_data.get(self.TYPE_KEYWORD))

                        if model_field.type == 'OneToOneField':
                            signal = Signal()
                            signal.set_signal('post_save', table_name, field_data.get('to'), field_name)
                            signals.append(signal)

                    elif key == self.VALIDATORS_KEYWORD:
                        for validator in field_data.get(self.VALIDATORS_KEYWORD):
                            model_field.add_validator(validator.get(self.FUNC_KEYWORD), validator.get(self.ARG_KEYWORD))

                    else:
                        value = field_data.get(key)
                        model_field.add_attribute(key, value)

                model_fields.append(model_field)

            model.fields = model_fields
            models.append(model)

        return models, signals

    def check_validator_support(self, models):
        """
        check models have validator
        """
        for model in models:
            for field in model.fields:
                if len(field.validators) > 0:
                    return True

        return False

    def create_dir_is_not_exists(self, directory):
        if not os.path.exists(f'{settings.BASE_DIR}/{self.app_label}/{directory}'):
            os.mkdir(f'{settings.BASE_DIR}/{self.app_label}/{directory}')

    def check_signal_support(self, models):
        """
        check models have one2one
        """
        for model in models:
            for field in model.fields:
                if field.type == 'OneToOneField':
                    return True

        return False

    def generate_tests(self, diagram_path):
        """
        stream tests to app_name/tests/*.py
        """
        diagram = self.load_json(diagram_path)
        models, signals = self.extract_models(diagram)

        self.create_dir_is_not_exists(self.TESTS_DIR)

        self.stream_to_template(
            output_path=f'{settings.BASE_DIR}/{self.app_label}/tests/test_model.py',
            template_path=f'{settings.BASE_DIR}/generator/templates/test_model.txt',  # TODO: Should be dynamic
            data={
                'app_name': self.app_label,
                'models': models,
                'signals': signals,
                'validator_support': self.check_validator_support(models),
                'signal_support': self.check_signal_support(models)
            }
        )

        self.fix_pep8(f'{settings.BASE_DIR}/{self.app_label}/tests/test_model.py')

        return True, 'Tests Generated Successfully. Changes are in this file:\ntest_model.py'
