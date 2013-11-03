'use strict';

var host = 'localhost';

var app = angular.module('frontendApp', ['ngResource', 'ui.bootstrap']);

app.factory('User', function($resource) {
  return $resource('http://' + host + '::port/users/:id/:verb', {'port': 9292, 'id': '@uid'}, {
                    query: { method: 'GET', params: {}, isArray: false },
                    records: { method: 'GET', params: {verb: 'records'}, isArray: false }
                  });
});

app.factory('Url', function($resource) {
  return $resource('http://' + host + '::port/urls/:id/:verb', {'port': 9292, 'id': '@id'});
});

app.config(function ($routeProvider) {
    $routeProvider
      // .when('/', {
      //   templateUrl: 'views/main.html',
      //   controller: 'MainCtrl'
      // })
      .when('/users', {
        templateUrl: 'views/users.html',
        controller: 'UsersCtrl'
      })
      .when('/users/:id/records', {
        templateUrl: 'views/records.html',
        controller: 'RecordsCtrl'
      })
      .when('/urls/:id/:uid', {
        templateUrl: 'views/url.html',
        controller: 'UrlCtrl'
      })
      .otherwise({
        redirectTo: '/users'
      });
  });
