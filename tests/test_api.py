

def test_index_status(client): 
    response = client.get('/')
    assert response.status_code == 200

#Fetch Catalog The system must allow users to retrieve lists of tracks via GET
def test_get_tracks(client):
    response = client.get('/api/tracks')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

#Filter by Genre Users must be able to filter tracks by genre using query parameters.
def test_get_tracks_by_genre(client):
    response = client.get('api/tracks?genre_name=Rock')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)


#Create Inventory Authorized users must be able to add new albums via POST
