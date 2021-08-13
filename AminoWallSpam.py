import amino
import asyncio
import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(Fore.CYAN)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminowallspam", font="stop"))

async def main():
	client = amino.Client()
	email = input("Email >> ")
	password = input("Password >> ")
	await client.login(email=email, password=password)
	clients = await client.sub_clients(start=0, size=100)
	for x, name in enumerate(clients.name, 1):
		print(f"{x}.{name}")
	communityid = clients.comId[int(input("Select the community >> "))-1]
	sub_client = await amino.SubClient(comId=communityid, profile=client.profile)
	userlink = input("User Link >> ")
	user_info = await client.get_from_code(userlink)
	userId = user_info.objectId
	comment = input("Message >> ")
	while True:
		try:
			await sub_client.comment(message=comment, userId=userId)
			print("WallComment Sended")
		except:
			pass

asyncio.get_event_loop().run_until_complete(main())
