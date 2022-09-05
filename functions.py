import json


def load_candidates():
    """Загрузит данные из файла"""
    with open("candidates.json", mode='r', encoding='utf-8') as candidates:
        return json.load(candidates)


def get_all():
    """Покажет всех кандидатов"""
    return load_candidates()


def get_by_pk(pk):
    """Вернет кандидата по pk"""
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate


def get_by_skill(skill_name):
    """Вернет кандидатов по навыку"""
    result = []
    for candidate in load_candidates():
        if skill_name.upper().lower() in candidate['skills']:
            result.append(candidate)
    return result


