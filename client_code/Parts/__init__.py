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
from ..Checkout import Checkout


class Parts(PartsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_parts()
    
  def back(self):
    self.content_panel.clear()
    self.load_parts()
  
  def render_checkout(self, part_name):
    self.content_panel.clear()
    self.content_panel.add_component(Checkout(part_name, self.back))
    
  def load_parts(self):
    parts = anvil.server.call('get_all_parts').search()
    course_panel = GridPanel()
    
    for i, part in enumerate(parts):
      p = PartItem(name=part['name'], button_text = f'Buy for ${part["price"]}', description=part['description'], image=part['image'], button_callback=self.render_checkout)
      course_panel.add_component(p, row=str(i//2), width_xs=6)
    # Any code you write here will run before the form opens.
    self.content_panel.add_component(course_panel)
