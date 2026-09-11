# 🐍 Cobra — Telegram ID Music Userbot

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new)

Aapki **apni Telegram ID** se chalega ek powerful **Music Userbot**. Voice chat mein music play karega. Link ya song name do — gaana bajega!

![Cobra Thumbnail](https://graph.org/file/a0d949ae033c97bb60c0b-238eeecbc9c32d092f.mp4)

---

## ✨ Features

- 🐍 **Userbot Mode** — Aapki personal ID se voice chat join karta hai
- 🎵 **Yuki Music API** — Superfast audio & video stream download
- 🎬 **Video Stream** — VC mein HD video stream support (`.vplay`)
- 📁 **Direct Audio Reply** — Kisi bhi audio/voice message pe reply karke `.play` karo
- 📋 **Queue System** — Unlimited songs queue support
- 📥 **Chat Downloader** — Direct audio (`.song`) aur video (`.vsong`) download chat mein
- 📝 **Lyrics Finder** — Instant lyrics search (`.lyrics`)
- 📢 **Broadcast** — Sabhi saved users aur groups ko ek click me message bhejo
- 📊 **Live Stats & Ping** — Bot uptime, system stats, ping response
- ☁️ **Cloud Ready** — Railway, Docker, Heroku & VPS 1-click deploy support

---

## 📋 Commands List

### 🎶 Voice Chat Player
| Command | Description |
|---------|-------------|
| `.play <query/link>` | 🎵 Voice chat mein audio stream play karega |
| `.play` *(reply to audio)* | 📁 Kisi bhi audio/voice message ko direct VC mein play karega |
| `.vplay <query/link>` | 🎬 Voice chat mein video stream play karega |
| `.skip` | ⏭️ Current gaana skip karke agla play karega |
| `.stop` | ⏹️ Playback stop karke voice chat chhod dega |
| `.pause` | ⏸️ Stream ko pause karega |
| `.resume` | ▶️ Paused stream ko wapas resume karega |
| `.queue` | 📋 Up next queue list dikhayega |
| `.np` | 🎧 Abhi baj raha gaana (Now Playing) info |

### 📥 Direct Downloader & Tools
| Command | Description |
|---------|-------------|
| `.song <name/link>` | 🎵 Audio MP3 file download karke chat mein send karega |
| `.vsong <name/link>` | 🎬 Video file download karke chat mein send karega |
| `.lyrics <song>` | 📝 Gaane ke lyrics find karke layega |
| `.ping` | 🏓 Bot response time aur status check karega |
| `.stats` | 📊 Users, groups, played songs, CPU/RAM stats dikhayega |
| `.clean` | 🧹 Downloads folder saaf karega *(Owner Only)* |
| `.broadcast <msg>` | 📢 Sabhi users/groups ko broadcast message karega *(Owner Only)* |
| `.help` | ❓ Sabhi commands ka menu dikhayega |

---

## 🛠 Required Environment Variables

| Variable | Description | Example / Default |
|----------|-------------|-------------------|
| `API_ID` | Telegram API ID ([my.telegram.org](https://my.telegram.org)) | `12345678` |
| `API_HASH` | Telegram API Hash ([my.telegram.org](https://my.telegram.org)) | `0123456789abcdef0123456789abcdef` |
| `STRING_SESSION` | Pyrogram String Session of your Account | `BQAF...` |
| `OWNER_ID` | Your Telegram User ID *(Optional)* | `1234567890` |
| `MEOW_API_URL` | Yuki Music API Endpoint *(Optional)* | `https://music.yukiapi.site` |
| `MEOW_API_KEY` | Yuki Music API Key *(Optional)* | `yuki_28d18045448fe0df857d31dfe08fcdef` |
| `DEFAULT_THUMB_URL` | Default Media Thumbnail *(Optional)* | `https://graph.org/file/a0d949ae033c97bb60c0b-238eeecbc9c32d092f.mp4` |

---

## ☁️ Deploy on Railway

1. **GitHub Fork/Clone**: Apne GitHub account pe ye repo push/fork karo.
2. **Railway Project**: [Railway Dashboard](https://railway.app) pe jaao -> **New Project** -> **Deploy from GitHub repo**.
3. **Select Repository**: `idmusicbot` repository select karo.
4. **Environment Variables**: Project settings ke **Variables** tab mein jaao aur ye add karo:
   - `API_ID`
   - `API_HASH`
   - `STRING_SESSION`
   - `OWNER_ID` (Optional)
5. **Deploy**: Railway automatically Dockerfile detect karke build aur deploy kar dega! 🚀

---

## 🚀 Local Run / VPS Run

```bash
# 1. Clone repository
git clone https://github.com/rounitk213-hash/idmusicbot.git
cd idmusicbot

# 2. Setup virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install FFmpeg
sudo apt update && sudo apt install -y ffmpeg  # On Debian/Ubuntu

# 5. Create .env file
cp .env.example .env
# Edit .env and put your credentials

# 6. Run bot
python main.py
```

---

## 📁 Project Structure

```
idmusicbot/
├── Dockerfile             # Production Docker container with FFmpeg & build tools
├── .dockerignore          # Docker build exclusion rules
├── railway.json           # Railway deployment configuration
├── railway.toml           # Railway toml builder config
├── nixpacks.toml          # Nixpacks multi-phase build config
├── Procfile               # Heroku / Dokku process file
├── runtime.txt            # Python runtime specification
├── config.py              # Configuration & Environment loader
├── main.py                # Bot startup & PyTgCalls client
├── plugins/               # Bot command plugins
│   ├── play.py            # .play, .vplay, reply to audio
│   ├── controls.py        # .skip, .stop, .pause, .resume
│   ├── queue_cmd.py       # .queue, .np
│   ├── broadcast.py       # .broadcast (Owner only)
│   ├── stats.py           # .stats
│   └── extra.py           # .song, .vsong, .lyrics, .ping, .clean, .help
├── utils/                 # Core utilities
│   ├── db.py              # TinyDB storage for broadcast & stats
│   ├── queue_manager.py   # Song queue per chat
│   ├── stream.py          # PyTgCalls voice chat stream manager
│   └── youtube.py         # YouTube search & Yuki API downloader
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

**Made with ❤️ for Telegram Voice Chats**
