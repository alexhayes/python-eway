class ValidationError(Exception):
    def __init__(self, message):
        self.message = message

        
class Field(object):
    def __init__(self, external_name=None, default=None, required=True):
        self.external_name = external_name
        self.required = required
        self._default = default
    
    def clean(self, value):
        return value
    
    def get_default(self):
        return self._default
    
    def _get_value(self):
        return self._value or self._default
    
    def is_valid(self):
        if self.required and self.value is None:
            raise ValidationError("Field Required")
        return True
    
    def _set_value(self, value):
        self._value = self.clean(value)
    
    value = property(_get_value, _set_value)


class CentsField(Field):
    def clean(self, value):
        return int(value * 100)

class FieldsMetaclass(type):
    def __new__(cls, name, bases, attrs):
        fields = {}
        for field_name, obj in attrs.items():
            if isinstance(obj, Field):
                field = attrs.pop(field_name)
                field.attname = field_name
                fields[field_name] = field
        attrs['fields'] = fields
        new_class = super(FieldsMetaclass, cls).__new__(cls, name, bases, attrs)
        return new_class

class ValidatorBase(object):
    def __init__(self, **kwargs):
        self._errors = {}
        for name, field in self.fields.items():
            val = kwargs.pop(field.attname, field.get_default())
            setattr(self, field.attname, val)
    
    def is_valid(self):
        valid = True
        for name, field in self.fields.items():
            value = getattr(self, name)
            field.value = value
            try:
                field.is_valid()
            except ValidationError, e:
                self._errors[name] = e.message
                valid = False
        return valid
    
    def _convert(self, fields):
        result = {}
        for name, field in fields.items():
            if field.external_name:
                result[field.external_name] = field.value
            else:
                result[name] = field.value
        return result
    
    def get_data(self):
        """
        Return a dictionary with the fields "external" name and the value
        """
        if self.is_valid():
            return self._convert(self.fields)
        return None

class Validator(ValidatorBase):
    __metaclass__ = FieldsMetaclass