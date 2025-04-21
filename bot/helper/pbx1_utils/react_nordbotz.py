from random import choice
from bot import LOGGER, bot

async def send_react(message):
    try:
        chat_id = int(message.chat.id)
        chat_info = await bot.get_chat(chat_id)
        available_reactions = getattr(chat_info, "available_reactions", None)

        full_emoji_set = {
            "👌", "🔥", "🥰", "❤️", "❤️‍🔥",
            "💯", "⚡", "💋", "😘", "🤩", "😍",
        }

        if available_reactions:
            if getattr(available_reactions, "all_are_enabled", False):
                emojis = full_emoji_set
            else:
                emojis = {
                    r.emoji for r in available_reactions.reactions or []
                }

            if emojis:
                selected = choice(list(emojis))
                await message.react(selected, big=True)
                LOGGER.info(f"Reacted with: {selected}")
            else:
                LOGGER.warning("No emojis available for reaction.")
        else:
            LOGGER.warning("Reactions not available for this chat.")
    except Exception as e:
        LOGGER.error(f"send_react error: {e}")
