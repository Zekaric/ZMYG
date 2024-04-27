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
import MygTypeList

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
      self._flagList:   list[bool]   = [False] * MygTypeList.GetCount()

   def __str__(self) -> str:
      value = ""

      for part in self._flagList:
         if part:
            value += "X"
         else:
            value += "-"

      value += "\n"

      return value

   def GetFlag(self, index: int) -> bool:
      """Get the type list of the task record"""
      return self._flagList[index]

   def ResetFlag(self):
      self._flagList = [False] * MygTypeList.GetCount()

   def Setflag(self, index: int, flag: bool):
      """Set the type flag"""
      self._flagList[index] = flag

   def SetFromStr(self, line: str):
      for index in range(MygTypeList.GetCount()):
         self._flagList[index] = False
         if line[index] == "X":
            self._flagList[index] = True

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
