import React from "react";
import axios from "axios";
export default class ItemList extends React.Component {
  state = {
    items: [],
  };
  componentDidMount() {
    axios.get(`http://0.0.0.0:8000/items/`).then((res) => {
      console.log(res);
      this.setState({items: res.data});
    });
  }

  render() {
    return (
      <ul>
        {this.state.items.map((item) => (
          <li key={item.id}>{item.meal_name}</li>
        ))}
      </ul>
    );
  }
}