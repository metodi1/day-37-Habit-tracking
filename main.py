from datetime import datetime
import os
import requests

TOKEN = os.environ.get('TOKEN')
USERNAME = os.environ.get('USERNAME')
GRAF = "graf1"

pixe_end_point = 'https://pixe.la/v1/users'
today_date = datetime.today().date()
td = today_date.strftime("%Y%m%d")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# -------------- creat user-------------------------#

# respond = requests.post(url=pixe_end_point, json=user_params)
# # print(respond.text)

# -------------- creat the graf-------------------------#

# graf_end_point = f'{pixe_end_point}/{USERNAME}/graphs'
# graf_config = {
#     "id": GRAF,
#     "name": "Cycling graf",
#     "unit": "km",
#     "type": "float",
#     "color": "shibafu",
# }
# resopond = requests.post(url=graf_end_point, json=graf_config, headers=headers)

# -------------- add cycling-------------------------#


#
# add_cycling_point = f"{pixe_end_point}/{USERNAME}/graphs/{GRAF}"
# add_cycling_config = {
#     "date": td,
#     "quantity": "1200",
# }
# respond = requests.post(url=add_cycling_point, json=add_cycling_config, headers=headers)
# print(respond.text)

# -------------- Update cycling-------------------------#

# update_point = f'{pixe_end_point}/{USERNAME}/graphs/{GRAF}/{td}'
# update_config = {
#     "quantity": "1"
# }
#
# respond = requests.put(url=update_point, json=update_config, headers=headers)
# print(respond.text)

# -------------- Delete cycling-------------------------#
delete_point = f'{pixe_end_point}/{USERNAME}/graphs/{GRAF}/{td}'


respond = requests.delete(url=delete_point, headers=headers)
print(respond.text)