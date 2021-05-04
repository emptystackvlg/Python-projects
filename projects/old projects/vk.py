import vk_api

vk_session = vk_api.VkApi('+79610622806', '12345Pravda??')
vk_session.auth()

vk = vk_session.get_api()


print((message='Hello world'))