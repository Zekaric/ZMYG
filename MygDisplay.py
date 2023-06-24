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

   # For all tasks...
   for index in range(MygTaskList.GetCount()):

      # Get the task
      task = MygTaskList.GetAt(index)

      if (dayOfWeek == 5 or dayOfWeek == 6):
         value += "<tr class=rowAlt>"
      else:
         value += "<tr>"
      dayOfWeek = (dayOfWeek + 6) % 7

      value += f"<td class=mono>{task.GetDate().replace('-', '&#8209;')} </td><td class=fill>"

      if (task.GetTypeCount() == 0):
         value += "<img class=sized src=noTask.svg />"
      else:
         for index in range(task.GetTypeCount()):
            typeItem = MygTypeList.FindById(task.GetTypeAt(index))
            if (typeItem is not None):
               value += f" {_GetSvg(typeItem)}"

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
