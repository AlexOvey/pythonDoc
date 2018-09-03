''' Instruction 
Multiple plots on single axis

It is time now to put together some of what you have learned and combine line plots on a common set of axes. The data set here comes from records of undergraduate degrees awarded to women in a variety of fields from 1970 to 2011. You can compare trends in degrees most easily by viewing two curves on the same set of axes.

Here, three NumPy arrays have been pre-loaded for you: year (enumerating years from 1970 to 2011 inclusive), physical_sciences (representing the percentage of Physical Sciences degrees awarded to women each in corresponding year), and computer_science (representing the percentage of Computer Science degrees awarded to women in each corresponding year).

You will issue two plt.plot() commands to draw line plots of different colors on the same set of axes. Here, year represents the x-axis, while physical_sciences and computer_science are the y-axes.

instruction
Import matplotlib.pyplot as its usual alias.
Add a 'blue' line plot of the % of degrees awarded to women in the Physical Sciences (physical_sciences) from 1970 to 2011 (year). Note that the x-axis should be specified first.
Add a 'red' line plot of the % of degrees awarded to women in Computer Science (computer_science) from 1970 to 2011 (year).
Use plt.show() to display the figure with the curves on the same axes.
Take Hint (-30 XP)

'''
# Import matplotlib.pyplot
import matplotlib.pyplot as plt 

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year,physical_sciences, color='blue')

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year,computer_science, color= 'red')

# Display the plot
plt.show()



'''Create a set of plot axes with lower corner xlo and ylo of 0.05 and 0.05, width of 0.425, and height of 0.9 (in units relative to the figure dimension).
Note: Remember to pass these coordinates to plt.axes() in the form of a list: [xlo, ylo, width, height].
Plot the percentage of degrees awarded to women in Physical Sciences in blue in the active axes just created.
Create a set of plot axes with lower corner xlo and ylo of 0.525 and 0.05, width of 0.425, and height of 0.9 (in units relative to the figure dimension).
Plot the percentage of degrees awarded to women in Computer Science in red in the active axes just created. 
'''
# Create plot axes for the first line plot
plt.axes([0.05,0.05,0.425,0.9])

# Plot in blue the % of degrees awarded to women in the Physical Sciences
plt.plot(year, physical_sciences, color='blue')

# Create plot axes for the second line plot
plt.axes([0.525, 0.05, 0.425,0.9])

# Plot in red the % of degrees awarded to women in Computer Science
plt.plot(year,computer_science, color='red')



''' instruction
Use plt.subplot() to create a figure with 1x2 subplot layout & make the first subplot active.
Plot the percentage of degrees awarded to women in Physical Sciences in blue in the active subplot.
Use plt.subplot() again to make the second subplot active in the current 1x2 subplot grid.
Plot the percentage of degrees awarded to women in Computer Science in red in the active subplot.
'''

