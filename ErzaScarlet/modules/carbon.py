import os
from ErzaScarlet import dispatcher
from telethon.tl import types, functions
from ErzaScarlet.utils.functions import make_carbon


from ErzaScarlet.events import register

@register(pattern="^/carbon")
async def _(event):
    reply = await event.get_reply_message()
    msg = reply.message
    user = (
        await event.client.get_entity(reply.forward.sender) ) 
    carbon = await make_carbon(message.reply_to_message.text)
       await event.client.send_document(message.chat.id, carbon)
       

    


