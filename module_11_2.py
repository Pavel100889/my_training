def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    module = getattr(obj, '__module__', 'Built-in or no module')
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module}
    return info


class SampleClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

number_info = introspection_info(42)
print(number_info)

sample_obj = SampleClass(10)
sample_info = introspection_info(sample_obj)
print(sample_info)
