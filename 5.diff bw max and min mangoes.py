
def distribute_mangoes(mangoes, students):
    mangoes.sort()
    min_diff = float('inf')
    for i in range(len(mangoes) - students + 1):
        diff = mangoes[i + students - 1] - mangoes[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff

# Example usage:
mangoes = [3, 7, 2, 9, 4]
students = 3
min_diff = distribute_mangoes(mangoes, students)
print("Minimum difference between bags distributed to students:", min_diff)