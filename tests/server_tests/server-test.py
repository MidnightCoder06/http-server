class Server:
    def __init__(self):
        self.database = Database()
        self.cache = Cache()
        self.server = Server()

  def test_put
    server = Server()
    put '/data/foo', 'sample object'
    res = JSON.parse(response.body)
    assert response.status == 201

  def test_get
    server = Server()
    put '/data/foo', 'sample object one'
    res_one = JSON.parse(response.body)

    put '/data/bar', 'sample object two'
    res2 = JSON.parse(response.body)

    get '/data/foo/'
    assert 'sample object one', response.body

    get '/data/bar'
    assert 'sample object two', response.body

  def test_get_nonexistant_data
    server = Server()
    get '/data/foo/bar'
    assert response.status == 404

  def test_delete
    server = Server()
    put '/data/foo', 'sample object'
    res = JSON.parse(response.body)

    delete '/data/foo'
    assert response.status == 200

    get '/data/foo'
    assert response.status == 404

  def test_delete_nonexistant_data
    server = Server()
    delete '/data/foo/bar'
    assert response.status == 404
