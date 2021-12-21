import requests

# "key": "8373ef84f9c5b618af6ced50c1c0f89aa0071842c7d93bb46a592ee2"

get_headers_my_pets = {
    "auth_key ": "8373ef84f9c5b618af6ced50c1c0f89aa0071842c7d93bb46a592ee2",
    "filter": "my_pets"
}

get_params_my_pets = get_headers_my_pets

my_pets_link = "https://petfriends1.herokuapp.com/api/pets?filter=my_pets"


def get_pets_list(link, params, headers):
    response = requests.get(link,
                            params=params,
                            headers=headers
                            )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(get_pets_list(my_pets_link, get_params_my_pets, get_headers_my_pets))
