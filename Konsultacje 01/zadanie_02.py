d1 = {"a": "1", "b": "2", "c": "2"}
d2 = {"b": "4", "c": "3", "d": "5"}


def slowniki(d1, d2):
    d3 = d1
    for key in d2:
        if key in d3:
            d3[key] = [d2[key], d3[key]]
        else:
            d3[key] = d2[key]
    return d3


print(slowniki(d1, d2))
