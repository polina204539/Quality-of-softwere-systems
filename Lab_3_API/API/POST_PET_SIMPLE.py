import requests
# "key": "8373ef84f9c5b618af6ced50c1c0f89aa0071842c7d93bb46a592ee2"


# POST PET SIMPLE
post_simple_headers = {
    "auth_key": "8373ef84f9c5b618af6ced50c1c0f89aa0071842c7d93bb46a592ee2",
    "name": "jarman",
    "animal_type": "Doberman",
    "age": '3'
}

post_simple_params = post_simple_headers
create_pet_simple_POST_link = "https://petfriends1.herokuapp.com/api/create_pet_simple"


def post_simple_pet(link, post_params, post_headers):
    response = requests.post(link,
                             params=post_params,
                             headers=post_headers
                             )

    if response.status_code == 200:
        print("OK")

    if response.ok:
        print("OK")

    print(type(response), type(response.ok))
    return response.ok


print(post_simple_pet(create_pet_simple_POST_link, post_simple_params, post_simple_headers))

