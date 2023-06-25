from ._anvil_designer import PartsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..PartItem import PartItem


class Parts(PartsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_parts()
    p = PartItem(name = 'NVIDIA GeForce RTX 4090', button_text = 'Buy for #1599.99', description = 'Graphics card')
    self.content_panel.add_component(p)

  def load_parts(self):
    parts = anvil.server.call('get_part_details').search()
    
    for part in parts:
      print(part['name'])
    # Any code you write here will run before the form opens.
