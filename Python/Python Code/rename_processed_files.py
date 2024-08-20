import os
import re
from groq import Groq

# Initialize the Groq client with the API key directly
client = Groq(
    api_key="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",
)

# Define the directories
output_directory = r"D:\GitHub\All_Programming\Python\test"
renamed_directory = r"D:\GitHub\All_Programming\Python\1"

# Ensure the renamed directory exists
os.makedirs(renamed_directory, exist_ok=True)

# Function to clean and extract the suggested file name
def extract_filename(suggestion):
    # Extract the filename from the code or command formatted suggestion
    match = re.search(r'`(.+?)`', suggestion)
    if match:
        cleaned_filename = match.group(1).strip()
        # Remove any invalid characters and return as .md file
        return re.sub(r'[\\/*?:"<>|]', "", cleaned_filename).replace(" ", "_") + ".md"
    return None  # Return None if no valid filename is found

# Step 2: Read the newly created files and get suggestions for new filenames
for processed_filename in os.listdir(output_directory):
    if processed_filename.endswith(".md"):
        processed_filepath = os.path.join(output_directory, processed_filename)
        
        # Read the content of the processed file
        with open(processed_filepath, 'r') as file:
            processed_content = file.read()

        # Prepare the request to Groq for filename suggestions in code format
        name_suggestion_message = [
            {
                "role": "user",
                "content": f"Based on the content below, suggest a concise and valid filename in the format of a code or command:\n\nContent:\n\n{processed_content}",
            }
        ]

        try:
            # Request a filename suggestion from Groq
            name_suggestion_completion = client.chat.completions.create(
                messages=name_suggestion_message,
                model="llama3-8b-8192",
            )

            # Extract and clean the suggested filename
            suggested_name_raw = name_suggestion_completion.choices[0].message.content
            suggested_name = extract_filename(suggested_name_raw)

            if suggested_name:
                # Define the new file path with the suggested name
                renamed_file_path = os.path.join(renamed_directory, suggested_name)

                # Rename the file with the suggested name
                os.rename(processed_filepath, renamed_file_path)
                print(f"File {processed_filename} renamed to {suggested_name}")
            else:
                print(f"No valid filename could be extracted for {processed_filename}")

        except Exception as e:
            print(f"An error occurred while renaming {processed_filename}: {e}")

print("All files processed and renamed.")