# Telegram Bot using Python-Telegram-bot

Welcome to the Telegram Bot project developed for the [AccioINTERN](https://github.com/AccioINTERN) internship program. This project aims to create a simple Telegram bot using Python and the python-telegram-bot library.

## Project Description

This Telegram bot is designed to greet users when they message it and handle basic commands. It also includes functionality to store user preferences such as name and language in a SQLite database.

### Features

- **Greeting**: The bot welcomes users when they start a conversation.
- **Command Handling**: It gracefully handles unknown commands with a default response.
- **Database Integration**: User preferences (e.g., name, language) are stored in an SQLite database.

## Requirements

- Basic understanding of Python programming language.
- No prior experience with the Telegram Bot API is required.

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AccioINTERN/Telegram_Bot_Internship.git
   cd Telegram_Bot_Internship
   ```

2. **Install dependencies**:
   Make sure you have Python installed. Install required libraries using pip:
   ```bash
   pip install python-telegram-bot
   ```

3. **Configuration**:
   - Obtain a Telegram Bot API token from BotFather on Telegram.
   - Replace `"your_telegram_bot_token"` in `bot.py` with your actual token.

4. **Database Setup**:
   - The bot uses SQLite for database operations. No additional setup is required for basic usage.

## Usage

Run the bot script `bot.py`:
```bash
python bot.py
```

## Contributing

Contributions are welcome! Please refer to the [CONTRIBUTING.md](https://github.com/AccioINTERN/.github/blob/main/profile/CONTRIBUTING.md) file for guidelines.

## Acknowledgments

Thank you to AccioINTERN for providing this internship opportunity!
