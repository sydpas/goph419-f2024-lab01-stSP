# GOPH 419 -- Lab 01
*Instructor: Brandon Karchewski, Author: Sydney Pasloski, UCID: 30178579*

## General overview. 

This program designs an algorithm to compute a range of allowable launch angles for a rocket as a function of Earth's amplitude.

The main function uses 3 parameters:
- ve_v0, which is the input ratio of the escape velocity to terminal velocity.
- alpha, which is the desired maximum altitude as a fraction of Earth's radius.
- tol_alpha, which is the tolerance for maximum altitude.

These 3 parameters are then used to compute the minimum and maximum launch angle within the tolerance of maximum altitude. The steps of the algorithm are all computed in the src directory in the functions01.py file. 

The launch angle range is then displayed on a graph in the driver.py file which contains the main() source code.  

## How to clone the repository.

1. Open your preferred terminal on your local device.
2. Navigate to the directory where the repository files will be stored. 
3. To actually clone:
   - If you have an SSH key setup on the device, use: git clone git@github.com:USER/goph419-f2024-lab01-stYY.git
   - If you do not have an SSH key, use: git clone https://github.com/USER/goph419-f2024-lab01-st00.git
   - If you have GitHub CLI, use: gh repo clone USER/goph419-f2024-lab01-stYY
   - For all, replace USER with your username and YY with your initials.