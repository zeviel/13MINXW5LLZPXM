from colorama import init
from colorama import Fore, Back, Style
init()
print(Back.BLACK)
print(Fore.CYAN)
print("Script by Zevi/Скрипт сделан Zevi")
print("┌────────────────────────────────────┐")
print("│Author :  LilZevi                   │")
print("│Github : https://github.com/LilZevi │")
print("└────────────────────────────────────┘")
print("YouTube: https://www.youtube.com/channel/UCJ61JlXJckmO6yJr8BDRuGQ")
print('▄▀▄ █▄░▄█ ▀ █▄░█ ▄▀▄ █░░░█ ▄▀▄ █░░ █░░ ▄▀▀ █▀▄ ▄▀▄ █▄░▄█')
print("█▀█ █░█░█ █ █░▀█ █░█ █░█░█ █▀█ █░▄ █░▄ ░▀▄ █░█ █▀█ █░█░█")
print("▀░▀ ▀░░░▀ ▀ ▀░░▀ ░▀░ ░▀░▀░ ▀░▀ ▀▀▀ ▀▀▀ ▀▀░ █▀░ ▀░▀ ▀░░░▀")
import amino
email = input("Email/Почта:")
password = input("Password/Пароль:")
client = amino.Client()
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=1000)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("Выберите сообщество/Select the community: "))-1]
sub_client = amino.SubClient(comId=communityid, profile=client.profile)

print('\nLogged in/Бот зашел!')
userlink=input("Type user link/Введите ссылку на пользователя: ")
user=client.get_from_code(userlink)
userId=user.objectId
sub_client=amino.SubClient(comId=communityid ,profile=client.profile)
comment=input("Message/Сообщение:")
while True:
	try:
		sub_client.comment(message=comment,userId=userId)
		print("WallComment Sended/Комментарий на стену отправлен!")
	except:
		pass
