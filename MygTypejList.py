###############################################################################
# file:       MygTypeList
# author:     Robbert de Groot
# company:    Zekaric
# copyright:  2022, Zekaric
#
# description:
# Project list handling.
###############################################################################
"""MygTypeList: a list of types for goals"""

###############################################################################
# import
###############################################################################
import os

import MygType

###############################################################################
# class
###############################################################################
class MygTypeList:
   """A list of types for goals"""
   _list: list[MygType.MygType] = []

   @classmethod
   def FileLoad(cls):
      """Load in the available types"""
      # for all files in the directory.
      for fileName in os.listdir("."):

         # check if the file is an task*.svg file.
         if (fileName[0:4] == "task"):
            goalType = MygType.CreateFromSvg(fileName)
            if (goalType is not None):
               cls._list.append(goalType)

      # this should sort the list by name.
      cls._list.sort()

   @classmethod
   def FindById(cls, idVal: str) -> MygType.MygType | None:
      """Find a type by id value"""
      # For all projects...
      for goalType in cls._list:

         # check if the ids match.
         if (idVal == goalType.GetId()):
            return goalType

      return None

   @classmethod
   def GetAt(cls, index: int) -> MygType.MygType:
      """Get a type at an index"""
      return cls._list[index]

   @classmethod
   def GetCount(cls) -> int:
      """Get the number of types"""
      return len(cls._list)

###############################################################################
# global
# class
###############################################################################

###############################################################################
# Load in the project list.
###############################################################################
def FileLoad():
   """Load in the types"""
   MygTypeList.FileLoad()

###############################################################################
# Find a project given a project id.
###############################################################################
def FindById(idVal: str) -> MygType.MygType | None:
   """Find type by id value"""
   return MygTypeList.FindById(idVal)

###############################################################################
# Get the n'th project in the array
###############################################################################
def GetAt(index: int) -> MygType.MygType:
   """Get a type at an index"""
   return MygTypeList.GetAt(index)

###############################################################################
# Get the number of projects in the project list.
###############################################################################
def GetCount() -> int:
   """Get the count of types"""
   return MygTypeList.GetCount()

###############################################################################
# Start the project list routines
###############################################################################
def Start() -> bool:
   """Program start up"""
   MygTypeList.FileLoad()
   return True
