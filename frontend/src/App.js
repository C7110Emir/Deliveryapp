// App.js
import React, {Component} from "react";
import ItemList from "./Components/ItemList";
import AddItem from "./Components/AddItem";
class App extends Component {
  render() {
    return (
      <div>
        <AddItem />
        <header>Items List</header>
        <ItemList />
      </div>
    );
  }
}

export default App;