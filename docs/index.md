Tool to generate forest garden layouts

## How does it work?

Send HTTP POST to URL, it returns a Forest Garden layout

In future, this could have a web app for choosing the inputs and displaying the results.

Although fastapi/sqlmodel seems easier, might be better off using django. Otherwise you will need fastapi plus some frontend framework to build it. Django has everything integrated in.
Django + Postgresql + Redis + NGINX Unit

Write the documentation and text on the website from a gardeners perspective, not an IT one. Someone wanting a garden layout doesnt care that its written in X programming language using X framework.

- Deployment in docker. Probably overkill. DO droplet or linode VM, smallest size. Alpine, ansible, deploy with rsync script, ping Unit to load new app.
- Look more into DRF, need to see how it works
    - Do you even necessarily need DRF? It doesnt need to be a REST/API backend if django is rendering the frontend.
- Look into how to generate SVG images (imagemagick?)
- Think about design of the frontend, how will it look? Buttons and sliders then click submit?
    - How to handle scale? Need to set max limit on size otherwise it wont fit on screen and take loads of CPU time.
    - Maybe set reasonable limits and just say if you need bigger then run it multiple times and join them up yourself.
    - Maybe use standard colours to denote canopy layer, climbers, perrenials etc. Then have a text output which has a key and explains what specific plants are used.
- Rate limiting, caching etc.
- If you want to show changes over time, you'd need to generate a long series of images. So you may want to cache requests and already generated images when they have been generated before. Then maybe have an option to generate a new image which bypasses the cache.
- Lots of variables to consider
    - Initial input parameters
    - Light, wind, water
    - Plants relationships to one another

## MSCW

- field inputs to change grid, like size or zone/climate type
- show time periods to show different timelines of the plants. First planted / X years / X decades. Trees will outlive most plants. Perrenials last longer than biennial etc.
- need a DB containing the different plants/trees and weighting for different plants.
- draw walls and ponds/lakes/water feature. Some plants like walls/shade. Some plants are aquatic.
- needs to be layered. Trees take up lots of space higher up, not so much at the base of the trunk. May also need to show underground, as some plants have tubers or other specific root structures.
- Square grid. Use circles or regular shapes to show plant location and area taken up.
- Application is responsible for generating the grid locations for each plant, then its up to the frontend to decide how to display it.
- Maybe instead of layers it could be 3 separate images, one for each layer. Then they could be side-by-side. Or overlaid, depends on the frontend.
- Label the circles underneath with an ID number, then have a key at the side that says the plant name and a link to a page which describes all aspects about that plant.
- Wont do - Seaweed app like vertical ocean farming. This can be done later or as a second app.

