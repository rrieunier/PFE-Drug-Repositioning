# Frontend [deprecated]

This project is based on the [GoJS integration tutorial in a React.JS project](https://gojs.net/latest/intro/react.html). We chose GoJS in order to implement [this visualization model](https://gojs.net/latest/extensions/OverviewResizing.html) that enables biochemists to explore and fold/unfold nodes and links freely.

## Make it up and running
```bash
cd frontend
npm install
npm start
```
## Limitations
We faced several problems in the graph update process for molecules exploration and the query results when fetching graphs. We were not able to provide a working visualization tool with ReactJS

### Disclaimer
This part of the project is for inspiration-purpose only, with some improvements and the implementation of the OverviewResizing template, it should be able to parse the right graph and display it to the user.

The frontend part was slowly discontinued as we found a better tool to explore nodes similarity with Neo4J Graph Algorithms.
