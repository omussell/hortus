# HORTUS 

Tool to generate example forest garden layouts


## How does it work?

Web app with buttons to generate

Initial landing page explains what a forest garden is. It also explains what this app does, namely, you give it your grid dimensions an choose some options, then it returns a graphic showing your generated garden, with a time slider so you can see the differences over time. Also shows the different layers: ground-cover, shrubs, canopy.


## MSCW

- random button
- field inputs to change grid, like size or zone/climate type
- show time periods to show different timelines of the plants. First planted / X years / X decades. Trees will outlive most plants. Perrenials last longer than biennial etc.
- Can do grid in CSS
- need a DB containing the different plants/trees and weighting for different plants.
- draw walls and ponds/lakes/water feature. Some plants like walls/shade. Some plants are aquatic.
- needs to be layered. Trees take up lots of space higher up, not so much at the base of the trunk. May also need to show underground, as some plants have tubers or other specific root structures.
- Square grid. Use circles to show plant location and area taken up.
- Application is responsible for generating the grid locations for each plant, then its up to the frontend to decide how to display it.
- Bulma CSS framework for building frontend
- Django? or FastAPI? or FastAPI proto with Go prod?
- Maybe instead of layers it could be 3 separate images, one for each layer. Then they could be side-by-side. Or overlaid, depends on the frontend.
- Label the circles underneath with an ID number, then have a key at the side that says the plant name and a link to a page which describes all aspects about that plant.
- Wont do - Seaweed app like vertical ocean farming. This can be done later or as a second app.
- JAMStack - static frontend, fastapi backend, SSG.
https://github.com/getpelican/pelican-themes/tree/master/bricks
- For generating output, we can use the GIS libraries. These handle coordinate systems and drawing shapes onto them.
    - GDAL
    - Fiona
    - Shapely - Converts the shapefile into an image
    - GeoJSON



## Plant information

### Deciduous/Evergreen
*D* indicates a deciduous woody plant or a herbaceous perennial that dies down to roots in winter. *E* indicates an evergreen plant. *SE* indicates a semi-evergreen plant.
### Zone (Hardiness zone)
The zone number given for a plant gives an indication of its hardiness. The zone number indicates the minimum average winter temperatures that a plant can tolerate.

### Sun/shade preference
This indicates the light conditions a plant really prefers and will thrive in.

- Full sun
- Light shade
- Moderate shade
- Deep shade

### Shade tolerance
This indicates the shadiest conditions that a plant will grow happily in and persist.

- Does not tolerate shade
- Tolerates light shade
- Tolerates moderate shade
- Tolerates fairly deep shade
- Tolerates deep shade beneath evergreen trees and shrubs

### Performance ratings
This indicates how well the plant performs in a forest garden, how well it grows and crops.

### Fertility
If the plant is a fruiting plant:

- *SF* Self-fertile
- *PSF* Partially self-fertile
- *SS* Self-sterile
- *M/F* Male and female plants

### Cover
For ground-layer plants, this indicates how well a dense planting covers the ground and excludes weeds.

- Poor
- Fair
- Good
- Very Good

### Products of a Forest Garden

- Fruits
- Vegetables
- Salad crops and herbs
- Dye plants
- Spices
- Poles and canes
- Basketry materials
- Medicinal plants
- Soap plants
- Sap and wood products
- Nuts and seeds
- Firewood
- Tying materials
- Mushrooms
- Honey
