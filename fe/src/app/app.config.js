'use strict';

angular.
  module('newableApp').
  config(['$locationProvider' ,'$routeProvider',
    function config($locationProvider, $routeProvider) {
      //$locationProvider.hashPrefix('!');

      $routeProvider.
        when('/register', {
          template: '<user-register></user-register>'
        }).
        when('/login', {
        template: '<user-login></user-login>'
        }).
        otherwise('/login');
    }
  ]);
