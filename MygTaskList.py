###############################################################################
# file:       MygTaskList
# author:     Robbert de Groot
# company:    Zekaric
# copyright:  2022, Zekaric
#
# description:
# Task list handling
###############################################################################
"""Task list routines"""

###############################################################################
# import
###############################################################################
from io import TextIOWrapper
import os
import datetime
import calendar

import MygTask

###############################################################################
# local
# constant
###############################################################################
class MYG_TASKLIST:
   """Task record constant"""
   FILE: str = 'myg.dat'

###############################################################################
# variable
###############################################################################
class MygTaskList:
   """Task rescord class"""
   _list: list[MygTask.MygTask] = []

   @classmethod
   def GetAt(cls, index: int) -> MygTask.MygTask:
      """Get a task record at a specific index"""
      return cls._list[index]

   @classmethod
   def GetCount(cls) -> int:
      """Get the number of task records"""
      return 366

   @classmethod
   def FileLoad(cls) -> bool:
      """Load the task record"""
      # No project list yet.
      if (not os.path.exists(MYG_TASKLIST.FILE)):
         return False

      # Read in the file.
      file: TextIOWrapper
      try:
         file = open(MYG_TASKLIST.FILE, 'r', encoding='utf-8')
      except OSError:
         return False

      fileContent = file.read()
      file.close()

      # For all lines in the file.
      lines       = fileContent.split('\n')
      fileContent = None
      for index in range(366):

         # Get the tasks of the day.
         task = MygTaskList.GetAt(index)

         # Set the task to what was stored.
         task.SetFromStr(lines[index])

      return True

   @classmethod
   def FileStore(cls) -> bool:

      # Open the file for writing
      file = None
      try:
         file = open(MYG_TASKLIST.FILE, 'w', encoding='utf-8')
      except OSError:
         return False

      # For all tasks...
      for task in cls._list:

         # Write the project information.
         file.write(str(task))

      # clean up
      file.close()

      return True

   @classmethod
   def Start(cls) -> bool:
      """Fill the list for the entire year with unset task values."""
      cls._list.clear()

      # For all the days in the year.
      for dayIndex in range(366):
         # Create the empty task
         task = MygTask.Create()

         cls._list.append(task)

      MygTaskList.FileLoad()

      return True

###############################################################################
# global
# function
###############################################################################
###############################################################################
# Save the items
###############################################################################
def Store() -> bool:
   """Store the task records"""
   return MygTaskList.FileStore()

###############################################################################
# Get the n'th task
###############################################################################
def GetAt(index: int) -> MygTask.MygTask:
   """Get a task record"""
   return MygTaskList.GetAt(index)

###############################################################################
# Start
###############################################################################
def Start() -> bool:
   """Program start"""
   MygTaskList.Start()

   todayMonth = datetime.date.today().month
   todayDay   = datetime.date.today().day

   # Reset the leap day.
   if todayMonth == 2 and todayDay > 22:
      task = MygTaskList.GetAt(365)
      task.ResetFlag()

   # Get today's year day number.
   todayYDay = datetime.date.today().timetuple().tm_yday - 1
   if calendar.isleap(datetime.date.today().year):
      todayYDay -= 1

   # wipe the next 7 days of the year.
   todayYDay = (todayYDay + 1) % 365;
   task = MygTaskList.GetAt(todayYDay)
   task.ResetFlag()
   todayYDay = (todayYDay + 1) % 365;
   task = MygTaskList.GetAt(todayYDay)
   task.ResetFlag()
   todayYDay = (todayYDay + 1) % 365;
   task = MygTaskList.GetAt(todayYDay)
   task.ResetFlag()
   todayYDay = (todayYDay + 1) % 365;
   task = MygTaskList.GetAt(todayYDay)
   task.ResetFlag()
   todayYDay = (todayYDay + 1) % 365;
   task = MygTaskList.GetAt(todayYDay)
   task.ResetFlag()
   todayYDay = (todayYDay + 1) % 365;
   task = MygTaskList.GetAt(todayYDay)
   task.ResetFlag()
   todayYDay = (todayYDay + 1) % 365;
   task = MygTaskList.GetAt(todayYDay)
   task.ResetFlag()

   MygTaskList.FileStore()

   return True