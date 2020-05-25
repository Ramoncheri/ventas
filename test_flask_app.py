import unittest
from test_base import TestFlaskBase

class TestWeb(TestFlaskBase):  #se lanza create app
   def test_server_on(self):
        resp= self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        
   def test_route_index_HolaMundo(self):
        resp= self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, b'Hola mundo')


if __name__ == '__main__':
    unittest.main()