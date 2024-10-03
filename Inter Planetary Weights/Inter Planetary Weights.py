# Author: Nick Hassett

#Declare constants by fully capitalizing names and separating names with underscores for readability.
MERCURY_SURFACE_GRAVITY_FACTOR = 0.38
VENUS_SURFACE_GRAVITY_FACTOR = 0.91
MOON_SURFACE_GRAVITY_FACTOR = 0.165
MARS_SURFACE_GRAVITY_FACTOR = 0.38
JUPITER_SURFACE_GRAVITY_FACTOR = 2.34
SATURN_SURFACE_GRAVITY_FACTOR = 0.93
URANUS_SURFACE_GRAVITY_FACTOR = 0.92
NEPTUNE_SURFACE_GRAVITY_FACTOR = 1.12
PLUTO_SURFACE_GRAVITY_FACTOR = 0.066

sName = input("Hello! What is your name?: ") #Get user's name as string.

userWeight = float(input("How much do you weigh?: ")) #Get user's weight and convert to float.

print  (f"\n{sName}, here is your weight if you were on a different planet:")

#Convert, format, and output user's weights on different planets.
print  (f"Weight on Mercury:    {userWeight * MERCURY_SURFACE_GRAVITY_FACTOR:>10.2f}\n"
        f"Weight on Venus:      {userWeight * VENUS_SURFACE_GRAVITY_FACTOR:>10.2f}\n"
        f"Weight on our Moon:   {userWeight * MOON_SURFACE_GRAVITY_FACTOR:>10.2f}\n"
        f"Weight on Mars:       {userWeight * MARS_SURFACE_GRAVITY_FACTOR:>10.2f}\n"
        f"Weight on Jupiter:    {userWeight * JUPITER_SURFACE_GRAVITY_FACTOR:>10.2f}\n"
        f"Weight on Saturn:     {userWeight * SATURN_SURFACE_GRAVITY_FACTOR:>10.2f}\n"
        f"Weight on Uranus:     {userWeight * URANUS_SURFACE_GRAVITY_FACTOR:>10.2f}\n"
        f"Weight on Neptune:    {userWeight * NEPTUNE_SURFACE_GRAVITY_FACTOR:>10.2f}\n"
        f"Weight on Pluto:      {userWeight * PLUTO_SURFACE_GRAVITY_FACTOR:>10.2f}\n")