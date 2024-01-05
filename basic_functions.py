import inflect


def int_to_ordinal_str(input_int):
    engine = inflect.engine()
    ordinal_string = engine.ordinal(input_int)
    return ordinal_string
