import AminoLab
import pyfiglet
from colorama import init, Fore, Back, Style
init()
print(Fore.CYAN)
print("""Script by deluvsushi
Github : https://github.com/deluvsushi""")
print(pyfiglet.figlet_format("aminowallspam", font="stop"))
client = AminoLab.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)
comment = input("Comment >> ")
user_info = client.get_from_link(input("User Link >> "))
user_id = user_info.object_Id; ndc_Id = user_info.ndc_Id

while True:
	try:
		client.submit_comment(ndc_Id=ndc_Id, message=comment, user_Id=user_id)
		print("Sended Comment")
	except Exception as e:	print(e)
