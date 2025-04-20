import sys
from telegram.ext import Application, CommandHandler

def read_token():
    try:
        with open('token.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Token file (token.txt) not found.", file=sys.stderr)
        return None

TOKEN = read_token()

if not TOKEN:
    print("Bot token is missing. Please make sure the token.txt file exists.", file=sys.stderr)
    sys.exit(1)

def main():
    app = Application.builder().token(TOKEN).job_queue(None).build()

    app.run_polling()

if __name__ == '__main__':
    main()