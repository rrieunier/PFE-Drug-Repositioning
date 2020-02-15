import React from "react";
import Playground from "./Playground";
import Autocomplete from "react-autocomplete";

interface AppState {
  search: string;
  drugs: Array<string>;
  nodes: object[];
  links: object[];
}

class App extends React.Component<{}, AppState> {
  text: string = "Lepirudin";
  state: AppState = {
    search: "Lepirudin",
    drugs: [],
    nodes: [],
    links: []
  };

  constructor(props: object) {
    super(props);
    fetch("http://localhost:5000/drugs")
      .then(data => data.json())
      .then(data => this.setState({ drugs: data }));
  }

  render() {
    const { drugs, search, nodes, links } = this.state;

    const url = `http://localhost:5000/graph${search && "/" + encodeURI(search)}`;
    console.log(url);
    return (
      <div>
        <h1>Drug repositioning</h1>
        <p>Cédric MARTINEZ & Roman RIEUNIER</p>
        <p>Gayo DIALLO (LaBRI)</p>
        <br />
        <label>
          Molecule{" "}
          <Autocomplete
            getItemValue={item => item}
            items={drugs}
            renderItem={(item, isHighlighted) => (
              <div
                style={{ background: isHighlighted ? "lightgray" : "white" }}
              >
                {item.label}
              </div>
            )}
            value={search}
            onChange={e => this.setState({ search: e.target.value })}
            onSelect={val =>
              this.setState({ search: val }, () =>
                fetch(url)
                  .then(data => data.json())
                  .then(({ nodes, links }) => this.setState({ nodes, links }))
              )
            }
          />
        </label>
        <br />
        <br />
        <Playground
          nodeDataArray={nodes}
          linkDataArray={links}
          updateGraph={() => {}}
        />
      </div>
    );
  }
}

export default App;
