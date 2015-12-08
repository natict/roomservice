
def obj_to_dict(obj, d=None):
    data = d or {}
    for k, v in vars(obj).items():
        data.update({k: v})
    return data


def to_dict(obj):
    if isinstance(obj, list):
        # assumes a list of objects
        return [obj_to_dict(item) for item in obj]
    elif isinstance(obj, dict):
        # assumes dict containing values that are objects.
        return {k: obj_to_dict(v) for k, v in obj.items()}
    elif isinstance(obj, object):
        return obj_to_dict(obj)
