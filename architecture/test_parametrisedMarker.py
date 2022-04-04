import pytest

#this piece of code can be worked when data  is to be provided in terms of csv files 
def get_data():
    return [

        ("user1","pass 1"),
        ("user2","pass 2"),
        ("user3","pass 3"),
        ("user4","pass 4"),
        ("user5","pass 5")

    ]

@pytest.mark.parametrize("username,password",get_data())
def test_dologin(username,password):
    print(username,"-------", password)