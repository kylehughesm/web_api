

def test_index_status(client): 
    response = client.get('/')
    assert response.status_code == 200

