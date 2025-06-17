def convert_string_to_boolean(value, default=False):
    ##### Convert a string to a real boolean 
    return str(value).strip().lower() in ("true", "1", "yes", "on")