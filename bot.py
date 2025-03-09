from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CallbackContext, CommandHandler
from telethon import version  # Import version from Telethon to display it

# Bot token from BotFather
TOKEN = '7274292874:AAE_qc_1LcUIleztZMpOjKrxB_PAYt0o2aY'
# Your personal chat ID to forward the messages
CHAT_ID = '-1002217780167'

UPIC = "https://envs.sh/_Cf.jpg"

CAPTION = "ʜᴇʟʟᴏ ɪ ᴀᴍ ʏᴏᴜʀ ꜰᴏʀᴡᴀʀᴅɪɴɢ ʙᴏᴛ.\nɪ ᴡɪʟʟ ꜰᴏʀᴡᴀʀᴅ ᴍᴇꜱꜱᴀɢᴇꜱ ꜰʀᴏᴍ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ʏᴏᴜʀ ᴘᴇʀꜱᴏɴᴀʟ ᴄʜᴀᴛ.\n\n"
CAPTION += f"ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴏꜰꜰɪᴄɪᴀʟ ʜᴀᴄᴋᴇʀ\n\n"


# This function will forward the messages from the channel to your personal chat
async def forward_post(update: Update, context: CallbackContext):
    # Log the type of update we are getting
    print(f"Received update: {update}")

    # Check if the update contains a channel post and forward it
    if update.channel_post:
        try:
            # Forward the message from channel to your personal chat
            await context.bot.forward_message(chat_id=CHAT_ID, from_chat_id=update.channel_post.chat.id, message_id=update.channel_post.message_id)
            print(f"Forwarded message from channel {update.channel_post.chat.id} to personal chat {CHAT_ID}.")
        except Exception as e:
            print(f"Error while forwarding message: {e}")
    else:
        print("No valid message found in the update.")

# This function will send a message when the user sends /start command
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/Broken_Heart_72"),
            InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/raoxc"),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.effective_message.reply_photo(
        photo=UPIC,
        caption=CAPTION,
        reply_markup=reply_markup
    )

def main():
    # Initialize the Application with the provided token
    application = Application.builder().token(TOKEN).build()

    # Handler to capture /start command and send a reply
    application.add_handler(CommandHandler("start", start))

    # Handler to capture any post in the channel (text, photo, video, etc.)
    application.add_handler(MessageHandler(filters.ChatType.CHANNEL, forward_post))

    # Start the polling to receive messages
    application.run_polling()

if __name__ == '__main__':
    main()
