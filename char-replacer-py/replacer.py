import os

def replacer_in_text(text, old_word, new_word):
    replaced_text = text.replace(old_word, new_word)
    print("Updated Text: ", replaced_text)

def replacer_in_file(file_path, old_word, new_word):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        replaced_content = content.replace(old_word, new_word)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(replaced_content)

        file_base_name, file_extension = os.path.splitext(file_path)
        file_name = os.path.basename(file_base_name)

        print(f"\tFile: {file_name}{file_extension}")
        print(f"\t\tReplaced '{old_word}' with '{new_word}'")

    except UnicodeDecodeError:
        print(f"ERROR: Could not decode {file_path}. It may not be in UTF-8 format.")
    except Exception as e:
        print(f"ERROR: An error occurred while processing {file_path}: {e}")

def replacer_in_directory(directory_path, old_word, new_word):
    try:
        for item_name in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item_name)

            if os.path.isdir(item_path):
                print(f"Processing internal directory: {item_path}")
                replacer_in_directory(item_path, old_word, new_word)
            elif os.path.isfile(item_path):
                replacer_in_file(item_path, old_word, new_word)

    except FileNotFoundError:
        print(f"ERROR: The directory {directory_path} was not found.")
    except Exception as e:
        print(f"ERROR: An error occurred: {e}")