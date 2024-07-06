input_string = "(()(())())"

def mark_parentheses_serial (input_string):
    stack = []
    serials = []
    serial_number = 1

    for i, char in enumerate(input_string):
        if char == "(":
            stack.append(serial_number)
            serials.append(serial_number)
            serial_number += 1
        elif char == ")":
            if stack:
                opening_index = stack.pop()
                serials.append(opening_index)
    
    return serials

def main ():
    serials = mark_parentheses_serial (input_string)

    print(" ".join(map(str, serials)))

if __name__ == "__main__":
    main ()