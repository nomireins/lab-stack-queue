from stack import Stack


def check_delimiters(expr: str, delims: dict[str,str]) -> bool:
    stack = Stack()
    closing_delims = set(delims.values())

    for char in expr:
        if char in delims and delims[char] == char:
            if stack.peek() == char:
                stack.pop()
            else:
                stack.push(char)
        elif stack and stack.peek() == char:
            stack.pop()
        elif char in delims:
            stack.push(delims[char])
        elif char in closing_delims:
            return False

    return stack.empty()


def infix_to_postfix(expr: str) -> str:
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    operators = Stack()
    output = []

    for token in expr.split():
        if token not in precedence and token not in ('(', ')'):
            output.append(token)
        elif token == '(':
            operators.push(token)
        elif token == ')':
            while operators.peek() != '(':
                output.append(operators.pop())
            operators.pop()
        else:
            while (operators and operators.peek() != '('
                   and precedence[operators.peek()] >= precedence[token]):
                output.append(operators.pop())
            operators.push(token)

    while operators:
        output.append(operators.pop())

    return ' '.join(output)
