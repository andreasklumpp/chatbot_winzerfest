import gradio as gr
from chatbot import Chatbot
from config import Config

def main():
    """Main function to run the chatbot."""

    # Initialize chatbot
    chatbot = Chatbot()
    chatbot.initialize()
    config = Config()

    google_analytics_script = f"""
        <script async src="http://www.googletagmanager.com/gtag/js?id={config.GOOGLE_ANALYTICS_ID}"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', '{config.GOOGLE_ANALYTICS_ID}');
        </script>
    """

    # Create Gradio interface
    with gr.Blocks(head=google_analytics_script) as interface:
        gr.ChatInterface(
            fn = chatbot.chat,
            type="messages",
            title="🍷 Besigheimer Winzerfest Chatbot",
            description="Fragen Sie mich alles über das Besigheimer Winzerfest! Ich helfe Ihnen gerne mit Informationen zum Programm, den Ständen und Veranstaltungen."
        )

    interface.launch()

if __name__ == "__main__":
    main()