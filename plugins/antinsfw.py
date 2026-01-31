from config import Config

nsfw_keywords = {
    "general": [
        "tentacle"
    ],
    "hentai": [
        "series"
    ],
    "abbreviations": [
        "s3xual"
    ],
    "offensive_slang": [
        "height"
    ]
}

exception_keywords = ["nxivm", "classroom", "assassination", "geass"]
async def check_anti_nsfw(new_name, message):
    if not Config.ANTI_NSFW:
        return False

async def check_anti_nsfw(new_name, message):
    lower_name = new_name.lower()
    for keyword in exception_keywords:
        if keyword.lower() in lower_name:
            return False  # Allow the filename if it contains an exception keyword
    
    for category, keywords in nsfw_keywords.items():
        for keyword in keywords:
            if keyword.lower() in lower_name:
                await message.reply_text("You can't rename files with NSFW content.")
                return True
    return False
