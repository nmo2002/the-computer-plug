from ._anvil_designer import MyPartsTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..PartItem import PartItem

class MyParts(MyPartsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_parts()
  
  def render_part(self, part_name):
    self.content_panel.clear()
    
  def load_parts(self):
    parts = anvil.server.call('get_my_parts')
    part_panel = GridPanel()

    if len(parts) > 0:
      self.no_parts_label.visible = False
      
    for i, part in enumerate(parts):
      p = PartItem(name=part['name'], button_text = 'View Content', description=part['description'], image=part['image'], button_callback=self.render_part)
      part_panel.add_component(p, row=str(i//2), width_xs=6)
      # Any code you write here will run before the form opens.
    self.content_panel.add_component(part_panel)
  
  
      # Any code you write here will run before the form opens.
