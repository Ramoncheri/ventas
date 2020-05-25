from flask import Flask
from flask_testing import TestCase
import run

class TestFlaskBase(TestCase): #crea la app para usarla en los test
    def create_app(self):
        self.app= run.app
        return run.app

        

    def setUp(self):  #crea un cliente de testing
        self.client= self.app.test_client()  #cliente de testing
        self.client.testing= True
