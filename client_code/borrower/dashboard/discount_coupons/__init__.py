from ._anvil_designer import discount_couponsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class discount_coupons(discount_couponsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def home_borrower_registration_form_copy_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('borrower.dashboard')

 
