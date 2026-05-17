import telebot
import time

from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# =========================
# CONFIG
# =========================

TOKEN = "8955624602:AAEcOHX1q3XTvgKkDsJ1t7joGD6_4E7RFzE"

ADMIN_ID = 8348593052

SALE_ACTIVE = False

CHANNEL_LINK = "https://t.me/+CTbKykg35Rg0YWU1"

bot = telebot.TeleBot(TOKEN)

# =========================
# ANTI SPAM
# =========================

user_cooldown = {}

MESSAGE_DELAY = 1

# =========================
# START COMMAND
# =========================

@bot.message_handler(commands=['start'])
def start(message):

    markup = ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    btn1 = KeyboardButton("🛒 Buy Key")

    btn2 = KeyboardButton("💰 Mod Price List")
    btn3 = KeyboardButton("🛠 Support")

    btn4 = KeyboardButton("👤 Account Purchase")
    btn5 = KeyboardButton("🔥 Sale")

    markup.row(btn1)
    markup.row(btn2, btn3)
    markup.row(btn4, btn5)

    bot.send_animation(
        message.chat.id,
        open("welcome.mp4", "rb"),

        caption=(
            "🔥 *Welcome To Anony Support Bot*\n\n"

            "━━━━━━━━━━━━━━━\n\n"

            "⚡ Fast Support\n"
            "🎮 Premium Mods\n"
            "🛒 Instant Purchases\n"
            "👤 Account Marketplace\n\n"

            "━━━━━━━━━━━━━━━\n\n"

            "👇 Select an option below"
        ),

        parse_mode="Markdown",
        reply_markup=markup
    )

# =========================
# MAIN HANDLER
# =========================

@bot.message_handler(
    func=lambda message:
    not (
        message.text
        and message.text.startswith("/")
    )
)
def handle_message(message):

    user_id = message.from_user.id
    current_time = time.time()

    text = ""

    if message.text:
        text = message.text.lower()

    # =====================
    # SAFE BUTTONS
    # =====================

    safe_buttons = [
        "🛒 buy key",
        "💰 mod price list",
        "🛠 support",
        "👤 account purchase",
        "🔥 sale"
    ]

    # =====================
    # ANTI SPAM
    # =====================

    if text not in safe_buttons:

        if user_id in user_cooldown:

            if current_time - user_cooldown[user_id] < MESSAGE_DELAY:

                bot.reply_to(
                    message,
                    "⚠️ Please slow down."
                )
                return

        user_cooldown[user_id] = current_time

    # =====================
    # PRICE LIST
    # =====================

    if "mod price list" in text:

        bot.reply_to(
            message,

            "━━━━━━━━━━━━━━━\n"
            "💰 *MOD PRICE LIST*\n"
            "━━━━━━━━━━━━━━━\n\n"

            "🎮 *OPBR*\n"
            "• 1 Month → `$5`\n"
            "• 1 Year → `$20`\n"
            "• Lifetime → `$35`\n\n"

            "🎮 *BGMI*\n"
            "• 1 Month → `$4`\n"
            "• 1 Year → `$18`\n"
            "• Lifetime → `$30`\n\n"

            "━━━━━━━━━━━━━━━\n"
            "⚡ Powered By AnonyxMod",

            parse_mode="Markdown"
        )

    # =====================
    # BUY KEY
    # =====================

    elif "buy key" in text:

        bot.send_message(
            message.chat.id,
            "⏳ Loading Products..."
        )

        markup = InlineKeyboardMarkup()

        btn1 = InlineKeyboardButton(
            "🔥 OPBR",
            callback_data="product_opbr"
        )

        btn2 = InlineKeyboardButton(
            "⚡ BGMI",
            callback_data="product_bgmi"
        )

        markup.add(btn1)
        markup.add(btn2)

        bot.send_message(
            message.chat.id,
            "━━━━━━━━━━━━━━━\n"
            "🛒 SELECT PRODUCT\n"
            "━━━━━━━━━━━━━━━",
            reply_markup=markup
        )

    # =====================
    # SUPPORT
    # =====================

    elif "support" in text:

        bot.reply_to(
            message,

            "━━━━━━━━━━━━━━━\n"
            "🛠 *SUPPORT CENTER*\n"
            "━━━━━━━━━━━━━━━\n\n"

            "Send your issue.\n"
            
            "Admin will reply shortly.\n\n"

            "━━━━━━━━━━━━━━━\n"
            "⚡ Powered By AnonyxMod",

            parse_mode="Markdown"
        )

    # =====================
    # ACCOUNT PURCHASE
    # =====================

    elif "account purchase" in text:

        bot.reply_to(
            message,

            "━━━━━━━━━━━━━━━\n"
            "👤 *ACCOUNT PURCHASE*\n"
            "━━━━━━━━━━━━━━━\n\n"

            "🛒 Browse Available Accounts:\n"
            "https://t.me/+63XIbT-MOtQ5ZjY1\n\n"

            "💸 For Custom Accounts\n"
            "Message Owner @AnonyxMod\n\n"

            "━━━━━━━━━━━━━━━\n"
            "⚡ Powered By AnonyxMod",

            parse_mode="Markdown"
        )

    # =====================
    # SALE
    # =====================

    elif "sale" in text:

        global SALE_ACTIVE

        if SALE_ACTIVE:

            bot.reply_to(
                message,

                "🔥 *LIMITED SALE ACTIVE* 🔥\n\n"

                "━━━━━━━━━━━━━━━\n\n"

                "🎮 *OPBR*\n"
                "• Lifetime → `$25`\n\n"

                "🎮 *BGMI*\n"
                "• Lifetime → `$20`\n\n"

                "━━━━━━━━━━━━━━━\n"
                "⚠️ Limited Time Offer",

                parse_mode="Markdown"
            )

        else:

            bot.reply_to(
                message,

                "━━━━━━━━━━━━━━━\n"
                "🔒 *NO ACTIVE SALE*\n"
                "━━━━━━━━━━━━━━━\n\n"

                "No active sale right now.\n\n"

                "━━━━━━━━━━━━━━━\n"
                "⚡ Powered By AnonyxMod",

                parse_mode="Markdown"
            )

    # =====================
    # FORWARD OTHER MSGS
    # =====================

    else:

        ignored = [
            "🛒 buy key",
            "💰 mod price list",
            "🛠 support",
            "👤 account purchase",
            "🔥 sale"
        ]

        if text in ignored:
            return

        if message.chat.id != ADMIN_ID:

            bot.forward_message(
                ADMIN_ID,
                message.chat.id,
                message.message_id
            )

            bot.reply_to(
                message,
                "✅ Message sent to admin."
            )

# =========================
# CALLBACK SYSTEM
# =========================

@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):

    bot.answer_callback_query(call.id)

    # =====================
    # PRODUCT SELECT
    # =====================

    if call.data.startswith("product_"):

        product = call.data.replace("product_", "")

        markup = InlineKeyboardMarkup()

        btn1 = InlineKeyboardButton(
            "1 Month",
            callback_data=f"duration_{product}_1Month"
        )

        btn2 = InlineKeyboardButton(
            "1 Year",
            callback_data=f"duration_{product}_1Year"
        )

        btn3 = InlineKeyboardButton(
            "Lifetime",
            callback_data=f"duration_{product}_Lifetime"
        )

        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)

        bot.edit_message_text(
            "━━━━━━━━━━━━━━━\n"
            f"🎮 PRODUCT: {product.upper()}\n"
            "━━━━━━━━━━━━━━━\n\n"
            "⏳ Select Duration:",

            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )

    # =====================
    # DURATION SELECT
    # =====================

    elif call.data.startswith("duration_"):

        data = call.data.split("_")

        product = data[1]
        duration = data[2]

        markup = InlineKeyboardMarkup()

        btn1 = InlineKeyboardButton(
            "💳 PayPal",
            callback_data=f"payment_{product}_{duration}_PayPal"
        )

        btn2 = InlineKeyboardButton(
            "🟡 Binance",
            callback_data=f"payment_{product}_{duration}_Binance"
        )

        btn3 = InlineKeyboardButton(
            "🪙 Crypto",
            callback_data=f"crypto_{product}_{duration}"
        )
        
        btn4 = InlineKeyboardButton(
            "🇮🇳 UPI",
            callback_data=f"payment_{product}_{duration}_UPI"
        )

        btn5 = InlineKeyboardButton(
            "🎁 Gift Cards",
            callback_data=f"payment_{product}_{duration}_GiftCards"
        )

        markup.add(btn1)
        markup.add(btn2)
        markup.add(btn3)
        markup.add(btn4)
        markup.add(btn5)

        bot.edit_message_text(
            "━━━━━━━━━━━━━━━\n"
            "💰 SELECT PAYMENT METHOD\n"
            "━━━━━━━━━━━━━━━\n\n"

            f"🎮 Product: {product.upper()}\n"
            f"⏳ Duration: {duration}",

            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )

    # =====================
    # CRYPTO
    # =====================

    elif call.data.startswith("crypto_"):

        data = call.data.split("_")

        product = data[1]
        duration = data[2]

        markup = InlineKeyboardMarkup()

        btn1 = InlineKeyboardButton(
            "USDT TRC20",
            callback_data=f"payment_{product}_{duration}_TRC20"
        )

        btn2 = InlineKeyboardButton(
            "USDT BEP20",
            callback_data=f"payment_{product}_{duration}_BEP20"
        )

        markup.add(btn1)
        markup.add(btn2)

        bot.edit_message_text(
            "━━━━━━━━━━━━━━━\n"
            "🪙 SELECT NETWORK\n"
            "━━━━━━━━━━━━━━━",

            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )

    # =====================
    # PAYMENT INFO
    # =====================

    elif call.data.startswith("payment_"):

        data = call.data.split("_")

        payment = data[3]

        payment_text = ""

        if payment == "PayPal":

            payment_text = (
                "💳 *PAYPAL PAYMENT*\n\n"
                "singhgurkirpal473@gmail.com\n\n"
            )

        elif payment == "Binance":

            payment_text = (
                "🟡 *BINANCE PAYMENT*\n\n"
                "1127340862\n\n"
            )

        elif payment == "TRC20":

            payment_text = (
                "🪙 *USDT TRC20*\n\n"
                "`TLGTEeFo2Rz6dZ7rHwtFFuhHpM6oQGGnLZ`\n\n"
                "📋 Click to copy"
            )

        elif payment == "BEP20":

            payment_text = (
                "🪙 *USDT BEP20*\n\n"
                "`0x2c423f9331bbfb0dd00b751a721ec1c8606b2e29`\n\n"
                "📋 Click to copy"
            )

        elif payment == "UPI":

            payment_text = (
                "🇮🇳 *UPI PAYMENT*\n\n"
                "`anonyxmod@ptaxis`\n\n"
                "📋 Click to copy"
            )

        elif payment == "GiftCards":

            payment_text = (
                "🎁 *GIFT CARD PAYMENT*\n\n"

                "Message Owner @AnonyxMod\n"
                "to continue your purchase."
            )

        if payment == "GiftCards":

            bot.edit_message_text(
                payment_text,

                call.message.chat.id,
                call.message.message_id,
                parse_mode="Markdown"
            )

        else:

            bot.edit_message_text(
                "━━━━━━━━━━━━━━━\n"
                "💳 PAYMENT INFO\n"
                "━━━━━━━━━━━━━━━\n\n"

                f"{payment_text}\n\n"

                "━━━━━━━━━━━━━━━\n"
                "📸 After payment,\n"
                "send screenshot here.",

                call.message.chat.id,
                call.message.message_id,
                parse_mode="Markdown"
            )

# =========================
# SCREENSHOT SYSTEM
# =========================

@bot.message_handler(content_types=['photo'])
def photo_handler(message):

    bot.send_photo(
        ADMIN_ID,
        message.photo[-1].file_id,

        caption=(
            f"🛒 New Purchase Request\n\n"
            f"👤 User: @{message.from_user.username}\n"
            f"🆔 USER_ID:{message.from_user.id}\n\n"

            "Customer sent payment screenshot."
        )
        )

    bot.reply_to(
        message,
        "✅ Payment screenshot sent.\n"
        "Admin will verify it shortly."
    )

# =========================
# ADMIN REPLY SYSTEM
# =========================

@bot.message_handler(
    func=lambda message:
    message.chat.id == ADMIN_ID
    and message.reply_to_message is not None
)
def admin_reply(message):

    try:

        reply_text = ""

        if message.reply_to_message.text:
            reply_text = message.reply_to_message.text

        elif message.reply_to_message.caption:
            reply_text = message.reply_to_message.caption

        if "USER_ID:" not in reply_text:
            return

        user_id = int(
            reply_text.split("USER_ID:")[1]
            .split("\n")[0]
            .strip()
        )

        bot.send_message(
            user_id,

            "━━━━━━━━━━━━━━━\n"
            "📩 *ADMIN REPLY*\n"
            "━━━━━━━━━━━━━━━\n\n"

            f"{message.text}\n\n"

            "━━━━━━━━━━━━━━━\n"
            f"📢 Join Channel:\n{CHANNEL_LINK}",

            parse_mode="Markdown"
        )

        bot.reply_to(
            message,
            "✅ Reply sent to customer."
        )

    except:
        pass

# =========================
# SALE ON
# =========================

@bot.message_handler(commands=['saleon'])
def sale_on(message):

    global SALE_ACTIVE

    if message.chat.id != ADMIN_ID:
        return

    SALE_ACTIVE = True

    bot.reply_to(
        message,
        "✅ Sale Enabled."
    )

# =========================
# SALE OFF
# =========================

@bot.message_handler(commands=['saleoff'])
def sale_off(message):

    global SALE_ACTIVE

    if message.chat.id != ADMIN_ID:
        return

    SALE_ACTIVE = False

    bot.reply_to(
        message,
        "❌ Sale Disabled."
    )

# =========================
# RUN BOT
# =========================

print("Bot Running...")

while True:

    try:

        bot.infinity_polling(
            timeout=30,
            long_polling_timeout=30,
            skip_pending=True
        )

    except Exception as e:

        print(f"Error: {e}")
        time.sleep(5)
