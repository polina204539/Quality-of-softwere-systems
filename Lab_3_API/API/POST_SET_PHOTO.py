import requests

post_set_photo_headers = {
    "auth_key": "8373ef84f9c5b618af6ced50c1c0f89aa0071842c7d93bb46a592ee2",
    "pet_id": "526c71d9-3787-4b72-b04f-da90293b869b"
}

post_set_photo_params = post_set_photo_headers
set_photo_POST_link = "https://petfriends1.herokuapp.com/api/pets/set_photo/" + "526c71d9-3787-4b72-b04f-da90293b869b"


def post_set_photo(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('dog.jpg', 'rb')}
                             )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(post_set_photo(set_photo_POST_link, post_set_photo_params, post_set_photo_headers))
