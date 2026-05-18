# CodeAlpha_TextSummarizer
The whole code is an Artificial Intelligence Text Summarizer application built using Python with a GUI interface. The main idea of the project is that the user writes a long paragraph or article inside the program, then clicks the “Summarize” button, and the AI model reads the text, analyzes the important information, and generates a short summary automatically.
At the beginning of the code, we imported the required libraries. We imported the transformers library because it contains ready-made AI models. We also imported pipeline, which allows us to use the summarization model easily. Then we imported tkinter to create the graphical user interface (GUI), and scrolledtext to create text areas with scrolling support so users can write long texts comfortably.
After importing the libraries, we loaded the AI summarization model using:
Python
summarizer = pipeline("summarization")
This line loads a pre-trained AI model specialized in text summarization. The model reads the text, understands the important points, and produces a shorter version containing the key ideas.
Next, we created a function called summarize_text(). This function runs when the user clicks the “Summarize” button. Inside the function, the program first reads the text entered by the user using:
Python
text = input_text.get("1.0", tk.END)
Then the program checks if the user actually entered text. If the text area is empty, the function stops to avoid errors.
After that, the AI model starts generating the summary using:
Python
result = summarizer(text, max_length=50, min_length=20, do_sample=False)
Here, the AI analyzes the text and creates the summary. The max_length parameter sets the maximum summary length, while min_length sets the minimum summary length. The do_sample=False option makes the output more stable and organized.
When the summary is generated, the program removes any previous summary using delete() and displays the new summary inside the output text box using insert().
After building the summarization logic, the code creates the graphical interface. First, it creates the main application window using:
Python
root = tk.Tk()