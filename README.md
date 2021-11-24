# Texels
A text-based **voxel** engine

Current goals:
------

* Create texel structure
  * Relative sizing, materials, use
* Create body structure to build out of texels
* Create update loop to begin to navigate texel universe
* Create format for developing new universes

Right now:
------

* Build room from body
* Room as 3D array
* Set null stages of array & texel stages
* Each texel contains a unique reference ID & type ID
* Type IDs keep us from having to create a unique texel every time
* And limit the amount of texels we actually create
* Although, we should be able to create 100% unique texels via scripting
* Bodies, being 3D arrays, can be hollow or filled
* Bodies can exist inside bodies, provided there is shape & space in the array
* To start; build a room with walls, floors, ceiling
* Then; build a player to put inside the room.
* Code must navigate positioning inside the Universe and inside each Body
* global_position & relative_position
* **Is the Universe a body?**