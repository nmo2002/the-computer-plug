from ._anvil_designer import BaseTemplate
from anvil import *

class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_1.text = "Hello World"

    # Any code you write here will run before the form opens.
