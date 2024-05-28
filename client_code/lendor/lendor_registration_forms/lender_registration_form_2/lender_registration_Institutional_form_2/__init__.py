from ._anvil_designer import lender_registration_Institutional_form_2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime

# Define a function to retrieve the user ID
def get_user_id_somehow():
    # Replace this with your actual logic to retrieve the user ID
    return "12345"  # For example, return a hardcoded user ID or retrieve it from session data

class lender_registration_Institutional_form_2(lender_registration_Institutional_form_2Template):
    def __init__(self, user_id, **properties):
        super().__init__(**properties)
        self.userId = user_id
        user_data = anvil.server.call('get_user_data', user_id)
        if user_data:
            self.industry_type = user_data.get('industry_type', '')
            self.turn_over = user_data.get('six_month_turnover', '')
            self.last_six_statements = user_data.get('last_six_month_bank_proof')
            self.year = user_data.get('year_estd', '')
            if self.industry_type:
                self.text_box_1.text = self.industry_type
            if self.turn_over:
                self.text_box_2.text = self.turn_over
            if self.year:
                self.date_picker_1.date = self.year
            if self.last_six_statements:
                self.file_loader_1.file = self.last_six_statements

    def button_2_click(self, **event_args):
        try:
            industry_type = self.text_box_1.text
            turn_over = self.text_box_2.text
            year = self.date_picker_1.date
            last_six_statements = self.file_loader_1.file
            user_id = self.userId
            if not year or not industry_type or not turn_over or not last_six_statements:
                Notification("Please fill all the fields").show()
            else:
                today = datetime.today()
                months = today.year * 12 + today.month - year.year * 12 - year.month
                anvil.server.call('add_lendor_institutional_form_2', year, months, industry_type, turn_over, last_six_statements, user_id)
                open_form('lendor.lendor_registration_forms.lender_registration_form_2.lender_registration_Institutional_form_3', user_id=user_id)
        except Exception as e:
            Notification("An error occurred: {}".format(str(e))).show()

    def button_1_click(self, **event_args):
        user_id = self.userId
        open_form('lendor.lendor_registration_forms.lender_registration_form_2.lender_registration_Institutional_form_1', user_id=user_id)

    def button_3_click(self, **event_args):
        open_form("bank_users.user_form")

    def file_loader_1_change(self, file, **event_args):
        if file:
            self.image_1.source = self.file_loader_1.file

    def date_picker_1_change(self, **event_args):
        self.date_picker_1.date = datetime.now().date()

# Example usage:
user_id = get_user_id_somehow()  
form = lender_registration_Institutional_form_2(user_id)
form.show()
