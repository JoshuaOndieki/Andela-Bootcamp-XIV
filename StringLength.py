def string_length(data):
    if isinstance(data, str):
        return [len(data)]
    elif isinstance(data, list):
        length_list = []
        for item in data:
            length_list.append(len(item))
        return length_list
    else:
        return "Input Not a string or list"

