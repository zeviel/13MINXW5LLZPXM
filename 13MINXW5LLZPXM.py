import amino
from pyfiglet import figlet_format
from colorama import init, Fore, Style
init()
print(
    f"""{Fore.CYAN}
Script by deluvsushi
Github : https://github.com/deluvsushi"""
)
print(figlet_format("13MINXW5LLZPXM", font="stop"))
client = amino.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
link_info = client.get_from_code(input("-- User link::: ")).json["extensions"]["linkInfo"]
com_id = link_info["ndcId"]
user_id = link_info["objectId"]
sub_client = amino.SubClient(comId=com_id, profile=client.profile)
message = input("-- Message::: ")
while True:
	try:
		sub_client.comment(userId=user_id, message=message)
		print("-- Comment is sent...")
	except Exception as e:
		print(e)
