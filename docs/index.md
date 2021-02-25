# HORTUS 

Tool to generate example forest garden layouts


## How does it work?

Send HTTP POST to URL, it returns a Forest Garden layout

In future, this could have a web app for choosing the inputs and displaying the results.

## MSCW

- field inputs to change grid, like size or zone/climate type
- show time periods to show different timelines of the plants. First planted / X years / X decades. Trees will outlive most plants. Perrenials last longer than biennial etc.
- need a DB containing the different plants/trees and weighting for different plants.
- draw walls and ponds/lakes/water feature. Some plants like walls/shade. Some plants are aquatic.
- needs to be layered. Trees take up lots of space higher up, not so much at the base of the trunk. May also need to show underground, as some plants have tubers or other specific root structures.
- Square grid. Use circles or regular shapes to show plant location and area taken up.
- Application is responsible for generating the grid locations for each plant, then its up to the frontend to decide how to display it.
- FastAPI
- Maybe instead of layers it could be 3 separate images, one for each layer. Then they could be side-by-side. Or overlaid, depends on the frontend.
- Label the circles underneath with an ID number, then have a key at the side that says the plant name and a link to a page which describes all aspects about that plant.
- Wont do - Seaweed app like vertical ocean farming. This can be done later or as a second app.

