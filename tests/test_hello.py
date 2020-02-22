import pytest
from greetings import hi

def test_hello_any_world():
   assert hi.hello_any_world("Swahili") == 'Salamu Dunia!'

def test_hello_any_world2():
   assert hi.hello_any_world("French") == 'Bonjour monde!'

