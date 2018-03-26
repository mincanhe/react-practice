import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Validation from './Validation/Validation';
import Char from './Char/Char';

class App extends Component {
  state = {
    UserInput:''
  };
 InputLengthHandler = (event) =>{
    this.setState({UserInput: event.target.value}
    )
  }
DeleteCharHandler = (index) => {
  const text = this.state.UserInput.split('');
  text.splice(index,1);
  const updatedText = text.join('');
  this.setState({UserInput:updatedText});
}
  render() {
    const charList = this.state.UserInput.split('').map((ch,index) => {
      return <Char character = {ch} key = {index} clicked = {()=>this.DeleteCharHandler(index)
      }/>
    });


    return (
      <div className="App">
        <input type='text' onChange = {this.InputLengthHandler}/>
        <p> {this.state.InputLength}</p>
        <Validation InputLength = {this.state.UserInput.length}/>
        {charList}
      </div>
    );
  }
}
export default App;
