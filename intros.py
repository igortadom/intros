import sys
from pprint import pprint


def introspection_info(obj):

    attributes = []
    methods = []
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)
        else:
            attributes.append(attr)
    return {
        'attributes': attributes,
        'methods': methods,
        'module': __name__,
        'id': id(obj),
        'type': type(obj).__name__,
        'size': sys.getsizeof(obj)
    }


number_info = introspection_info(42)
pprint(number_info)
print(sys.getrefcount(__name__))
print(sys.getfilesystemencoding())
print(sys.winver)
