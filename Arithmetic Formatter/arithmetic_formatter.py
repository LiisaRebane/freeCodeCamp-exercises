def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_operands = []
    operators = []
    second_operands = []
    solutions = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid problem format.'

        first_operand, operator, second_operand = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (first_operand.isdigit() and second_operand.isdigit()):
            return 'Error: Numbers must only contain digits.'

        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        first_operands.append(first_operand)
        operators.append(operator)
        second_operands.append(second_operand)

        if display_answers:
            if operator == '+':
                solution = str(int(first_operand) + int(second_operand))
            elif operator == '-':
                solution = str(int(first_operand) - int(second_operand))
            solutions.append(solution)

    first_line = []
    second_line = []
    dashes = []
    answers = []

    for i in range(len(problems)):
        length = max(len(first_operands[i]), len(second_operands[i])) + 2
        first_line.append(first_operands[i].rjust(length))
        second_line.append(operators[i] + ' ' + second_operands[i].rjust(length - 2))
        dashes.append('-' * length)
        if display_answers:
            answers.append(solutions[i].rjust(length))

    arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dashes)
    if display_answers:
        arranged_problems += '\n' + '    '.join(answers)

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)}')
