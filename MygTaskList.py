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
   def AddOrSet(cls, task: MygTask.MygTask) -> None:
      """Add or replace a task record"""
      if   (len(cls._list) == 0):
         cls._list.append(task)
      elif (task.GetDate() == cls._list[0].GetDate()):
         cls._list[0] = task
      else:
         cls._list.insert(0, task)

   @classmethod
   def GetAt(cls, index: int) -> MygTask.MygTask:
      """Get a task record at a specific index"""
      return cls._list[index]

   @classmethod
   def GetCount(cls) -> int:
      """Get the number of task records"""
      return len(cls._list)

   @classmethod
   def FileLoad(cls) -> bool:
      """Load the task order"""
      # No project list yet.
      if (not os.path.exists(MYG_TASKLIST.FILE)):
         return False

      # Clear anything that might currently exist
      cls._list = []

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
      for line in lines:

         # Create the task from the line
         task = MygTask.CreateFromStr(line)
         if (task is None):
            continue

         # Append the task to the list.
         cls._list.append(task)

      cls._list.reverse()

      return True

   @classmethod
   def FileStore(cls) -> bool:
      """Store the task records in chrono order"""
      cls._list.reverse()

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

      cls._list.reverse()

      return True

###############################################################################
# global
# function
###############################################################################
###############################################################################
# Add a new or set if already present.
###############################################################################
def AddOrSet(task: MygTask.MygTask) -> None:
   """Add a new task record"""
   MygTaskList.AddOrSet(task)

###############################################################################
# Load in the tasks
###############################################################################
def FileLoad() -> bool:
   """Load the task records"""
   return MygTaskList.FileLoad()

###############################################################################
# Save the items
###############################################################################
def FileStore() -> bool:
   """Store the task records"""
   return MygTaskList.FileStore()

###############################################################################
# Fill missing records
###############################################################################
def FillMissing():
   """Add missing value for days we missed."""

   # create a brand new task, always today's date.
   newTask = MygTask.Create()

   # first time run, empty task list.  Add today's task.
   if (MygTaskList.GetCount() == 0):
      MygTaskList.AddOrSet(newTask)
      MygTaskList.FileStore()
      return

   # get the last task in the list chronologically, top task.
   task    = MygTaskList.GetAt(0)

   # Check if they are the same...
   if (task.GetDate() != newTask.GetDate()):
      # they are not the same, fill in the missing days.
      lastDT = datetime.date.fromisoformat(task.GetDate())
      nowDT  = datetime.date.fromisoformat(newTask.GetDate())

      missingDT = lastDT + datetime.timedelta(days=1)
      while missingDT != nowDT:
         missingTask = MygTask.Create()
         missingTask.SetDate(missingDT.isoformat())

         MygTaskList.AddOrSet(missingTask)

         missingDT = missingDT + datetime.timedelta(days=1)

      #Add today's task.
      MygTaskList.AddOrSet(newTask)
      MygTaskList.FileStore()

   return

###############################################################################
# Get the n'th task
###############################################################################
def GetAt(index: int) -> MygTask.MygTask:
   """Get a task record"""
   return MygTaskList.GetAt(index)

###############################################################################
# Get the size of the list.
###############################################################################
def GetCount() -> int:
   """Get the number of task records"""
   return MygTaskList.GetCount()

###############################################################################
# Start
###############################################################################
def Start() -> bool:
   """Program start"""
   return MygTaskList.FileLoad()
