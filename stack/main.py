from stack import Stack


def is_balanced_brackets(braskets):
    stack = Stack()
    for bracket in braskets:
        if bracket == "(" or bracket == "{" or bracket == "[":
            stack.push(bracket)
        else:
            if bracket == ")" and stack.size() > 0 and stack.peek() == "(":
                stack.pop()
            elif bracket == "}" and stack.size() > 0 and stack.peek() == "{":
                stack.pop()
            elif bracket == "]" and stack.size() > 0 and stack.peek() == "[":
                stack.pop()
            else:
                return "Несбалансированно"
    if stack.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"


if __name__ == "__main__":
    print(is_balanced_brackets("{{[()]}}"))
