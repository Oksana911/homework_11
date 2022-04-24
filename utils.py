import json

def load_candidates_from_json(path):
    """возвращает список всех кандидатов"""
    with open(path, "r") as file:
        data = json.load(file)
    return data


def get_candidate(candidate_id):
    """возвращает всю информацию (словарь) про одного кандидата по его id"""
    data = load_candidates_from_json("candidates.json")
    for candidate in data:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """возвращает кандидатов по имени"""
    data = load_candidates_from_json("candidates.json")
    candidates_by_name = []
    for candidate in data:
        if candidate_name.lower() in candidate["name"].lower().split(" "):
            candidates_by_name.append(candidate)
    return candidates_by_name


def get_candidates_by_skill(skill_name):
    """возвращает кандидатов по навыку"""
    data = load_candidates_from_json("candidates.json")
    candidates_by_skill = []
    for candidate in data:
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            candidates_by_skill.append(candidate)

    return candidates_by_skill
