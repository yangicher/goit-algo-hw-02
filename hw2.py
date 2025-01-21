from collections import deque

def palindrome(input_string):
    normalized_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    char_deque = deque(normalized_string)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

def main():
    words = [
        "potop",
        "result",
        "palindrome",
        "12 33 21",
        "Lorem ipsum"
    ]

    for word in words:
        print(f"{word} -> pailndrom: {palindrome(word)}")

if __name__ == "__main__":
    main()