import aminofix
from pyfiglet import figlet_format
from colorama import init, Fore, Style
init()
print(
    f"""{Fore.CYAN}
Script by lilkek
TG : https://t.me/two_brothers_2"""
)
print(figlet_format("aminowallspam", font="stop"))
client = aminofix.Client()
email = input("-- Email::: ")
password = input("-- Password::: ")
client.login(email=email, password=password)
link_info = client.get_from_code(input("-- User link::: ")).json
com_id = link_info["extensions"]["linkInfo"]["ndcId"]
user_id = link_info["extensions"]["linkInfo"]["objectId"]
message = input("-- Message::: ")
while True:
	try:
		client.comment(userId=user_id, message=message)
		print("-- Comment is sent...")
	except Exception as e:
		print(e)
