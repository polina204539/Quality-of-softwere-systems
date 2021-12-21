import requests

post_new_pet_headers = {
    "auth_key": "8373ef84f9c5b618af6ced50c1c0f89aa0071842c7d93bb46a592ee2",
    "name": "Marsik",
    "animal_type": "kit",
    "age": '12',
    "pet_photo": ""
}

post_new_pet_params = post_new_pet_headers
new_pet_POST_link = "https://petfriends1.herokuapp.com/api/pets"


def post_new_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers,
                             files={"pet_photo": open('Cat.jpg', 'rb')}
                             )
    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    return response.text


print(post_new_pet(new_pet_POST_link, post_new_pet_params, post_new_pet_headers))
