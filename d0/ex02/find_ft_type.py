def all_thing_is_obj(object) -> int:
    type_object = type(object)
    if type_object == str:
        print(f"{object} is in the kitchen : {type_object}")
    elif type_object == int:
        print("Type not found")
    else:
        print(f"{type_object.__name__.capitalize()} : {type_object}")
    return 42
