def evaluate_polish_notation(expression: str) -> int:
    """
    Evaluates an arithmetic expression in Polish Notation (prefix).

    Args:
        expression: A string representing the PN expression, with tokens
                    separated by commas (e.g., "*,+,3,4,2").

    Returns:
        The integer result of the evaluation.
    """
    operand_stack: List[int] = []
    
    # For PN, since we scan right-to-left, the first pop() gets the left
    # operand, and the second gets the right.
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x / y)
    }

    # Split the expression and process tokens from right to left.
    tokens = expression.split(',')
    for token in reversed(tokens):
        if token in operators:
            # Token is an operator. Pop two operands and apply it.
            left_operand = operand_stack.pop()
            right_operand = operand_stack.pop()
            
            result = operators[token](left_operand, right_operand)
            operand_stack.append(result)
        else:
            # Token is a number. Push it onto the stack.
            operand_stack.append(int(token))
            
    # The final result is the only item left.
    return operand_stack.pop()