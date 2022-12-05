# from discord import Webhook, AsyncWebhookAdapter
# import aiohttp

#URL = 'https://discordapp.com/api/webhooks/1043146108999848006/ODxjPglgK_t7jewfk-zBlwBC2Jx6g7GpQVopwokBsmriRRVo6vCeo2043HrWcyXcchS0'

# async def coroutine():
#   async with aiohttp.ClientSession() as session:
#     webhook = Webhook.from_url(URL, adapter=AsyncWebhookAdapter(session))
#     await webhook.send(content="Hello World")

import requests
from discord import Webhook, RequestsWebhookAdapter

webhook = Webhook.partial(1043146108999848006, 'ODxjPglgK_t7jewfk-zBlwBC2Jx6g7GpQVopwokBsmriRRVo6vCeo2043HrWcyXcchS0', adapter=RequestsWebhookAdapter())
webhook.send(content="últimas pruebas", username="Bee Bot de TIClass")
