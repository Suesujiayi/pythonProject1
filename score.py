def main():
    import random
    score = random.randint(0, 100)
    print(score_kinds(score))
    filename = ' score_kinds.txt  '
    with open(filename, 'w') as file_object:
        file_object.write(" {} is {} ".format(score, score_kinds(score)+"\n"))
        file_object.close()


def score_kinds(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score <= 50:
        return "Bad"
    elif score <= 90:
        return "Passable"
    else:
        return "Excellent"
