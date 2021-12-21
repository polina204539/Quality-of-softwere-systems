import requests

delete_pet_headers = {
    "auth_key": "8373ef84f9c5b618af6ced50c1c0f89aa0071842c7d93bb46a592ee2",
    "pet_id": "b1295f44-a06a-4c45-8d55-688d41f69a36"
}

delete_pet_params = delete_pet_headers
DELETE_pet_link = "https://petfriends1.herokuapp.com/api/pets/" + "b1295f44-a06a-4c45-8d55-688d41f69a36"


def delete_pet(link, del_params, del_headers):
    response = requests.delete(link,
                               params=del_params,
                               headers=del_headers
                               )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(delete_pet(DELETE_pet_link, delete_pet_params, delete_pet_headers))
