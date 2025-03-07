import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the input file
input_file = os.path.join(current_dir, 'Words.txt')

# Open the Words.txt file in read mode
try:
    with open(input_file, 'r', encoding='utf-8') as file:
        txt = file.read()

    # Split the text into a list of words and remove leading/trailing whitespace
    words = [word.strip().split('. ')[-1] for word in txt.split("\n") if word.strip()]

    # Print the words list for debugging
    print(f"Words found: {words}")
    print(f"Number of words: {len(words)}")

    if not words:
        print("Warning: No words were extracted from the input file.")
    else:
        # Construct the full path to the output file
        output_file = os.path.join(current_dir, 'ArrayWords.txt')

        # Open the ArrayWords.txt file in write mode
        with open(output_file, 'w', encoding='utf-8') as file:
            # Format the words with backticks and join them
            formatted_words = [f'"{word}"' for word in words]
            output_string = '[' + ', '.join(formatted_words) + ']'
            file.write(output_string)

        # Verify the output file
        with open(output_file, 'r', encoding='utf-8') as file:
            content = file.read()
            if content:
                print(f"Words have been successfully written to {output_file}")
                print(f"First part of the output file: {content[:100]}...")
            else:
                print(f"Error: The output file {output_file} is empty.")

except FileNotFoundError:
    print(f"Error: The file {input_file} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
