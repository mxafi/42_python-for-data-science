def NULL_not_found(object) -> int:
    try:
        type_object = type(object)
    except Exception:
        print("Type not found")
        return 1
    if type_object is type(None):
        print(f"Nothing: {object} {type_object}")
    elif type_object == float and object != object:
        print(f"Cheese: {object} {type_object}")
    elif type_object == int and object == 0:
        print(f"Zero: {object} {type_object}")
    elif type_object == str and object == "":
        print(f"Empty: {type_object}")
    elif type_object == bool and object is False:
        print(f"Fake: {object} {type_object}")
    else:
        print("Type not Found")
        return 1
    return 0
