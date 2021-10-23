# Tool to generate forest garden designs

Desired end goal is to have a web app which lets you select certain parameters, then when you click generate, it returns the layout for a forest garden according to your parameters.

To start off with it will just be the API backend and a HTTP client as the frontend.


Send HTTP POST to URL, it returns a Forest Garden layout
Maybe just coordinates and data to start with, not an actual image
Dont need Frontend tech like react/angular/svelte etc. Just use HTML and templating to create a basic page and render it on the server.

## Tech stack: 

- Frontend: 
    - Svelte
    - Typescript
    - Tailwind CSS 
    or
    - generated from backend
- Backend:
    - Go
    - sqlc + pgx
    - Postgresql

## Development 

### Phase 1:

- Project bootstrapping
    - Documentation generation
    - Initial Hello world code
    - Able to connect to database
    - Database schema migrations and SQL generation
    - Config/settings file
    - Able to deploy for testing

### Phase 2:

- Can send/receive HTTP requests to HTTP server
- HTTP server can connect to database and return test data
- No processing of the data

### Phase 3:

- Working API backend which when sending a request with a HTTP client, returns a JSON response which describes a basic garden layout and plant attributes.
- Backend can determine basic relationships between plants from test data

### Phase 4:

- More sophisticated methods for determining relationships between plants from test data

### Phase 5:

- API backend returns generated basic images instead of JSON data

## Notes
Write the documentation and text on the website from a gardeners perspective, not an IT one. Someone wanting a garden layout doesnt care that its written in X programming language using X framework.

- Deployment to server running NGINX Unit. SCP new binary to server. Ping Unit to load new app.
- Look into how to generate SVG images
- Think about design of the frontend, how will it look? Buttons and sliders then click submit?
    - How to handle scale? Need to set max limit on size otherwise it wont fit on screen and take loads of CPU time.
    - Maybe set reasonable limits and just say if you need bigger then run it multiple times and join them up yourself.
    - Maybe use standard colours to denote canopy layer, climbers, perrenials etc. Then have a text output which has a key and explains what specific plants are used.
- Rate limiting, caching etc.
- If you want to show changes over time, you'd need to generate a long series of images, or a GIF/video. So you may want to cache requests and already generated images when they have been generated before. Then maybe have an option to generate a new image which bypasses the cache.
- Lots of variables to consider
    - Initial input parameters
    - Light, wind, water
    - Plants relationships to one another
    - geographic location - will determine sun location, average temperature, hardiness zones

## MSCW

- field inputs to change grid, like size or zone/climate type
- show time periods to show different timelines of the plants. First planted / X years / X decades. Trees will outlive most plants. Perrenials last longer than biennial etc.
- need a DB containing the different plants/trees and weighting for different plants.
- draw walls and ponds/lakes/water feature. Some plants like walls/shade. Some plants are aquatic.
- needs to be layered. Trees take up lots of space higher up, not so much at the base of the trunk. May also need to show underground, as some plants have tubers or other specific root structures.
- Square grid. Use regular shapes (just squares/rectangles?) to show plant location and area taken up.
- Application is responsible for generating the grid locations for each plant, then its up to the frontend to decide how to display it.
- Maybe instead of layers it could be 3 separate images, one for each layer. Then they could be side-by-side. Or overlaid, depends on the frontend.
- Label the circles underneath with an ID number, then have a key at the side that says the plant name and a link to a page which describes all aspects about that plant.
- Wont do - Seaweed app like vertical ocean farming. This can be done later or as a second app.

