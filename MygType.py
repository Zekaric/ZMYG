###############################################################################
# file:       MygType
# author:     Robbert de Groot
# company:    Zekaric
# copyright:  2022, Zekaric
#
# description:
# Type.
###############################################################################
"""MygType, a type for a goal"""

###############################################################################
# import
###############################################################################

###############################################################################
# global
# class
###############################################################################
###############################################################################
# Type Class
###############################################################################
class MygType:
   """MygType class"""

   def __init__(self, idVal: str = ""):

      self._id:  str = idVal
      self._svg: str = f"task{idVal}.svg"

   def __eq__(self, other: object) -> bool:
      if (isinstance(other, MygType)):
         return self._id == other._id
      return NotImplemented

   def __ge__(self, other: object) -> bool:
      if (isinstance(other, MygType)):
         return self._id >= other._id
      return NotImplemented

   def __gt__(self, other: object) -> bool:
      if (isinstance(other, MygType)):
         return self._id > other._id
      return NotImplemented

   def __le__(self, other: object) -> bool:
      if (isinstance(other, MygType)):
         return self._id <= other._id
      return NotImplemented

   def __lt__(self, other: object) -> bool:
      if (isinstance(other, MygType)):
         return self._id < other._id
      return NotImplemented

   def __ne__(self, other: object) -> bool:
      if (isinstance(other, MygType)):
         return self._id != other._id
      return NotImplemented

   def GetId(self) -> str:
      """Get the Type's id"""
      return self._id

   def GetSvg(self) -> str:
      """Get the Type's svg file"""
      return self._svg

###############################################################################
# global
# function
###############################################################################
###############################################################################
# Create
###############################################################################
def Create(idVal: str = "") -> MygType:
   """Create a Type"""
   return MygType(idVal)

###############################################################################
# Create a Type from a filename
###############################################################################
def CreateFromSvg(svgFileName: str) -> MygType | None:
   """Create a Type from a filename"""
   # Split the line
   part  = svgFileName.split('.')
   idVal = part[0][4:]

   return Create(idVal)
