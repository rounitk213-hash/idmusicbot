# Cobra — Telegram Music Userbot
# Aapki ID se chalega, voice chat mein music play karega

import asyncio
import os
import sys
from pyrogram import Client, filters, idle
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, STRING_SESSION, DOWNLOADS_DIR, BOT_NAME
from utils.db import db
from utils.stream import stream_manager


# Downloads & Data folders create karo
os.makedirs(DOWNLOADS_DIR, exist_ok=True)
os.makedirs("data", exist_ok=True)

# Required Environment Variables check karo
if not API_ID or not API_HASH or not STRING_SESSION:
    print("""
=====================================================
❌ ERROR: MISSING REQUIRED ENVIRONMENT VARIABLES!
=====================================================
Please provide the following environment variables:
  1. API_ID         (from my.telegram.org)
  2. API_HASH       (from my.telegram.org)
  3. STRING_SESSION (Pyrogram string session)

👉 If deploying on Railway / Heroku / Render:
   Go to the 'Variables' (or 'Config Vars') tab
   and add API_ID, API_HASH, and STRING_SESSION.
=====================================================
""")
    sys.exit(1)


# Pyrogram Client — Userbot mode (aapki ID se chalega)
app = Client(
    name="Cobra",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
    plugins=dict(root="plugins"),
)

# PyTgCalls — Voice chat handle karega
pytgcalls = PyTgCalls(app)


# Auto-save users and groups jab bhi koi message aaye
@app.on_message(filters.group, group=-1)
async def auto_save_handler(client, message):
    """Har group message pe user aur group save karo DB mein."""
    try:
        db.save_group(message.chat.id)
        if message.from_user:
            db.save_user(message.from_user.id)
    except Exception:
        pass


@app.on_message(filters.private & filters.incoming, group=-1)
async def auto_save_private(client, message):
    """Private messages se bhi users save karo."""
    try:
        if message.from_user:
            db.save_user(message.from_user.id)
    except Exception:
        pass


async def main():
    """Bot start karo."""
    print(f"""  
╔══════════════════════════════════╗
║     🎵 {BOT_NAME} Started! 🎵     ║
║                                  ║
║  Commands:                       ║
║  .play   - Play music            ║
║  .vplay  - Play video            ║
║  .skip   - Skip song             ║
║  .stop   - Stop & leave VC       ║
║  .pause  - Pause stream          ║
║  .resume - Resume stream         ║
║  .queue  - Show queue            ║
║  .np     - Now playing           ║
║  .broadcast - Broadcast msg      ║
║  .stats  - Bot statistics        ║
╚══════════════════════════════════╝
""")
    
    await app.start()
    stream_manager.setup(pytgcalls)
    await pytgcalls.start()
    
    me = await app.get_me()
    print(f"✅ Logged in as: {me.first_name} (@{me.username})")
    print(f"✅ User ID: {me.id}")
    print(f"✅ PyTgCalls ready — Voice chat support active!")
    print("\n🎵 Bot is running... Press Ctrl+C to stop.")
    
    await idle()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
