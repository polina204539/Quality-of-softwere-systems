import requests

put_info_headers = {
    "auth_key": "8373ef84f9c5b618af6ced50c1c0f89aa0071842c7d93bb46a592ee2",
    "pet_id": "569be327-4e73-471e-bfe8-b70525382412"
}

put_info_params = put_info_headers
put_info_link = "https://petfriends1.herokuapp.com/api/pets/" + "569be327-4e73-471e-bfe8-b70525382412"


def put_pet_info(link, p_params, p_headers):
    response = requests.put(link,
                            params=p_params,
                            headers=p_headers
                            )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(put_pet_info(put_info_link, put_info_params, put_info_headers))
