import React from 'react';
import Home from './homePage';
import Courses from './courses';
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom';
const App = () => (
  <Router>
    <div>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><a href="#" data-toggle="modal" data-target="#login-modal">Login</a></li>
        <li><Link to="/courses">Courses</Link></li>
      </ul>

      <hr/>

      <Route exact path="/" component={Home}/>
      <Route path="/courses" component={Courses}/>
    </div>
  </Router>
);
export default App;