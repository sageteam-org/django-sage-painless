class Attribute:
    """
    Required Field object that contains `key` and `value`
    """
    def __init__(self):
        self.key = None
        self.value = None

    def set_attr(self, attr_key, attr_value):
        """
        set `key` and `value`
        """
        self.key = attr_key
        self.value = attr_value


class Field:
    """
    Field object that contains attributes of a django model field
    """
    def __init__(self):

        self.name = None
        self.type = None
        self.attrs = list()

    field_types = {
        'character': {
            'type': 'CharField',
            'required': []
        },
        'integer': {
            'type': 'IntegerField',
            'required': []
        },
        'datetime': {
            'type': 'DateTimeField',
            'required': []
        },
        'text': {
            'type': 'TextField',
            'required': []
        },
        'fk': {
            'type': 'ForeignKey',
            'required': []
        },
        'one2one': {
            'type': 'OneToOneField',
            'required': []
        },
        'image': {
            'type': 'ImageField',
            'required': []
        },
        'bool': {
            'type': 'BooleanField',
            'required': []
        }
    }

    def set_type(self, field_type):
        """
        Set field type based on `field_types` and required_attrs
        """
        field = self.field_types.get(field_type)
        if field:
            self.type = field.get('type')
            message = True, 'Applied Successfully'
        else:
            message = False, 'Field Not Defined'

        return message

    def add_attribute(self, key, value):
        """
        Add attribute to Field
        """
        attr = Attribute()
        attr.set_attr(key, value)
        self.attrs.append(attr)
        return True
