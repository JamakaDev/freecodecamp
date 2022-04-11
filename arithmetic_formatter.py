def arithmetic_arranger(problems, solve=False):
    lines = [[], [], []]
    if solve:
        lines = [[], [], [], []]

    for i, problem in enumerate(problems):
        problem = problem.split()
        if len(problems) > 5:
            return 'Error: Too many problems.'
        if problem[1] != '+' and problem[1] != '-':
            return 'Error: Operator must be \'+\' or \'-\'.'
        if not (problem[0].isdigit() and problem[2].isdigit()):
            return 'Error: Numbers must only contain digits.'
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        places = max([len(problem[0]), len(problem[2])]) + 2
        for index, j in enumerate(problem):
            count = 0
            row = ''
            if index < 1:
                for place in range(places):
                    if place < places-len(j):
                        row += ' '
                    elif places-len(j) <= place <= places - 1:
                        row += j[count]
                        count += 1
                lines[index].append(row)
            elif index > 1:
                for place in range(places):
                    if place < 1:
                        row += problem[1]
                    elif place < places-len(j):
                        row += ' '
                    elif places-len(j) <= place <= places - 1:
                        row += j[count]
                        count += 1
                lines[index-1].append(row)
        lines[2].append('-'*places)
        if solve:
            result = str(eval(problems[i]))
            result_count = 0
            row = ''
            for place in range(places):
                if place < places-len(result):
                    row += ' '
                elif places-len(result) <= place <= places - 1:
                    row += result[result_count]
                    result_count += 1
            lines[3].append(row)
    new_line = ''
    for line in lines:
        if line != lines[-1]:
            new_line += ('    '.join(line) + '\n')
        else:
            new_line += ('    '.join(line))
    return new_line


print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
print('*'*50)
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print('*'*50)
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
