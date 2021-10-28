# Traveler
Game simulating a travler atttempting to cross a river with their livestock and crops.

# Parcels

## The Traveler
A neutral entity that has the following abilities:
 - Is able to load and unload packages from the transport
 - Is able to perform the crossing when present on the transport

## The Packages
All packages have two attributes list 
One list containing it's prey
One list containing it's predators

One or both lists have the potential to be empty

### Prey
If the traveler is not present a package is at risk to be consumed by another package that is in on it's predator list.
### Predator
If the traveler is not present a package is at risk to be consume another package that is in on it's prey list.

# Controls

## Load Packages
## Unload Packages

When a parcel crosses

## Attempt a Crossing
A crossing may be attempted at any point by selecting the 
Selecting to cross will set the state of the packages and produce one of 3 outcomes

# Outcomes
## Continue
User may keep playing the game.

## Success
The game has finished 'Congradulations!' the goal state has been met

## Game Over
A failure state has been met and the damage is irrepairable. 
Go back in time and try again.

# Problem Definition
There are 3 possible locations for a package to be located:
1. Start
2. Transport
3. End

For an item to reach 'Start' or 'End' the 'Transport' must be entereted prior to taking the Action to 'Cross'.
Each state will be represented as a dictionary
## State Representation 
Represented as a dictionary
 - Start -> []
 - Transport -> []
 - End -> []
 
### Initial State
Represented as a dictionary
 - Start -> (Traveler, Cabbage, Sheep, Wolf)
 - Transport -> ()
 - End -> ()

### Goal State
 - Start -> ()
 - Transport -> ()
 - End -> (Traveler, Cabbacge, Sheep, Wolf)



## Actions
A user has one possible action they may take 
Load Package
Unload Package
Cross

## Cost




