import vectormath as vmath


class Texel:

    position = vmath.Vector3(0, 0, 0)
    UID = None
    material_id = None

    texel_dict = {
        "UID": UID,
        "typeID": material_id,
        "position": position,
    }
