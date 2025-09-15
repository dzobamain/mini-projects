from replacer import replacer_in_text, replacer_in_file, replacer_in_directory
      
def check_user_choice(user_choice):
    array = enter(user_choice)
    if array is None:
        return

    match user_choice:
        case '1':
            replacer_in_text(array[0], array[1], array[2])
        case '2':
            replacer_in_file(array[0], array[1], array[2])
        case '3':
            replacer_in_directory(array[0], array[1], array[2])
        case _:
            print("Unknown choice.")

                
def enter(number):
    if number == 'q':
        return None
    
    if number == '1':
        text_or_path = input("Enter your text: ")
    elif number == '2' or number == '3':
        text_or_path = input("Enter the file path: ")
    else:
        print("Invalid choice.")
        return None

    
    old_word = input("Enter the word to replace: ")
    new_word = input("Enter the new word: ")
    
    if  old_word == new_word:
        return None
    
    return text_or_path, old_word, new_word
    
def main():
    user_choice = ''
    while user_choice.lower() != 'q':
        print("1. Text")
        print("2. File")
        print("3. Directory")
        print("q. exit")
        
        user_choice = input("Choose!: ")
        check_user_choice(user_choice)

if __name__ == "__main__":
    main()
