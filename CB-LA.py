import tkinter as tk
import webbrowser
import pygame.mixer as mixer       
import os
mixer.init()
# Function to get chatbot responses
youtube_url = "https://www.youtube.com"
youtube_url1 = "https://www.youtube.com/watch?v=vgJeQvGYYpk"
youtube_url2="https://www.google.com/search?q=pac+Man&sca_esv=576780426&ei=J346Zc3mGPGhseMPqKunkAM&ved=0ahUKEwiNltO7_JOCAxXxUGwGHajVCTIQ4dUDCBA&uact=5&oq=pac+Man&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgCIgdwYWMgTWFuMg0QLhiKBRixAxiDARhDMg4QLhiDARixAxiKBRiRAjIOEAAYigUYsQMYgwEYkQIyCBAuGIoFGJECMggQABiKBRiRAjIHEC4YigUYQzIHEC4YigUYQzIHEAAYigUYQzIHEC4YigUYQzIHEAAYigUYQzIcEC4YigUYsQMYgwEYQxiXBRjcBBjeBBjgBNgBAkjmRFCjGFitQXAGeAGQAQCYAZoBoAGoC6oBBDAuMTG4AQPIAQD4AQGoAgrCAgoQABhHGNYEGLADwgIWEAAYAxiPARjlAhjqAhi0AhiMA9gBAcICFhAuGAMYjwEY5QIY6gIYtAIYjAPYAQHCAhQQLhiKBRiRAhiLAxioAxiYAxjwA8ICCBAuGIAEGLEDwgILEAAYgAQYsQMYgwHCAhEQLhiABBixAxiDARjHARjRA8ICDhAuGIAEGLEDGMcBGNEDwgIFEAAYgATCAhQQLhiDARjHARixAxjRAxiKBRiRAsICCxAAGIoFGLEDGJECwgIKEC4YigUYsQMYQ8ICCBAAGIAEGLEDwgIjEC4YgwEYxwEYsQMY0QMYigUYkQIYlwUY3AQY3gQY4ATYAQLCAhYQLhiKBRixAxhDGIsDGPADGKgDGJsDwgIJEC4YigUYChhDwgIFEC4YgATCAiUQLhiKBRixAxhDGIsDGPADGKgDGJsDGJcFGNwEGN4EGOAE2AECwgIYEC4YigUYChhDGJcFGNwEGN4EGOAE2AECwgIWEC4YigUYQxiXBRjcBBjeBBjgBNgBAsICCxAuGIAEGLEDGIMBwgIKEAAYigUYsQMYQ8ICDhAAGIAEGLEDGIMBGMkDwgIOEC4YigUYsQMYgwEYkQLCAhAQLhiKBRixAxiDARjlBBhDwgINEAAYigUYsQMYgwEYQ-IDBBgAIEGIBgGQBgi6BgQIARgKugYGCAIQARgU&sclient=gws-wiz-serp"
mixer.music.load(r"C:\Users\prajn\Music\ShapeofRingtone.mp3") 
def get_response():
    user_message = user_input.get()
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, "You: " + user_message + "\n")
    chatbot_rules =['hi','sing me a song']
    for i in chatbot_rules:
        if "hi" == user_message:
            response = "Hello! Long time no see buddy..."
        elif "how are you" == user_message:
            response = "I am fine,how are you?"
        elif "good" == user_message:
            response = "Hmm... How was your day by the way?"
        elif "sad" == user_message:
            response = "Its ok everything will be fine"
        elif "tell me a joke" == user_message:
            response = "Why does shrimp doesn't share    its tressure because it Is shellfish 😂😂😂😂"   
        elif "what is your name" == user_message:
            response = "My name is Bangtan🫰🏻"
        elif "sing me a song" == user_message:
            response = mixer.music.play()
        elif "Stop" == user_message:
            response = mixer.music.stop()
        elif "I am bored" == user_message:
            response = webbrowser.open(youtube_url2)
        elif "bye" == user_message:
            response = "Goodbye! Have a great day."
        elif "ha ha" == user_message:
            response = "ha ha ha..."    
        else:
            response ="Sorry I didn't catch it"

    chat_display.insert(tk.END, "Chatbot: " + response + "\n")
    chat_display.config(state=tk.DISABLED)
    user_input.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.configure(bg="light gray") 
window.title("Bangtan💜")

# Create a chat display
chat_display = tk.Text(window, height=20,bg="lavender", width=40, state=tk.DISABLED)
chat_display.pack()

# Create a user input field
user_input = tk.Entry(window, width=40,bg="white")
user_input.pack()

# Create a send button
send_button = tk.Button(window, text="Send", command=get_response,bg="grey")
send_button.pack()

# Start the Tkinter main loop
window.mainloop()





