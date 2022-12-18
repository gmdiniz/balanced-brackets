'''
Given an expression string exp, write a program to examine whether the pairs and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in the given expression.

Example:
Input: exp = “[()]{}{[()()]()}”
Output: Balanced
Explanation: all the brackets are well-formed

Input: exp = “[(])”
Output: Not Balanced
Explanation: 1 and 4 brackets are not well formed
'''

def check_stack(input_stack):
    def type_of_bracket(bracket):
        if bracket in ('(', '[', '{'):
            return 'open'
        elif bracket in (')', '}', ']'):
            return 'close'
        else:
            return 'not a bracket'

    def check_if_brackets_is_same_kind(bracket1, bracket2):
        types = (['[',']'], ['{','}'], ['(',')'])
        for type in types:
            if bracket1 in type and bracket2 in type:
                return True
            elif bracket1 not in type and bracket2 not in type:
                pass
            else: 
                return False

    def get_output(balanced, explanation):
        if balanced:
            output = 'Balanced'
            explanation = 'all the brackets are well-formed'
            return [output, explanation]
        else:
            output = 'Not Balanced'
            explanation = ''
            return [output, explanation]

    balanced_brackets = False
    explanation = ''
    comparative_stack = []
    array_of_unbalanced_index = []

    for index, bracket in enumerate(input_stack):
        if type_of_bracket(bracket) == 'open':
            comparative_stack.append(bracket)
        elif type_of_bracket(bracket) == 'close':
            same_kind = check_if_brackets_is_same_kind(
                bracket, comparative_stack[-1])
            if same_kind:
                comparative_stack.pop()
            else: 
                array_of_unbalanced_index.append(index)
                comparative_stack.append(bracket)   

    balanced_brackets = False if len(array_of_unbalanced_index) > 0 else True

    return get_output(balanced_brackets, explanation)


assert (check_stack('[()]{}{[()()]()}')) == ['Balanced', 'all the brackets are well-formed']
assert (check_stack('[(])')) == ['Not Balanced', '']

