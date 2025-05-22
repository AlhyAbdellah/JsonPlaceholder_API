import requests
import time
from faker import Faker
import random
from selenium.webdriver.support import expected_conditions as EC

#CRUD Complet avec JSONPlaceholder

base_url="https://jsonplaceholder.typicode.com/posts"

#Test Read
def test_read_all_posts():
    response=requests.get(base_url)
    assert response.status_code ==200
    assert isinstance(response.json(),list)

#Test Creat
def test_creat_post():
    fake=Faker()
    data={"title":fake.sentence(), "body":fake.text(),"userId":random.randint(1,10)
    }
    response=requests.post(base_url,json=data)
    assert response.status_code == 201
    json_data=response.json()
    assert "id" in json_data
    assert json_data["title"]==data["title"]
    
#Test Update
def test_updat_post():
    fake=Faker()
    post_id=1
    data ={"id":post_id,
           "title":fake.sentence(),
           "body":fake.text(),
           "userId":random.randint(1,100)
    }
    response=requests.put(f"{base_url}/{post_id}",json=data)
    assert response.status_code==200
    assert response.json()["id"]==post_id

#Test Delete
def test_delet_post():
    post_id=1
    response=requests.delete(f"{base_url}/{post_id}")
    assert response.status_code ==200
