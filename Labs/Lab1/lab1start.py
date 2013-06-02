# STARTUP (Don't edit, typically) 
from __future__ import division
from visual import *
from physutil import *
import csv

# VISUALIZATION & GRAPH INITIALIZATION
# ===========================================

# Setup window for plotting
graph = PhysGraph(1)
# Setup Display window for visualization 
scene = display(width = 640, height = 480, background = color.white, range = 2.5, title = "VPython Test")
# Create object for visualization
ball = sphere(color = color.blue, radius = 0.22)
# Create a track behind object to visualize trajectory
trail = curve(color = color.green, radius = 0.02)
# Create small sphere to mark the origin in Display window
origin = sphere(pos=vector(0,0,0), color = color.yellow, radius = 0.04)


# SYSTEM PROPERTIES and INITIAL CONDITIONS 
# ===========================================

# System Mass
#EDIT THIS (next one line): 
ball.m = 1

#Initial Conditions
#EDIT THIS (next three lines, as necessary) 
ball.pos = vector(-1,0,0)
ball.vel = vector(1,0,0)
t = 0  #the time when we choose to start our clock


# OTHER INITIALIZATION 
# ===========================================
#
#Timestep
#EDIT THIS (next one line, as necessary)
deltat = 0.01

#OPTIONAL: Output model predictions to file (.csv format)
#To use, uncomment next five lines (delete leftmost # ONLY)
#outputfile = open('pythonTest.csv', 'wb') # Set name of output file.
#                                        # NOTE: if the file already exists,
#                                         # it will be overwritten                                  
#DataWriter = csv.writer(outputfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL) # Create writer object
#DataWriter.writerow(['Time (s)','Position (m)']) # Write column headers for time, position, and velocity


# CALCULATION LOOP(Motion Prediction and Visualization)
# ===========================================
while t < 2.0:
    #Calculate Net Force
    #EDIT THIS (next one line; add more lines if necessary)
    Fnet=vector(1,1,1)
    #Predict new velocity (Insert Newton's 2nd Law here)
    #EDIT THIS (next one line)
    ball.vel = ball.vel + vector(0,0,0)
    #Predict new position
    #EDIT THIS (next one line)
    ball.pos = ball.pos + vector(0.01,0,0)
    # advance the clock
    t = t + deltat


    
    #Update the object's track
    trail.append(pos = ball.pos)
    #Plot something as a function of time
    #EDIT THIS (next one line, as necessary)
    graph.plot(t,ball.pos.x)

    #To speed up or slow down program execution
    #Edit next line (larger number, faster execution)
    rate(100)

    #OPTIONAL: Output model predictions to file (.csv format)
    #To use, uncomment next line
    #DataWriter.writerow([str(t),str(ball.pos.x)])




print(t,ball.pos.x)

#OPTIONAL: Output model predictions to file (.csv format)
#To use, uncomment next line
#outputfile.close()
