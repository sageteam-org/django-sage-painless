import os

from django.test import TestCase
from django.conf import settings

from sage_painless.classes.admin import Admin
from sage_painless.services.admin_generator import AdminGenerator
from sage_painless.utils.json_service import JsonHandler

from tests import fixtures


class TestAdminGenerator(TestCase):
    def setUp(self) -> None:
        self.json_handler = JsonHandler()
        self.app_name = 'products'
        self.admin_generator = AdminGenerator()
        self.diagram_path = os.path.abspath(fixtures.__file__).replace('__init__.py', 'product_fixture.json')
        self.diagram = self.json_handler.load_json(self.diagram_path).get('apps').get(self.app_name).get('models')

    def get_diagram_admins(self, diagram):
        admins = list()
        for table_name in diagram.keys():
            table = diagram.get(table_name)
            admin_data = self.admin_generator.get_table_admin(table)

            admin = Admin()
            admin.model = table_name
            for key in admin_data.keys():
                value = admin_data.get(key)
                setattr(admin, key, value)

            admins.append(admin)

        return admins

    def check_field_value(self, list1, list2, field):
        for item in list1:
            for item2 in list2:
                if getattr(item, field) == getattr(item2, field):
                    return True

        return False

    def open_generated_file(self, file_path):
        with open(file_path, 'r') as f:
            data = f.read()
        return data

    def get_obj_properties(self, obj):
        return vars(obj)

    def test_extract_admin(self):
        admins = self.admin_generator.extract_admin(self.diagram)
        test_admins = self.get_diagram_admins(self.diagram)

        self.assertEqual(len(admins), len(test_admins))
        self.assertTrue(self.check_field_value(admins, test_admins, 'model'))
        self.assertTrue(self.check_field_value(admins, test_admins, 'list_display'))
        self.assertTrue(self.check_field_value(admins, test_admins, 'list_filter'))
        self.assertTrue(self.check_field_value(admins, test_admins, 'search_fields'))
        self.assertTrue(self.check_field_value(admins, test_admins, 'raw_id_fields'))
        self.assertTrue(self.check_field_value(admins, test_admins, 'filter_horizontal'))
        self.assertTrue(self.check_field_value(admins, test_admins, 'filter_vertical'))
        self.assertTrue(self.check_field_value(admins, test_admins, 'has_add_permission'))
        self.assertTrue(self.check_field_value(admins, test_admins, 'has_change_permission'))
        self.assertTrue(self.check_field_value(admins, test_admins, 'has_delete_permission'))

    def test_stream_to_jinja(self):
        admins = self.admin_generator.extract_admin(self.diagram)
        self.admin_generator.generate(self.diagram_path, self.app_name)
        admin_data = self.open_generated_file(f'{settings.BASE_DIR}/{self.app_name}/admin.py')
        for admin in admins:
            for prop in self.get_obj_properties(admin):
                if getattr(admin, prop):
                    self.assertTrue(getattr(admin, prop), admin_data)
