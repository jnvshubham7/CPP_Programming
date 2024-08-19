import os
from groq import Groq

# Initialize the Groq client with the API key directly
client = Groq(
    api_key="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",
)

# Define the directory containing the Markdown files
input_directory = "D:\GitHub\All Notes\Android_chatgpt"
output_directory = "D:\\GitHub\\All Notes\\ChatGPT Notes1"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Define the prompt for processing files
# Define the prompt for processing files
prompt = "rewrite in article  in point wise  with code and example without giving  any details you should direct start writing article from first line with heading and subheading explain in details"


# Process each Markdown file in the directory
for filename in os.listdir(input_directory):
    if filename.endswith(".md"):
        # Read the content of the Markdown file
        with open(os.path.join(input_directory, filename), 'r') as file:
            content = file.read()

        # Combine the content with the prompt
        messages = [
            {
                "role": "user",
                "content": f"{prompt}\n\n{content}",
            }
        ]

        # Perform the chat completion
        try:
            chat_completion = client.chat.completions.create(
                messages=messages,
                model="llama3-8b-8192",
            )

            # Get the response
            response_content = chat_completion.choices[0].message.content

            # Prepend the file name under the article heading
            article_with_filename = f"{response_content}"

            # Define the output file path
            output_file_path = os.path.join(output_directory, f"{filename}")

            # Write the response to the new file
            with open(output_file_path, 'w') as output_file:
                output_file.write(article_with_filename)

            print(f"Processed and saved: {output_file_path}")

        except Exception as e:
            print(f"An error occurred while processing {filename}: {e}")
