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

    # Any code you write here will run before the form opens.
    # Initially, check if there is any existing ascend category
    self.check_existing_ascend_category()

  def check_existing_ascend_category(self):
    # Define ascend_categorys
    ascend_categorys = ['VeryGood', 'Good', 'Average', 'Bad']

    for ascend_category in ascend_categorys:
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
    # Enable textboxes for the specified membership type
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
    # Disable textboxes for the specified ascend category
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
      self.button_2.visible = True

  def disable_save_button(self, ascend_category):
    # Disable the corresponding edit button
    if ascend_category == 'VeryGood':
      self.button_2.visible = False
    elif ascend_category == 'Good':
      self.button_2.visible = False
    elif ascend_category == 'Bad':
      self.button_2.visible = False
    elif ascend_category == 'Bad':
      self.button_2.visible = False

  def edit_ascend_category(self, ascend_category):
    print("Editing membership for:", ascend_category)
    # Enable editing for the corresponding ascend_category
    self.enable_text_boxes(ascend_category)
    # Disable the edit button
    self.disable_edit_button(ascend_category)
    self.enable_save_button(ascend_category)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.home_button_admin_1.visible = False
    for ascend_category in ['VeryGood', 'Good', 'Average', 'Bad']:
        self.edit_ascend_score(ascend_category)       

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    for ascend_category in ['VeryGood', 'Good', 'Average', 'Bad']:
        self.save_ascend_score(ascend_category)
    open_form('admin.dashboard.manage_settings.manage_ascend_category')