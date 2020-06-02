import React, { useState, useEffect } from "react";
import { Switch, Route } from 'react-router-dom'
import Counter from './components/Counter'
import Chart from './components/Chart'
import "./style.css";

export default function App() {

  return (
    <div className="App">
      <Switch>
        <Route exact path='/' component={ Counter }/>
        <Route path='/chart' component={ Chart }/>
        <Route path='*' component={ Counter }/>
      </Switch>
    </div>
  );
}
