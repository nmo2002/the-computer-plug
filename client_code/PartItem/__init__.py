from ._anvil_designer import PartItemTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class PartItem(PartItemTemplate):
  def __init__(self, name, description, button_text, image, button_callback, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name_label.content = name
    self.description_label.content = description
    self.button.text = button_text
    self.image_content.source = image

    # Any code you write here will run before the form opens.

  def button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

