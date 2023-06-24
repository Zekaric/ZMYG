###############################################################################
# file:       MygDisplay
# author:     Robbert de Groot
# company:    Zekaric
# copyright:  2023, Zekaric
#
# description:
#
###############################################################################
"""Display routines"""

###############################################################################
# imports:
###############################################################################
import datetime

import MygType
import MygTypeList
#import MygTask
import MygTaskList

###############################################################################
# global
# function
###############################################################################
###############################################################################
# Process the display
###############################################################################
def Process() -> str:
   """Print out the display"""

   value = """<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">

 <head>
  <meta charset="utf-8" />
  <link rel="stylesheet" type="text/css" href="style_reset.css">
  <link rel="stylesheet" type="text/css" href="style.css">
  <title>Zekaric:MYG</title>
 </head>

 <body>
"""

   value += _DisplayTypeList()
   value += _DisplayTaskList()

   value += """
 </body>
</html>"""

   return value

###############################################################################
# local
# function
###############################################################################
###############################################################################
# Display the project list.
###############################################################################
def _DisplayTypeList() -> str:

   value = "  <h1>Zekaric : MYG Goals "

   typeCount = MygTypeList.GetCount()
   for index in range(typeCount):

      typeItem: MygType.MygType = MygTypeList.GetAt(index)

      button = _GetCmd(typeItem)

      value += f"{button} "

   value += "</h1>"

   return value

###############################################################################
# Display the task list.
###############################################################################
def _DisplayTaskList() -> str:

   dayOfWeek = datetime.date.today().weekday()

   value = "<table>\n"

   # For all task records...
   for index in range(MygTaskList.GetCount()):

      # Get the task
      task = MygTaskList.GetAt(index)

      # start the row.
      if (dayOfWeek == 5 or dayOfWeek == 6):
         value += "<tr class=rowAlt>"
      else:
         value += "<tr>"
      dayOfWeek = (dayOfWeek + 6) % 7

      # display the date.  &#8209; is a non-breaking hyphen.
      value += f"<td class=mono>{task.GetDate().replace('-', '&#8209;')} </td><td class=fill>"

      # For all task types...
      for typeIndex in range(MygTypeList.GetCount()):
         # Get the type.
         typeVal = MygTypeList.GetAt(typeIndex)

         # Get the type id.
         typeId = typeVal.GetId()

         # For all tasks in the record...
         isSet = False
         for taskIndex in range(task.GetTypeCount()):

            # Get the type of the task
            taskTypeId = task.GetTypeAt(taskIndex)

            # if a task is matching the id then break
            if (taskTypeId == typeId):
               isSet = True
               break

         # Display the task icon if needed.
         if (not isSet):
            value += " <img class=sized src=noTask.svg />"
         else:
            value += f" {_GetSvg(typeVal)}"

      value += "</td></tr>\n"

   value += "</table>\n"

   return value

###############################################################################
# Convenience function for displaying a simple button form.
###############################################################################
def _GetCmd(typeItem: MygType.MygType) -> str:

   return f"""<a href="?val={typeItem.GetId()}">{_GetSvg(typeItem)}</a>"""

###############################################################################
# Convenience function to get a bit image.
###############################################################################
def _GetSvg(typeItem: MygType.MygType) -> str:

   return f"<img class=sized src={typeItem.GetSvg()} />"
