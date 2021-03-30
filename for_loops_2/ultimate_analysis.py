def ultimate_analysis(list):
    result = {
        'sum_total': None,
        'maximum': None,
        'minimum': None,
        'average': None,
        'length': 0
    }
    if len(list) == 0:
        return result
    else:
        result['sum_total'] = 0
        result['maximum'] = list[0]
        result['minimum'] = list[0]
    
    for i in list:
        if i > result['maximum']:
            result['maximum'] = i
        elif i < result['minimum']:
            result['minimum'] = i

        result['sum_total'] += i
        result['length'] += 1
    result['average'] = result['sum_total'] / len(list)

    return result

print(ultimate_analysis([37, 2, 1, -9]))
print(ultimate_analysis([]))