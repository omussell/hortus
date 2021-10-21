- Create scaffold for project:
    - Scripts to run formatting/linting
    - Initial barebones Go app
    - Initial sqlc models
    - Initial db migrations
    - Documentation build

- Figure out how to generate an image
- Add models and db stuff to store initial test data
- Generate an image using all the test data, no logic to layout nicely
- Start on logic to change layout based on rules

- Initial frontend setup
- Set up to load the initial landing page

- Deployment setup
    - minimal VM
    - k3s
    - kaniko for building images
    - skaffold for build control


- Test idea of storing plant info in DB, but their interactions with other plants (which is the maths stuff) in starlark files. Each plant is going to be different. Starlark language is simple but compiles easily. Could have common functions like spirals etc. which are imported.