from typing import Dict, Any


# Пишем функцию сортировки операций по статусу
def filter_by_state(inform_dict: list[Dict[str, Any]], state_id: str = "EXECUTED") -> list[Dict[str, Any]]:
    """Возвращает новый список словарей, у которых ключ соответствует
    указаному значению по умолчанию "EXECUTED'"""

    new_list_state = []

    for every_dict in inform_dict:
        if every_dict["state"] == state_id:
            new_list_state.append(every_dict)
    return new_list_state


# Пишем функцию для сортировки по дате
def sort_by_date(inform_dict: list[Dict[str, Any]], reverse: bool = True) -> list[Dict[str, Any]]:
    """Cортировка операций клиентов по дате"""
    return sorted(inform_dict, key=lambda x: (x["date"], x["id"]), reverse=reverse)


# print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       # {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       # {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       # {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
#print(sort_by_date([{'id': 41428827, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    #{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    #{'id': 41428828, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    #{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    #{'id': 41428826, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    #{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
