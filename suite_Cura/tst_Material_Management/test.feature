Feature: Material manager


  Scenario: Create material
    Given Cura has been started with preset configurations
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Materials in preferences
    And I select Create material
    Then the material 'Custom Custom Material' has been added
    And I close the preferences
    Then Extruder one makes use of material 'Custom Custom Material'

  Scenario: Duplicate material
    Given Cura is running
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Materials in preferences
    And I select Duplicate material
    Then the material 'Custom Custom Material' has been added
    Then I select 'Unlink Material' in material manager
    And I change the material name to 'Baby'
    And I close the preferences

  Scenario: Remove material
    Given Cura is running
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Materials in preferences
    And I select 'Custom Custom Material' material in preferences
    And I select Remove material
    And I confirm the removal
    Then the material 'Custom Custom Material' has not been added
    And I close the preferences

  Scenario: Adjust material diameter
    Given Cura is running
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Materials in preferences
    And I select Create material
    Then the material 'Custom Custom Material' has been added
    When I change the material name to 'Diameter Test'
    Then the material 'Custom Diameter Test' has been added
    And the material property 'Diameter' is '2.85 mm'
    When I change the material property 'Diameter' to '3.25'
    Then the material 'Custom Diameter Test' has been added
    And the material property 'Diameter' is '3.25 mm'
    When I change the material property 'Diameter' to '1.75'
    And I deny changing the diameter
    Then the material 'Custom Diameter Test' has been added
    And the material property 'Diameter' is '3.25 mm'
    When I change the material property 'Diameter' to '1.75'
    And I confirm changing the diameter
    Then the material 'Custom Diameter Test' has not been added
    And the material property 'Diameter' is '2.85 mm'
    And the material 'PLA' is selected
    And I close the preferences

  Scenario: Material diameter after restarting
    Given Cura is running
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Materials in preferences
    And I select Create material
    Then the material 'Custom Custom Material' has been added
    When I change the material name to 'Diameter Restart'
    Then the material 'Diameter Restart' has been added
    And the material property 'Diameter' is '2.85 mm'
    When I change the material property 'Diameter' to '3.33'
    Then the material 'Diameter Restart' has been added
    And the material property 'Diameter' is '3.33 mm'
    When I close the preferences
    And I restart Cura
    And I navigate to menu Preferences and Configure Cura
    And I navigate to Materials in preferences
    Then the material 'Diameter Restart' has been added
    And the material property 'Diameter' is '3.33 mm'
    And I close the preferences

  Scenario: Export material
    Given Cura has been started
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Materials in preferences
    And I select Duplicate material
    And I change the material name to 'Export'
    Then I select 'Print settings' tab
    And I change the material print settings properties
      | setting                         | value |
      | Default Printing Temperature    | 220   |
      | Default Build Plate Temperature | 65    |
      | Retraction Distance             | 8     |
      | Retraction Speed                | 30    |
      | Standby Temperature             | 190   |
      | Fan Speed                       | 75    |
    Then I select Export material
    And I save the file as 'materialExport'
    Then the file 'materialExport' is a valid 'material'
    And I close the preferences

  Scenario: Import material
    Given Cura is running
    When I navigate to menu Preferences and Configure Cura
    And I navigate to Materials in preferences
    And I select 'Generic PLA' material in preferences
    And I select Activate material
    Then I select 'Generic Export' material in preferences
    And I select Remove material
    Then I select Import material
    And I choose to load 'materialExport'
    Then the material 'Generic Export' has been added











