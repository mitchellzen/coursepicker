"use strict";
import { Router, Route, Switch } from 'react-router'
var React = require('react');
//var Router = require('react-router');
var DefaultRoute = Router.DefaultRoute;
var NotFoundRoute = Router.NotFoundRoute;
var Redirect = Router.Redirect;

var routes = (
  <Route name="app" path="/" handler={require('./components/app')}>
    <DefaultRoute handler={require('./components/homePage')} />
    <Route name="courses" handler={require('./components/courses')} />
    <Route name="course" handler={require('./components/course')} />
    <Route name="login" handler={require('./components/login')} />
    <NotFoundRoute handler={require('./components/notFoundPage')} />
  </Route>
);
export {routes};