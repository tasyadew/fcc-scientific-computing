def arithmetic_arranger(problems, show_answers=False):

    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Check if there are any invalid operators
    for problem in problems:
        if "+" not in problem and "-" not in problem:
            return "Error: Operator must be '+' or '-'."

    # Check if there are any invalid numbers
    for problem in problems:
        if not problem.split()[0].isdigit() or not problem.split()[2].isdigit():
            return "Error: Numbers must only contain digits."
    
    # Check if there are any numbers with more than 4 digits
    for problem in problems:
        if len(problem.split()[0]) > 4 or len(problem.split()[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

    # No errors, so we can proceed with the arrangement
    # Initialize the lines
    top_lines = []
    bottom_lines = []
    dash_lines = []
    answer_lines = []

    # loop for each problem
    for problem in problems:
        # split the problem into its components
        num1 = problem.split()[0]
        operator = problem.split()[1]
        num2 = problem.split()[2]

        # find the longest number
        longest = max(len(num1), len(num2))

        # calculate answer
        if operator == "+":
            answer = str(int(num1) + int(num2))
        else:
            answer = str(int(num1) - int(num2))

        # create the lines
        top_line = num1.rjust(longest + 2)
        bottom_line = operator + num2.rjust(longest + 1)
        dashes = "-" * (longest + 2)
        answer = str (answer.rjust(longest + 2))

        # append lines to the respective lists
        top_lines.append(top_line)
        bottom_lines.append(bottom_line)
        dash_lines.append(dashes)
        if show_answers:
            answer_lines.append(answer)

    # join the lines with spaces
    arranged_problems = "    ".join(top_lines) + "\n" + "    ".join(bottom_lines) + "\n" + "    ".join(dash_lines)
    if show_answers:
        arranged_problems += "\n" + "    ".join(answer_lines)

    return arranged_problems