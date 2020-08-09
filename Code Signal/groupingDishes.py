def groupingDishes(dishes):
    d = {}
    for dish in dishes:
        item = dish[0]
        for ingredient in dish[1:]:
            if ingredient not in d:
                d[ingredient] = []
            d[ingredient].append(item)
    output = []
    for key,value in sorted(d.items()):
        if len(value) >= 2:
            output.append([key] + sorted(value))
    return output
