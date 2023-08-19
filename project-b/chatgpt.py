import tkinter as tk
import openai

# Apply the API Key
openai.api_key = "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" #"YOUR_API_KEY"

# Generate a response using OpenAI GPT-3
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# GUI interface
def display_response():
    input_text = input_field.get()
    response = generate_response(input_text)
    output_field.config(state='normal')
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.END, response)
    output_field.config(state='disabled')

# Create the main window
root = tk.Tk()
root.title("OpenAI Chatbot")
root.geometry("600x700")

# Create the input field
input_field = tk.Entry(root, font=("Arial", 14))
input_field.pack(pady=10)

# Create the submit button
submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=display_response)
submit_button.pack(pady=10)

# Create the output field
output_field = tk.Text(root, font=("Arial", 14), state='disabled')
output_field.pack(pady=10)

# Start the GUI event loop
root.mainloop()

'''
Thank you for providing the complete code. This code creates a simple graphical user interface (GUI) using the Tkinter library to interact with OpenAI's GPT-3 model and display responses.

Here's a breakdown of how the code works:

1. **Import Statements**: The code starts by importing the necessary modules: `tkinter` for creating the GUI interface and `openai` for using the OpenAI API to generate responses.

2. **Setting API Key**: You set your OpenAI API key using the `openai.api_key` attribute. Remember to replace `"YOUR_API_KEY"` with your actual OpenAI API key.

3. **Generating Response**: The `generate_response` function takes a prompt as input and uses the OpenAI API to generate a response. It configures the parameters of the API request and returns the generated message.

4. **Displaying Response**: The `display_response` function reads the user's input from the input field, generates a response using the `generate_response` function, and then displays the response in the output field.

5. **Creating GUI Elements**: The main GUI window is created using `tk.Tk()`. Various GUI elements such as input field, submit button, and output field are created using `tk.Entry()`, `tk.Button()`, and `tk.Text()`, respectively. These elements are configured with appropriate fonts and options.

6. **Button Command**: The "Submit" button is associated with the `display_response` function using the `command` parameter. This means that when the button is clicked, the `display_response` function will be called.

7. **GUI Event Loop**: The GUI event loop is started using `root.mainloop()`, which keeps the GUI interface running and responsive to user interactions.

Overall, this code creates a basic interface where users can enter text prompts, click the "Submit" button, and receive generated responses from the GPT-3 model.

Remember to have the `openai` library installed using `pip install openai` and ensure you have the necessary OpenAI API key to use this code effectively.

'''