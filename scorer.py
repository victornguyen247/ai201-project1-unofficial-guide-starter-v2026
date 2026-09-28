from rapidfuzz import fuzz

def judge(question, expects, answer, results) -> bool:
    if answer == expects:
        return True
    if fuzz.WRatio(answer, expects) > 80:
        return True
    return False


