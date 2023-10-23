"""
Copyright (c) 2023 Himank Deka & Contributers [See CONTRIBUTERS.txt]
"""
"""
This file contains the exceptions that will be shown if there is error in the code.
"""

class ExitNotSetError(Exception) :
    def __str__() :
        return "Exit is set to true but exit is not created"
    
class NotUpgradableError(Exception) :
    def __str__() :
        return "The item you are trying to upgrade in non-upgradable"

