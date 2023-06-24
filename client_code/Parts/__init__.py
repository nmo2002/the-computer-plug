from ._anvil_designer import PartsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

class Parts(PartsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_parts()

  def load_parts(self):
    parts = anvil.server.call('get_part_details').search()
    for part in parts:
      print(part)
    # Any code you write here will run before the form opens.
