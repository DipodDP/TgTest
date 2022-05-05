# from python_socks import ProxyType
from telethon import TelegramClient, events, utils
from telethon.network import ConnectionHttp

from config import load_config


config = load_config(".env")

# proxy = (socks.SOCKS5, ip, port)
# proxy = {
#     'proxy_type': ProxyType.HTTP,  # (mandatory) protocol to use (see above)
#     'addr': str(config.proxy[1]),  # (mandatory) proxy IP address
#     'port': int(config.proxy[2]),  # (mandatory) proxy port number
#     'username': 'foo',  # (optional) username if the proxy requires auth
#     'password': 'bar',  # (optional) password if the proxy requires auth
#     'rdns': False  # (optional) whether to use remote or local resolve, default remote
# }
# px.ProxyType.SOCKS5
# proxy = Proxy.from_url(str(config.proxy))

# proxy = python_socks.ProxyType.SOCKS4, "",
client = TelegramClient('my_account', config.api_id, config.api_hash)


@client.on(events.NewMessage)
async def my_event_handler(event):
    # ID чата
    chat_id = event.chat_id
    # Получаем ID Юзера+79835040412
    sender_id = event.sender_id
    # Получаем ID сообщения
    msg_id = event.id
    # получаем имя юзера
    sender = await event.get_sender()
    # Имя Юзера
    name = utils.get_display_name(sender)

    # получаем имя группы
    chat_from = event.chat if event.chat else (await event.get_chat())
    chat_title = utils.get_display_name(chat_from)

    # полчаем текст сообщения
    if event.message.message == '':
        msg = '* Hided *'
    else:
        msg = event.text.split('\n')
        msg = msg[0]
    with open("Chat_log.txt", 'a', encoding='utf-8') as f:
        f.writelines(f"ID: {event.date} {chat_id} {chat_title} >>  (ID: {sender_id})  {name} - (ID: {msg_id}) {msg}\n")
    print(f"ID: {event.date} {chat_id} {chat_title} >>  (ID: {sender_id})  {name} - (ID: {msg_id}) {msg}")


with client:
    print('Get_ID is running')
    client.run_until_disconnected()
