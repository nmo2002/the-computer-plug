from ._anvil_designer import CheckoutTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import stripe

class Checkout(CheckoutTemplate):
  def __init__(self, id_name, back_button_callback, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.back_button_callback = back_button_callback
    self.update_form(id_name)

    # Any code you write here will run before the form opens.
  def update_form(self, id_name):
    part = anvil.server.call('get_part_details', id_name)
    self.part = part
    self.name_label.text = part['name']
    self.description_label.text = part['description']
    self.price_label.text = f'${part["price"]} USD'
    self.image_content.source = part['image']

  def buy_click(self, **event_args):
    """This method is called when the button is clicked"""
    if anvil.users.get_user() == None:
      anvil.users.login_with_form()

    user = anvil.users.get_user()
    if user == None:
      alert("Please sign in!")
      return

    if user['purchased_parts'] and self.part['name'] in user['purchase_parts']:
      alert("You already own this part!")
    try:
      token, info = stripe.checkout.get_token(amount=self.part['price'], currency="USD", title=self.part['name'], description=self.part['description'])
      anvil.server.call('charge_user', token, user['email'], self.course['name'])
      alert('Success')
    except:
      alert('Something went wrong!')
    
      
  def back_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.back_button_callback()
