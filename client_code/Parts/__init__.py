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
    

  def load_parts(self):
    parts = anvil.server.call('get_part_details').search()
    course_panel = GridPanel()
    
    for i, part in enumerate(parts):
      p = PartItem(name=part['name'], button_text = f'Buy for ${part["price"]}', description=part['description'], image=part['image'], button_callback=None)
      course_panel.add_component(p, row=str(i//2), width_xs=6)
    # Any code you write here will run before the form opens.
    self.content_panel.add_component(course_panel)
