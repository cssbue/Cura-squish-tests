# -*- coding: utf-8 -*-
from PageObjects.CommonPage import PageObject
from Helpers.GetObjectsByProperties import ObjectDescendants
from Helpers.SquishModuleHelper import importSquishSymbols
import names


class Preferences(PageObject):
    def __init__(self):
        PageObject.__init__(self)
        importSquishSymbols()

    def navigateTo(self, menu_item):
        menu_object = self.findObjectByText(names.mnu_item_preferences, menu_item)
        self.click(menu_object)

    def selectPrinterMenu(self, action):
        button = self.replaceObjectProperty(names.pps_mnu_btn, self.getMenuBtn(action), 'id')
        self.click(button)
        
    def getMenuBtn(self, menu_action):
        switcher = {
            'Add': 'activateMenuButton',
            'Activate': 'addMenuButton',
            'Remove': 'removeMenuButton',
            'Rename': 'renameMenuButton'
        }

        return switcher.get(menu_action)

    def removePrinter(self):
        self.click(names.rpd_btn_confirm)

    def verifyPrinterDeleted(self, printer):
        obj = self.replaceObjectProperty(names.pps_printer_item, printer)
        return self.verifyObjDeleted(obj)

    def getPrinterListSize(self):
        # This list contains non-printer objects, such as 'Local printers' and 'Network printers'
        # As they are the same object type
        printer_list = len(ObjectDescendants.getObjects(names.pps_printer_list, {"type": "QQuickRectangle"}))

        # Check if 'Local/Network printers' exists, if so extract one item from the printer list
        if object.exists(self.getObjByLang(names.pps_local_printers)):
            printer_list -= 1
        if object.exists(self.getObjByLang(names.pps_network_printers)):
            printer_list -= 1

        return printer_list

    def getPrinterFromList(self, property_value):
        printer = ObjectDescendants.getObjects(names.pps_printer_list, {"text": f"{property_value}"})
        return printer

    def selectPrinter(self, printer_type):
        printer_list = self.getPrinterList(printer_type)

        if len(printer_list) != 0:
            self.click(printer_list[0])
        else:
            test.fail("Printer %s not found" % printer_type)

    def renamePrinter(self, printer_name):
        self.click(names.input_printer_name)
        self.setTextFieldValue(names.input_printer_name, printer_name)
        self.click(names.btn_rename_confirm)

    def verifyPrinterActivated(self):
        object.exists(names.pps_btn_machine_settings)
