import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token="f17d2f2e41b3f67ad489d85ce6966c0a42f391f0a30d0ecf730bc46fe019fb8750e9755f09889d08a7849")

vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

mes = ["Привет", "Как дела?", "Отстань", "Что делаешь?", "Какое ДЗ?"]

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.from_user:

            vk.messages.send(
                user_id=event.user_id,
                message=mes[random.randint(0, 4)],
                random_id=random.randint(1, 2147483647),
            )