def data_type(value):
    if isinstance(value, list):
        return 'list'
    elif isinstance(value, dict):
        return 'dictionary'
    elif isinstance(value, str):
        return 'string'
    elif isinstance(value, int):
        return 'integer'
    elif isinstance(value, float):
        return 'float'
    elif isinstance(value, bool):
        return 'boolean'
    else:
        return 'date'

#Used the isinstance() method