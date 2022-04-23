import json

def load_candidates_from_json(path):
    """возвращает список всех кандидатов"""
    with open(path, "r") as file:
        data = json.load(file)
    return data

def format_candidate(candidates_list):
    """
    Форматируем данные кандидатов из списка в формат:
    Имя кандидата -
    Позиция кандидата -
    Возраст -
    Навыки через запятую
    """
    candidates = "<pre>"
    for candidate in candidates_list:
        name = candidate["name"]
        position = candidate["position"]
        skills = candidate["skills"]
        age = candidate["age"]
        candidates += (
            f"Имя кандидата - {name}\n"
            f"Позиция кандидата - {position}\n"
            f"Возраст - {age}\n"
            f"Навыки - {skills}\n\n"
        )

    return candidates + "<pre>"


def get_candidate(candidate_id):
    """возвращает одного кандидата по его id"""
    data = load_candidates_from_json("candidates.json")
    for candidate in data:
        if candidate["id"] == candidate_id:
            return format_candidate(candidate)


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    data = load_candidates_from_json("candidates.json")
    candidates_by_name = []
    for candidate in data:
        if candidate_name in candidate["name"]:
            candidates_by_name.append(candidate)
    return format_candidate(candidates_by_name)


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    data = load_candidates_from_json("candidates.json")
    candidates_by_skill = []
    for candidate in data:
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            candidates_by_skill.append(candidate)

    return format_candidate(candidates_by_skill)
