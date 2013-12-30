lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

def average(lst):
    return float(sum(lst))/len(lst)
    
def get_average(kid):
    hw = average(kid['homework'])
    qu = average(kid['quizzes'])
    te = average(kid['tests'])
    avg = (hw*0.1) + (qu*0.3) + (te*0.6)
    
    return avg

def get_letter_grade(score):
    if score >= 90: return 'A'
    elif 80 <= score < 90: return 'B'
    elif 70 <= score < 80: return 'C'
    elif 60 <= score < 70: return 'D'
    elif score < 60: return 'F'
    
print get_letter_grade(get_average(lloyd))
