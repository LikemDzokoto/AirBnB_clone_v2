#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
import unittest
from models.base_model import BaseModel
from models.state import State
from os import getenv, remove 
import pep8

storage = getenv("HBNB_TYPE_STORAGE", "fs")

class TestState(unittest.TestCase):
    """Test the State class. """
    @classmethod
    def setUpClass(cls):
        '''
            Sets up unittest
        '''
        cls.new_state = State()
        cls.new_state.name = "California"

    @classmethod
    def tearDownClass(cls):
        del cls.new_state
        try:
            remove("file.json")
        except FileNotFoundError:
            pass




    def __init__(self, *args, **kwargs):        
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


    def test_States_dbtable(self):
        '''
            Check if the tablename is correct
        '''
        self.assertEqual(self.new_state.__tablename__, "states")

    def test_State_inheritance(self):
        self.assertIsInstance(self.new_state,Basemodel)


    @unittest.skipIf(storage == "db", "Testing database storage only")
    def test_State_attributes_type(self):
        '''
            Test that State class attribute name is class type str.
        '''
        name = getattr(self.new_state, "name")
        self.assertIsInstance(name, str)
