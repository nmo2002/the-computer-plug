import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home
from ..Parts import Parts
from ..MyParts import MyParts

urls = {'home': Home, 'parts': Parts, 'my-parts': MyParts}
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from .Base import Module1
#
#    Module1.say_hello()
#

def say_hello():
  print("Hello, world")
