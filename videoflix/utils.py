def convert_string_to_boolean(value, default=False):
    ##### Convert a string to a real boolean 
    if default is None:
        return default
    return str(value).strip().lower() in ("true", "1", "yes", "on")