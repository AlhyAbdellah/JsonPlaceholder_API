import requests
import time
from faker import Faker
import random
from selenium.webdriver.support import expected_conditions as EC

#CRUD Complet avec JSONPlaceholder

base_url="https://jsonplaceholder.typicode.com/posts"

#Read
def test_read_all_posts():
    response=requests.get(base_url)

    try:

        if response.status_code ==200:
            print(f"Read succesufflu, code is :{response.status_code}")
        else:
            print("Read failed")
    except:
        print("error {e}")
    
    print(f"message is :{response.json()}")

#Creat
def test_creat_post():
    fake=Faker()
    data={"title":fake.sentence(), "body":fake.text(),"userId":random.randint(1,10)
    }
    response=requests.post(base_url,json=data)
    if response.status_code == 201:
        print("\n Post created :", response.json())
        print(f"\n Statu Code is : {response.status_code}")
    else:
        print("Failed to creat post", response.status_code)

#Update
def test_updat_post():
    fake=Faker()
    post_id=1
    data ={"id":post_id,
           "title":fake.sentence(),
           "body":fake.text(),
           "userId":random.randint(1,100)
    }
    response=requests.put(f"{base_url}/{post_id}",json=data)
    if response.status_code==200:
        print(f"\n Post updated : {response.json()}, statu code is : {response.status_code}")
    else:
        print("Updat failed")

#Delete
def test_delet_post():
    post_id=1
    response=requests.delete(f"{base_url}/{post_id}")

    if response.status_code ==200:
        print(f"Post {post_id} deleted.")
    else:
        print("Failed to delete post.")

test_read_all_posts()
test_creat_post()
test_updat_post()
test_delet_post()