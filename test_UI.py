from app import app
def test_html_page():
    with app.test_client() as c:
        home = c.get('/')
        html = home.data.decode()
        assert 'Hello World' in html
