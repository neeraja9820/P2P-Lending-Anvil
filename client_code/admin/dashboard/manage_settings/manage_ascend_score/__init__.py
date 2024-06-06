from ._anvil_designer import manage_ascend_scoreTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class manage_ascend_score(manage_ascend_scoreTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Initially, check if there is any existing Ascen score data
    self.check_existing_ascend_score_data()

  def check_existing_ascend_score_data(self):
    # Define Ascend score types
    ascend_category = ['VeryGood', 'Good', 'Average', 'Bad']

    for ascend_category in ascend_category:
        row = app_tables.fin_admin_ascend_score.get(ascend_category=ascend_category)

        if row is None:
            self.enable_text_boxes(ascend_category)
            self.disable_edit_button(ascend_category)
        else:
            self.populate_text_boxes(row, ascend_category)
            self.disable_text_boxes(ascend_category)
            self.enable_edit_button(ascend_category)
            self.disable_save_button(ascend_category)


  def populate_text_boxes(self, row, ascend_category):
    # Populate textboxes with existing data
    if ascend_category == 'VeryGood':
      self.text_box_1.text = row['max_ascend_score_range']
      self.text_box_2.text = row['min_ascend_score_range']
      self.text_box_3.text = row['colour']
    elif ascend_category == 'Good':
      self.text_box_4.text = row['max_ascend_score_range']
      self.text_box_5.text = row['min_ascend_score_range']
      self.text_box_6.text = row['colour']
    elif ascend_category == 'Average':
      self.text_box_7.text = row['max_ascend_score_range']
      self.text_box_8.text = row['min_ascend_score_range']
      self.text_box_9.text = row['colour']
    elif ascend_category == 'Bad':
      self.text_box_10.text = row['max_ascend_score_range']
      self.text_box_11.text = row['min_ascend_score_range']
      self.text_box_12.text = row['colour']  

  def enable_text_boxes(self, ascend_category):
    # Enable textboxes for the specified ascend_category 
    #if ascend_category == 'VeryGood':
      self.text_box_1.enabled = True
      self.text_box_2.enabled = True
      self.text_box_3.enabled = True
    #elif ascend_category == 'Good':
      self.text_box_4.enabled = True
      self.text_box_5.enabled = True
      self.text_box_6.enabled = True
    #elif ascend_category == 'Average':
      self.text_box_7.enabled = True
      self.text_box_8.enabled = True
      self.text_box_9.enabled = True
    #elif ascend_category == 'Bad':
      self.text_box_10.enabled = True
      self.text_box_11.enabled = True
      self.text_box_12.enabled = True

  def disable_text_boxes(self, ascend_category):
    # Disable textboxes for the specified ascend_category
    #if ascend_category == 'VeryGood':
      self.text_box_1.enabled = False
      self.text_box_2.enabled = False
      self.text_box_3.enabled = False
    #elif ascend_category == 'Good':
      self.text_box_4.enabled = False
      self.text_box_5.enabled = False
      self.text_box_6.enabled = False
    #elif ascend_category == 'Average':
      self.text_box_7.enabled = False
      self.text_box_8.enabled = False
      self.text_box_9.enabled = False
    #elif ascend_category == 'Bad':
      self.text_box_10.enabled = False
      self.text_box_11.enabled = False
      self.text_box_12.enabled = False

  def enable_edit_button(self, ascend_category):
    # Enable the corresponding edit button
    if ascend_category == 'VeryGood':
      self.button_1.visible = True
    elif ascend_category == 'Good':
      self.button_1.visible = True
    elif ascend_category == 'Average':
      self.button_1.visible = True
    elif ascend_category == 'Bad':
      self.button_1.visible = True  

  def disable_edit_button(self, ascend_category):
    # Disable the corresponding edit button
    if ascend_category == 'VeryGood':
      self.button_1.visible = False
    elif ascend_category == 'Good':
      self.button_1.visible = False
    elif ascend_category == 'Average':
      self.button_1.visible = False
    elif ascend_category == 'Bad':
      self.button_1.visible = False  
      
  def enable_save_button(self, ascend_category):
    # Enable the corresponding edit button
    if ascend_category == 'VeryGood':
      self.button_2.visible = True
    elif ascend_category == 'Good':
      self.button_2.visible = True
    elif ascend_category == 'Average':
      self.button_2.visible = True
    elif ascend_category == 'Bad':
      self.button_2.visible = False  

  def disable_save_button(self, ascend_category):
    # Disable the corresponding edit button
    if ascend_category == 'VeryGood':
      self.button_2.visible = False
    elif ascend_category == 'Good':
      self.button_2.visible = False
    elif ascend_category == 'Average':
      self.button_2.visible = False
    elif ascend_category == 'Bad':
      self.button_2.visible = False  
  

  def save_ascend_score(self, ascend_category):
    print("Saving ascend_score for:", ascend_category)
    # Determine which textboxes to read based on ascend catagory
    if ascend_category == 'VeryGood':
        max_ascend_score_range = int(self.text_box_1.text)
        min_ascend_score_range = int(self.text_box_2.text)
        if min_ascend_score_range <= 0:
            alert("VeryGood Min ascend score must be greater than zero!", title="Error")
            return
        if min_ascend_score_range >= max_ascend_score_range:
            alert("VeryGood Min ascend score must be less than VeryGood Max ascend score!", title="Error")
            return
        # Check if VeryGood max_ascend_score_range exceeds Good max ascend score range
        good_max_ascend_score_range = int(self.text_box_6.text)
        if max_ascend_score_range >= good_max_ascend_score_range:
            alert("VeryGood max_ascend_score_range exceed Good max_ascend_score_range or same!", title="Warning")
            return
        
        
    elif ascend_category == 'Good':
        min_ascend_score_range = int(self.text_box_4.text)
        max_ascend_score_range = int(self.text_box_5.text)
        if min_ascend_score_range <= 0:
            alert("Good Minimum ascend score can't be set as zero, it should be greater than VeryGood max_ascend_score and less than Good max_ascend_score!", title="Error")
            return
        if min_ascend_score_range >= max_amount:
            alert("Gold Minimum amount must be less than Gold maximum amount!", title="Error")
            return
        silver_max = int(self.text_box_2.text)
        if min_ascend_score_range <= silver_max:
            alert("Gold's min_amount must be greater than Silver's max_amount!", title="Error")
            return
        # Check if Gold's max_amount exceeds Platinum's max_amount
        platinum_max = int(self.text_box_6.text)
        if max_amount >= platinum_max:
            alert("Gold's max_amount cannot exceed Platinum's max_amount or same!", title="Warning")
            return
        
    elif ascend_category == 'Platinum':
        min_ascend_score_range = int(self.text_box_5.text)
        max_amount = int(self.text_box_6.text)
        if  >= max_amount:
            alert("Platinum Minimum amount must be less than Platinum maximum amount!", title="Error")
            return
        if min_amount <= 0:
            alert("Platinum Minimum amount can't be set as zero, it should be greater than Gold max-amount and less than platinum max_amount!", title="Error")
            return
        gold_max = int(self.text_box_4.text)
        if min_amount <= gold_max:
            alert("platinum's min_amount must be greater than Gold's max_amount!", title="Error")
            return
      
    print("Min Amount:", min_amount)
    print("Max Amount:", max_amount)

    # Check if a row already exists for this membership type
    existing_row = app_tables.fin_membership.get(ascend_category=ascend_category)
    if existing_row is not None:
        # Update the existing row with the provided min_amount and max_amount
        existing_row.update(min_amount=min_amount, max_amount=max_amount)
    else:
        # If the row doesn't exist, create a new row with the provided min_amount and max_amount
        app_tables.fin_membership.add_row(ascend_category=ascend_category, min_amount=min_amount, max_amount=max_amount)
      
    if ascend_category == 'Silver':
        min_amount = int(self.text_box_1.text)
        max_amount = int(self.text_box_2.text)
        silver_row = app_tables.fin_membership.get(ascend_category='Silver')
        if min_amount >= max_amount:
            alert("Minimum amount must be less than maximum amount!", title="Error")
            return
        # Check if Silver's max_amount exceeds Gold's min_amount
        gold_row = app_tables.fin_membership.get(ascend_category='Gold')
        if gold_row is not None and gold_row['min_amount'] is not None and max_amount >= gold_row['min_amount']:
            print("silver max", max_amount)
            # gold_row['min_amount'] =  max_amount + 1
            self.text_box_3.text = max_amount + 1  
            alert("Silver's max_amount cannot exceed Gold's min_amount! Adjusting max_amount.", title="Warning")
       
    elif ascend_category == 'Gold':
        min_amount = int(self.text_box_3.text)
        max_amount = int(self.text_box_4.text)
        if min_amount >= max_amount:
            alert("Minimum amount must be less than maximum amount!", title="Error")
            return
        # Check if Gold's max_amount exceeds Platinum's min_amount
        platinum_row = app_tables.fin_membership.get(ascend_category='Platinum')
        if platinum_row is not None and platinum_row['min_amount'] is not None and max_amount >= platinum_row['min_amount']:
            self.text_box_5.text =  max_amount + 1
            alert("Gold's max_amount cannot exceed Platinum's min_amount! Adjusting max_amount.", title="Warning")
        
    elif ascend_category == 'Platinum':
        min_amount = int(self.text_box_5.text)
        max_amount = int(self.text_box_6.text)
        if min_amount >= max_amount:
            alert("Minimum amount must be less than maximum amount!", title="Error")
            return
        # Ensure that Platinum's min_amount is greater than Gold's max_amount
        gold_row = app_tables.fin_membership.get(ascend_category='Gold')
        if gold_row is not None and gold_row['max_amount'] is not None and min_amount <= gold_row['max_amount']:
            min_amount = gold_row['max_amount'] + 1
            alert("Platinum's min_amount cannot be less than or equal to Gold's max_amount! Adjusting min_amount.", title="Warning")

    print("Max Ascend score range:", max_ascend_score_range)
    print("Min Ascend score range:", min_ascend_score_range)
    open_form('admin.dashboard.manage_settings.manage_ascend_score')

    # Re-enable edit and save buttons
    self.disable_save_button(ascend_category)
    self.enable_edit_button(ascend_category)
    self.disable_text_boxes(ascend_category)

  def edit_ascend_score(self, ascend_category):
    print("Editing ascend_score for:", ascend_category)
    # Enable editing for the corresponding ascend_category
    self.enable_text_boxes(ascend_category)
    # Disable the edit button
    self.disable_edit_button(ascend_category)
    self.enable_save_button(ascend_category)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.home_button_admin_1.visible = False
    for ascend_category in ['VeryGood', 'Good', 'Average','Bad']:
        self.edit_ascend_score(ascend_category)       

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    for ascend_category in ['VeryGood', 'Good', 'Average', 'Bad']:
        self.save_ascend_score(ascend_category)
    open_form('admin.dashboard.manage_settings.manage_ascend_score')

