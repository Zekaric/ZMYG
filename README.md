
# Zekaric: Manage Your Goal (MY Goal)


## Table Of Contents

**1 - Summary**<br />
**2 - Discussion**<br />
**3 - Install**<br />

# 1 - Summary


"My Goal" is a web based Goal or trend manager for an internal network.  The idea of the tool is to see a running stream of achievement over time.  This is a psychological trick to keep you motivated.

# 2 - Discussion


This is a simple python base web application.  Everyday you pick which goals you achieved for that day and it will be displayed and stored for that day.

The data storage is a simple file.  It is a text file with date and keys of which tasks were completed that day.

**Warning:** This program is not intended to be used on a public server and should only be run on a local machine or a local network.  It is also only a single person goal tracker and not meant for multiple people.

# 3 - Install


Copy the files to a folder.

Set up an environment variable called MYG_DIR that points to the folder where you put the python code.

Start the program with...

```
	python "%MYG_DIR%/myg.py"
```

Point your browser to the http://... address that the new command prompt is showing.  If the program is unchanged it will be...

```
	http://localhost:8001
```

From there it will show you the past days and what you selected.  Click on an icon next to the title to set the tasks you did today.  Click the same icon if you made a mistake an need to remove a task.

**How to add or change tasks?**

Tasks are basically the svg files that start with the word "task".  The code saved to the myg.dat will be the rest of the file name for that file.  Very simple system.  Use your favorite vector program to create your svg files.

myg.dat is a simple text file where one record is stored per day.  A record is one line, starting with an ISO date and tab delimited codes for the tasks performed that day.

I find going very 'general' with your tracking is best.  I would not break down the tasks to include more specifics.  For me, my tasks were as follows.

**Art** - Anything creative like, writing, drawing, painting, etc.

**Dev** - Any programming as a hobby that I do.  It doesn't matter what project I'm working on, just that I am doing development and it's on my time and my project.

**Home** - Anything home/car/whatever related.  Like taking the car for an oil change.  Planing a reno in my home.  Cleaning the house.  Making simple repairs.  etc.

**Lrn** - Anything that is considered learning.  I'm trying to learn Chinese for instance.  Or learning to use a new software tool.  If it increases my knowledge in some way, it is learning.

**Med** - Anything health related.  Going for a hike, lifting weights, biking, dancing, anything fitness related.  Going to the Dentist, Optometrist, doctor's apointment, etc.

**Play** - Anything that is entertaining.  Playing a board game, video game, watching videos or movies, etc.
