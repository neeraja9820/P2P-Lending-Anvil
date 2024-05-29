from ._anvil_designer import lender_registration_Institutional_form_2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timedelta, date

class lender_registration_Institutional_form_2(lender_registration_Institutional_form_2Template):
  def init(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user_data = anvil.server.call('get_user_data', user_id)
        
    if user_data:
            self.industry_type = user_data.get('industry_type', '')
            self.turn_over = user_data.get('six_month_turnover', '')
            self.last_six_statements = user_data.get('last_six_month_bank_proof')
            self.year = user_data.get('year_estd', '')
           
    
    else:
        self.industry_type = ''
        self.turn_over = ''
        self.year = ''

    # user_data=app_tables.fin_user_profile.get(customer_id=user_id)
    # if user_data:
    #   self.date_picker_1.date = user_data['year_estd']
    #   self.text_box_1.text=user_data['industry_type']
    #   self.text_box_2.text=user_data['six_month_turnover']
    #   # self.file_loader_1.file = user_data['last_six_month_bank_proof']
       #Restore previously entered data if available
    if self.industry_type:
            self.text_box_1.text= self.industry_type
    if self.turn_over:
            self.text_box_2.text= self.turn_over

    if self.year:
           self.date_picker_1.date = self.year

    if self.last_six_statements:
        self.file_loader_1.file = self.last_six_statements
    
    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    industry_type = self.text_box_1.text
    turn_over = self.text_box_2.text
    year = self.date_picker_1.date
    last_six_statements = self.file_loader_1.file
    user_id = self.userId
    
    # Get today's date
    today = date.today()
    
    # Check if the selected date is in the future
    if year and year.year > today.year:
      alert("The year cannot be in the future. Please select a valid year.", title="Invalid Year")
      return
    elif year and year.year == today.year and year.month > today.month:
      alert("The month cannot be in the future. Please select a valid month.", title="Invalid Month")
      return
    elif year and year.year == today.year and year.month == today.month and year.day > today.day:
      alert("The date cannot be in the future. Please select a valid date.", title="Invalid Date")
      return

    if not year or not industry_type or not turn_over or not last_six_statements:
      Notification("Please fill all the fields").show()
    else:
     months = (datetime.now().year - year.year) * 12 + (datetime.now().month - year.month)
     anvil.server.call('add_lendor_institutional_form_2',year,months,industry_type,turn_over,last_six_statements,user_id)
     open_form('lendor.lendor_registration_forms.lender_registration_form_2.lender_registration_Institutional_form_3',user_id = user_id)
     """This method is called when the button is clicked"""

  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor.lendor_registration_forms.lender_registration_form_2.lender_registration_Institutional_form_1',user_id = user_id)
    """This method is called when the button is clicked"""

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.user_form")

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if file:
      self.image_1.source = self.file_loader_1.file

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    selected_date = self.date_picker_1.date
    today = date.today()
    two_days_before = today - timedelta(days=2)
    
    if selected_date and selected_date <= two_days_before:
      Notification("The selected date is within two days before today. Please choose a valid date.").show()
    elif selected_date and selected_date.year > today.year:
      alert("The year cannot be in the future. Please select a valid year.", title="Invalid Year")
    elif selected_date and selected_date.year == today.year and selected_date.month > today.month:
      alert("The month cannot be in the future. Please select a valid month.", title="Invalid Month")
    elif selected_date and selected_date.year == today.year and selected_date.month == today.month and selected_date.day > today.day:
      alert("The date cannot be in the future. Please select a valid date.", title="Invalid Date")