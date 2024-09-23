from typing import List, Dict, Callable


def aggregate_data(data: List[Dict], key: str, aggregator: Callable):
    final_dict = dict()
    for item in data:
        aggregator(item, final_dict, key)
    return final_dict


def sum_aggregator(item, final_dict, key):
    if item[key] in final_dict.keys():
        final_dict[item[key]] += item["value"]
    else:
        final_dict[item[key]] = item["value"]


data = [{'category': 'R', 'value': 10}, {'category': 'C', 'value': 20}, {'category': 'R', 'value': 5}]

result = aggregate_data(data, 'category', sum_aggregator)
print(result)
