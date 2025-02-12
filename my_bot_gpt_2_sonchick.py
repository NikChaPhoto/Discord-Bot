import discord
from transformers import pipeline
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
# Intents aktivieren
@client.event
async def on_ready():
    print(f'Bot {client.user} verbunden!')

@client.event
async def on_message(message):
    # Ignoriere Nachrichten vom Bot selbst
    if message.author == client.user:
        return

    print(f"Nachricht erhalten: '{message.content}'")  # Debugging

    # Verwende die gesamte Nachricht als Eingabe für die Textgenerierung
    prompt = message.content.strip()  # Entferne unnötige Leerzeichen

    if not prompt:
        await message.channel.send("Bitte geben Sie einen Text zur Generierung ein.")
        return

    try:
        print("Starte Textgenerierung...")  # Debugging
        response = text_generator(
            prompt,
            max_length=100,
            num_return_sequences=1,
            truncation=True,
            temperature=0.7,
            top_k=50,
            top_p=0.9
        )
        print(f"Antwort generiert: {response}")  # Debugging

        await message.channel.send(response[0]['generated_text'])

    except Exception as e:
        print(f"Fehler bei der Textgenerierung: {e}")
        await message.channel.send("Es ist ein Fehler bei der Textgenerierung aufgetreten.")

# Füge deinen neuen Token hier ein!
if __name__ == '__main__':
    if TOKEN:
        text_generator = pipeline('text-generation', model='gpt2', device=0)  # device(-1 - CPU, 0 - GPU)
        print("GPT-2-Modell geladen!")
        client.run(TOKEN)
    else:
        print("Der Token ist nicht vorhanden")