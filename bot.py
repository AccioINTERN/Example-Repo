import sqlite3
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace with your bot's API token
TOKEN = "your_telegram_bot_token"

# Connect to SQLite database (you can replace this with other DB libraries like SQLAlchemy)
conn = sqlite3.connect('user_preferences.db')
cursor = conn.cursor()

# Create table for storing user preferences
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        chat_id INTEGER NOT NULL,
        first_name TEXT,
        language TEXT
    )
''')
conn.commit()

# Bot commands handler
def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id
    first_name = update.effective_user.first_name
    
    # Check if user already exists in the database
    cursor.execute('SELECT * FROM users WHERE chat_id=?', (chat_id,))
    existing_user = cursor.fetchone()
    
    if not existing_user:
        # Insert new user into the database
        cursor.execute('INSERT INTO users (chat_id, first_name) VALUES (?, ?)', (chat_id, first_name))
        conn.commit()
    
    update.message.reply_text(f"Hello {first_name}! Welcome to the Telegram Bot.")

def unknown(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Sorry, I didn't understand that command.")

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    # Handlers for commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
