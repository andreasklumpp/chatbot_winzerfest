import gradio as gr
from chatbot import Chatbot

def main():
    """Main function to run the chatbot."""

    # Initialize chatbot
    chatbot = Chatbot()
    chatbot.initialize()

    # Create Gradio interface
    interface = gr.ChatInterface(
        fn = chatbot.chat,
        type="messages",
         title="🍷 Besigheimer Winzerfest Chatbot",
        description="Fragen Sie mich alles über das Besigheimer Winzerfest! Ich helfe Ihnen gerne mit Informationen zum Programm, den Ständen und Veranstaltungen."
    )

    interface.launch()

if __name__ == "__main__":
    main()