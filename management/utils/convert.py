def convert_none_to_empty_string(objects):
    for obj in objects:
        for field in obj._meta.fields:
            value = getattr(obj, field.name)
            if value is None:
                setattr(obj, field.name, '')
    return objects
