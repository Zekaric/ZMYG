###############################################################################
# file:       MygCommand
# author:     Robbert de Groot
# company:    Zekaric
# copyright:  2022, Zekaric
#
# description:
# Web site commands.
#
# t             - toggle the task type for the current day.
###############################################################################
"""Command processing routines"""

###############################################################################
# imports:
###############################################################################
#import MygTask
import MygTaskList

###############################################################################
# local
# constants
###############################################################################
class COMMAND:
   """Constants"""
   VALUE : str = 'val'

###############################################################################
# global
# function
###############################################################################
###############################################################################
# process the command.
###############################################################################
def Process(param : dict[str, list[str]]) -> bool:
   """Process the command"""

   value = ""

   # For local debugging purposes.
   if (COMMAND.VALUE in param):
      value = param[COMMAND.VALUE][0]

   return _Process(value)

###############################################################################
# local
# function
###############################################################################
###############################################################################
# Process the command string.
###############################################################################
def _Process(value: str) -> bool:

   task = MygTaskList.GetAt(0)

   task.SetType(value)

   MygTaskList.FileStore()

   # Unknown command
   return False
