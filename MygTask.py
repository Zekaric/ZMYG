###############################################################################
# file:       MygTask
# author:     Robbert de Groot
# company:    Zekaric
# copyright:  2022, Zekaric
#
# description:
# Item handling
###############################################################################
"""Task record routines"""

###############################################################################
# import
###############################################################################
import datetime

###############################################################################
# global
# class
###############################################################################
###############################################################################
# Task Class
###############################################################################
class MygTask:
   """Task record"""

   def __init__(self):
      self._date:       str         = datetime.date.today().isoformat()
      self._typeList:   list[str]   = []

   def __str__(self) -> str:
      value = self._date
      for part in self._typeList:
         value += "\t" + part
      value += "\n"
      return value

   def GetDate(self) -> str:
      """Get the date for the task record."""
      return self._date

   def GetTypeAt(self, index: int) -> str:
      """Get the type list of the task record"""
      return self._typeList[index]

   def GetTypeCount(self) -> int:
      """Get the number of types in the task"""
      return len(self._typeList)

   def SetDate(self, value: str):
      """Set the date for the task record"""
      self._date = value

   def SetType(self, value: str):
      """Toggle a type value"""

      # if not in the list, add it.
      if (value not in self._typeList):
         self._typeList.append(value)
         self._typeList.sort()
      # if in the list
      else:
         self._typeList.remove(value)

###############################################################################
# global
# function
###############################################################################
###############################################################################
# Create a task from values
###############################################################################
def Create() -> MygTask:
   """Create a blank task record."""
   return MygTask()

###############################################################################
# Create a Task from a string definition
###############################################################################
def CreateFromStr(line: str) -> MygTask | None:
   """Create a task record from string."""

   # Split the line.
   partList = line.split('\t')

   # Create a new item.
   result = Create()
   for index, part in enumerate(partList):
      if (index == 0):
         if (part == ''):
            return None
         result.SetDate(part)
      else:
         result.SetType(part)

   return result
