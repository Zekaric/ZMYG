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

import MygTypeList
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

   dayOfYear = 0
   dayOfWeek = datetime.date(datetime.date.today().year, 1, 1).weekday()

   todayMonth = datetime.date.today().month - 1
   todayDay   = datetime.date.today().day - 1

   isLeapDay  = False
   isLeapYear = False

   # For all months...
   for month in range(12):

      value += "<td>"

      # For all days...
      for day in range(calendar.monthrange(datetime.date.today().year, month + 1)[1]):

         # Test for leap years
         if month == 1 and day == 28:
            isLeapDay  = True;
            isLeapYear = True;

         isToday = False
         if month == todayMonth and day == todayDay:
            isToday = True

         # start the row.
         if   isToday:
            value += "<p class=Now>"
         elif dayOfWeek == 5 or dayOfWeek == 6:
            value += "<p class=Alt>"
         else:
            value += "<p>"
         dayOfWeek = (dayOfWeek + 1) % 7

         # display the date.  &#8209; is a non-breaking hyphen.
         value += f"<span class=\"text\">{day + 1:02d}&nbsp;</span>"

         # Get the tasks of the day.
         dayIndex = dayOfYear
         if isLeapYear and not isLeapDay:
            dayIndex = dayOfYear - 1
         # leap year day is day 365.  This is just so that at year change all
         # the pasy year's days are in the right place.
         elif isLeapYear and isLeapDay:
            dayIndex = 365

         task = MygTaskList.GetAt(dayIndex)

         # For all task types...
         for typeIndex in range(MygTypeList.GetCount()):

            # For all tasks in the record...
            isSet = task.GetFlag(typeIndex)

            # Display the task icon if needed.
            value += f"&nbsp;<span class=\"img\">{_GetCmd(dayIndex, typeIndex, isSet)}</span>"

         value += "</p>\n"

         dayOfYear += 1
         isLeapDay  = False;

      value += "</td>\n"

   value += """
  </tr>
 </tbody>
</table>\n"""

   return value

###############################################################################
# Convenience function for displaying a simple button form.
###############################################################################
def _GetCmd(dayIndex: int, typeIndex: int, isSet: bool) -> str:

   return f"""<a href="?day={dayIndex}&type={typeIndex}">{_GetSvg(typeIndex, isSet)}</a>"""

###############################################################################
# Convenience function to get a bit image.
###############################################################################
def _GetSvg(typeIndex: int, isSet: bool) -> str:

   typeItem = MygTypeList.GetAt(typeIndex)

   return f"<img class=sized src={typeItem.GetSvg(isSet)} />"
