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
import calendar

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

   value += _DisplayTitle()
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
def _DisplayTitle() -> str:

   return "  <h1>Zekaric : MYG Goals</h1>"

###############################################################################
# Display the task list.
###############################################################################
def _DisplayTaskList() -> str:

   value = """
<table>
 <tbody>
  <tr>
   <th>JAN</th>
   <th>FEB</th>
   <th>MAR</th>
   <th>APR</th>
   <th>MAY</th>
   <th>JUN</th>
   <th>JUL</th>
   <th>AUG</th>
   <th>SEP</th>
   <th>OCT</th>
   <th>NOV</th>
   <th>DEC</th>
  </tr><tr>
"""

   dayOfWeek = datetime.date(datetime.date.today().year, 1, 1).weekday()

   # For all months...
   for month in range(12):

      value += "<td>"

      # For all days...
      for day in range(calendar.monthrange(datetime.date.today().year, month + 1)[1]):

         # start the row.
         if (dayOfWeek == 5 or dayOfWeek == 6):
            value += "<p class=Alt>"
         else:
            value += "<p>"
         dayOfWeek = (dayOfWeek + 1) % 7

         # display the date.  &#8209; is a non-breaking hyphen.
         value += f"<span class=\"text\">{day + 1:02d}&nbsp;&#8209;&nbsp;</span>"

         # For all task types...
         for typeIndex in range(MygTypeList.GetCount()):

            # Get the type.
            typeVal = MygTypeList.GetAt(typeIndex)

            # Get the type id.
            #typeId = typeVal.GetId()

            # For all tasks in the record...
            #isSet = False
            #for taskIndex in range(task.GetTypeCount()):

            #   # Get the type of the task
            #   taskTypeId = task.GetTypeAt(taskIndex)

            #   # if a task is matching the id then break
            #   if taskTypeId == typeId:
            #      isSet = True
            #      break

            # Display the task icon if needed.
            #if not isSet:
            #   value += "&nbsp;<img class=sized src=noTask.svg />"
            #else:
            value += f"&nbsp;<span class=\"img\">{_GetSvg(typeVal)}</span>"

         value += "</p>\n"

      value += "</td>\n"

   value += """
  </tr>
 </tbody>
</table>\n"""

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
