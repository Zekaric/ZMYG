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
   DAY : str = 'day'
   TYPE: str = 'type'

###############################################################################
# global
# function
###############################################################################
###############################################################################
# process the command.
###############################################################################
def Process(param : dict[str, list[str]]) -> bool:
   """Process the command"""

   day  = ""
   type = ""

   # For local debugging purposes.
   if COMMAND.DAY  in param:
      day  = param[COMMAND.DAY][0]
   if COMMAND.TYPE in param:
      type = param[COMMAND.TYPE][0]

   return _Process(day, type)

###############################################################################
# local
# function
###############################################################################
###############################################################################
# Process the command string.
###############################################################################
def _Process(day: str, type: str) -> bool:

   dayIndex  = int(day);
   typeIndex = int(type);

   task = MygTaskList.GetAt(dayIndex)
   task.Setflag(typeIndex, not task.GetFlag(typeIndex))

   MygTaskList.Store()

   # Unknown command
   return False
