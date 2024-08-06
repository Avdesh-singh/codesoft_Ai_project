import tkinter as tk
import re

class RuleBasedChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Rule-Based Chatbot")
        
        # Define colors
        self.bg_color = '#A4E1EC'
        self.text_color = '#CA3E55'
        self.entry_color = '#AC88D4'
        self.button_color = '#0E34F3'
        self.chat_bg = '#97A9C6'
        self.chat_color = '#F01B4C'

        self.rules = {
            'hi|hello|hey': 'Hello! How can I assist you today?',
            'what is your name|who are you': 'I am a chatbot created by awadhesh. How can I help you today?',
            'what can you do|how can you help me': 'I can answer questions, provide information, and assist with various tasks. Just let me know what you need!',
            'goodbye|bye|see you later': 'Goodbye! Have a great day!',
            'help|support|assist': 'Sure, I’m here to help! What do you need assistance with?',
            'what time is it|what is the weather today': "I'm sorry, I can't provide real-time information. You might want to check a weather website or app for that.",
            'feedback|provide feedback': "We’d love to hear your feedback! Please let us know what you think or how we can improve.",
            'appointment|book a meeting': "I can't schedule appointments directly, but I can help guide you on how to use our scheduling system.",
            'products|services': "We offer a range of products and services. Can you specify which product or service you are interested in?",
            'trouble|order didn’t go through': "I’m sorry to hear that. Can you provide more details about the issue? I’ll do my best to assist you.",
            'reset my password|update my profile': "For security reasons, I can't assist with account management directly. Please visit our website or contact support for help.",
            'faq|frequently asked questions': "You can find our FAQ page on our website under the 'Help' section.",
        }

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Text area for conversation history
        self.text_area = tk.Text(self.root, height=15, width=50, bg=self.chat_bg, fg=self.chat_color, state=tk.DISABLED)
        self.text_area.pack(pady=10)

        # Entry box for user input
        self.entry_box = tk.Entry(self.root, width=50, bg=self.entry_color, fg=self.text_color)
        self.entry_box.pack(pady=10)
        self.entry_box.bind("<Return>", self.process_input)

        # Button to send user input
        self.send_button = tk.Button(self.root, text="Send", command=self.process_input, bg=self.button_color, fg=self.entry_color)
        self.send_button.pack(pady=5)

        # Set window background color
        self.root.configure(bg=self.bg_color)

    def process_input(self, event=None):
        user_input = self.entry_box.get()
        if user_input.strip() == "":
            return

        self.display_message(f"You: {user_input}", "user")

        response = self.get_response(user_input)
        self.display_message(f"Chatbot: {response}", "bot")

        self.entry_box.delete(0, tk.END)

    def display_message(self, message, sender):
        self.text_area.config(state=tk.NORMAL)
        if sender == "user":
            self.text_area.insert(tk.END, message + '\n', ('user'))
        else:
            self.text_area.insert(tk.END, message + '\n', ('bot'))
        self.text_area.config(state=tk.DISABLED)
        self.text_area.yview(tk.END)

    def get_response(self, user_input):
        user_input = user_input.lower()
        for pattern, response in self.rules.items():
            if re.search(pattern, user_input):
                return response
        return "I'm not sure how to respond to that."

if __name__ == "__main__":
    root = tk.Tk()
    chatbot = RuleBasedChatbot(root)
    root.mainloop()
