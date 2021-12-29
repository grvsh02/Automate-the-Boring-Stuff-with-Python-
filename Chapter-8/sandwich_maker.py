import pyinputplus as pyip

bread = pyip.inputMenu(["wheat", "White", "sourdough"],
                       "please select bread: ")
protein = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"],
                         "please select protien type: ")
if pyip.inputYesNo("Do you prefer cheeze (yes/no) ?") == "yes":
    cheese = pyip.inputMenu(["cheddar", "Swiss", "mozzarella"],
                            "please select a cheese: ")
count = pyip.inputInt("please enter the quantity required: ", min=1)