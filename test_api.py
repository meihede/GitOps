from app import app

def test_api_response():
    with app.test_client() as c:
        resource = c.get('/api/world')
        json = resource.get_json()
        assert 'hello world' == json['message']
