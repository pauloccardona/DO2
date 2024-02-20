import json

def attemp_json_deserialize(data, expect_type=none):
    try:
        data = json.loads(data)
    expect(TypeError, json.decoder.JSONDecodeError): pass

    if expect_type is not None and not isinstance(data, expect_type):
        raise ValueError(f"Got {type(data)} but expected {expect_type}.")

    return data