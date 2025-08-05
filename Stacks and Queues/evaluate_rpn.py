from typing import List

def evaluate_rpn(expression: str) -> int:
    """
    Evaluates an arithmetic expression in Reverse Polish Notation (RPN).

    Args:
        expression: A string representing the RPN expression, with tokens
                    separated by commas (e.g., "3,4,+,2,*").

    Returns:
        The integer result of the evaluation.
    """
    operand_stack: List[int] = []
    
    # Note on operator order for RPN: The first pop() gets the right operand,
    # the second gets the left. The lambda arguments are therefore defined
    # as (right_operand, left_operand) to match this popping order.
    operators = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: int(x / y) # Use int() for integer division
    }

    for token in expression.split(','):
        if token in operators:
            # Token is an operator. Pop two operands, apply the operator,
            # and push the result back onto the stack.
            right_operand = operand_stack.pop()
            left_operand = operand_stack.pop()
            
            result = operators[token](right_operand, left_operand)
            operand_stack.append(result)
        else:
            # Token is a number. Convert it to an integer and push it.
            operand_stack.append(int(token))

    # The final result is the only item left on the stack.
    return operand_stack.pop()