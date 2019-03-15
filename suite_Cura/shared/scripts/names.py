# encoding: UTF-8
from objectmaphelper import *

# Main window
mainWindow = {"title": "Ultimaker Cura", "type": "MainWindow", "unnamed": 1, "visible": True}
mainWindowOverlay = {"container": mainWindow, "type": "Overlay", "unnamed": 1, "visible": True}

# Cura Menu
mainWindowPrinter = {"container": mainWindow, "id": "machineSelection", "type": "MachineSelector", "unnamed": 1, "visible": True}
mainWindowSelectedPrinter = {"container": mainWindowPrinter, "type": "Label", "unnamed": 1, "visible": True}
mainWindowOpenFile = {"checkable": False, "container": mainWindow, "id": "openFileButton", "type": "Button", "unnamed": 1, "visible": True}
mainWindowPrinterList = {"container": mainWindowOverlay, "id": "machineSelectorList", "type": "MachineSelectorList", "unnamed": 1, "visible": True}
mainWindowPrintSettings = {"container": mainWindow, "id": "printSetupSelectorItem", "type": "Item", "unnamed": 1, "visible": True}
mainWindowPrinterListItem = {"checkable": True, "container": mainWindowOverlay, "text": "", "type": "MachineSelectorButton", "unnamed": 1, "visible": True}

# File Dialog
fileDialog = {"name": "QFileDialog", "type": "QFileDialog", "visible": 1}
fileNameLabel = {"name": "fileNameLabel", "type": "QLabel", "visible": 1, "window": fileDialog}
fileNameInput = {"buddy": fileNameLabel, "name": "fileNameEdit", "type": "QLineEdit", "visible": 1}
openFile = {"text": "Open", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": fileDialog}
saveFile = {"text": "Save", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": fileDialog}
fileType = {"name": "fileTypeCombo", "type": "QComboBox", "visible": 1, "window": fileDialog}

fileAlreadyExistsDialog = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "File Already Exists"}
overwriteFile = {"text": "Yes", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": fileAlreadyExistsDialog}

# Menu (top-level)
menuBar = {"container": mainWindow, "id": "menuBarLoader", "type": "Loader", "unnamed": 1, "visible": True}
menuItem = {"container": menuBar, "plainText": "", "type": "StyleItem1", "unnamed": 1, "visible": True}

o_QQuickMenuPopupWindow = {"type": "QQuickMenuPopupWindow1", "unnamed": 1, "visible": True}
scrollView = {"container": o_QQuickMenuPopupWindow, "id": "scrollView", "type": "ScrollView", "unnamed": 1, "visible": True}

configureCura = {"container": scrollView, "text": Wildcard("Configure Cura*"), "type": "StyleItem1", "unnamed": 1, "visible": True}
clearBuildplate = {"container": scrollView, "text": "Clear Build Plate", "type": "StyleItem1", "unnamed": 1, "visible": True}

# Changelog
changelogWindow = {"title": "Changelog", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
changelogClose = {"container": changelogWindow, "text": "Close", "type": "Button", "unnamed": 1, "visible": True}

# Agreement
agreementDialog = {"title": "User Agreement", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
agreementButton = {"container": agreementDialog, "text": "I understand and agree", "type": "Button", "unnamed": 1, "visible": True}

# Printer dialog
addPrinterDialog = {"title": "Add Printer", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
addPrinter = {"container": addPrinterDialog, "id": "addPrinterButton", "text": "Add Printer", "type": "Button", "unnamed": 1, "visible": True}
addPrinterFinish = {"container": addPrinterDialog, "id": "nextButton", "text": "Finish", "type": "Button", "unnamed": 1, "visible": True}

printerView = {"container": addPrinterDialog, "id": "machinesHolder", "type": "ScrollView", "unnamed": 1, "visible": True}
printerList = {"container": printerView, "id": "machineList", "type": "ListView", "unnamed": 1, "visible": True}
selectedPrinter = {"container": printerList, "id": "machineButton", "text": "", "type": "AbstractCheckable", "unnamed": 1, "visible": True}

# Printer dialog - network
addNetworkPrinter = {"container": addPrinterDialog, "id": "addButton", "text": "Add", "type": "Button", "unnamed": 1, "visible": True}
printerAddressDialogue = {"title": "Printer Address", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
printerAddressInputField = {"container": printerAddressDialogue, "id": "addressField", "type": "TextField", "unnamed": 1, "visible": True}
printerAddressOKButton = {"container": printerAddressDialogue, "id": "btnOk", "text": "OK", "type": "Button", "unnamed": 1, "visible": True}
connectNetworkPrinter = {"container": addPrinterDialog, "text": "Connect", "type": "Button", "unnamed": 1, "visible": True}

# Preferences
preferenceWindow = {"title": "Preferences", "type": "QQuickWindowQmlImpl", "unnamed": 1, "visible": True}
preferencesMenu = {"container": preferenceWindow, "id": "pagesList", "type": "TableView", "unnamed": 1, "visible": True}
preferencesMenuItem = {"container": preferencesMenu, "objectName": "label", "text": "", "type": "Text", "visible": True}

# Printer preferences
preferencesMenuButton = {"container": preferenceWindow, "text": "", "type": "Button", "unnamed": 1, "visible": True}
printerListView = {"container": preferenceWindow, "id": "objectList", "type": "ListView", "unnamed": 1, "visible": True}
printerListItem = {"container": printerListView, "text": Wildcard("*"), "type": "Text", "unnamed": 1, "visible": True}

# Slice & Save
sliceButton = {"checkable": False, "container": mainWindow, "id": "sliceButton", "text": "Slice", "type": "ActionButton", "unnamed": 1, "visible": True}
saveToFileButton = {"checkable": False, "container": mainWindow, "id": "saveToButton", "text": "Save to File", "type": "ActionButton", "unnamed": 1, "visible": True}
previewButton = {"checkable": False, "container": mainWindow, "id": "previewStageShortcut", "text": "Preview", "type": "ActionButton", "unnamed": 1, "visible": True}

# Print Settings
printSettingsCustomButton = {"checkable": False, "container": mainWindow, "text": "Custom", "type": "ActionButton", "unnamed": 1, "visible": True}
customPrintSettingsView = {"container": mainWindow, "id": "customPrintSetup", "type": "CustomPrintSetup", "unnamed": 1, "visible": True}
printSettingsProfileSelection = {"container": customPrintSettingsView, "id": "globalProfileSelection", "type": "Button", "unnamed": 1, "visible": True}
printSettingsFineProfile = {"container": scrollView, "text": "Fine - 0.1mm", "type": "StyleItem1", "unnamed": 1, "visible": True}

