import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Login from './components/Login/Login';

const App = () => (
  <Router>
    <div className="App">
      <Route path="/login" component={Login} />
    </div>
  </Router>
);

export default App;
