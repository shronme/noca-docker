'use strict';

// Register `phoneList` component, along with its associated controller and template
angular.
  module('userLogin').
  component('userLogin', {
    templateUrl: 'user-login/user-login.template.html',
    controller: ['$scope', '$http', function Userlogin($scope, $http) {
      var self = this;
      self.orderProp = 'age';
      self.name = $scope.name;
      self.password = $scope.password;

      $scope.submit = function () {


        var req_data = { "action": "login", "name":$scope.email, "password":$scope.password};
        var response;
        $http({
              method: 'POST',
              url: 'http://newable-dev.w3stsheff8.eu-west-1.elasticbeanstalk.com/api/user',
              data: req_data,
              headers: {
                'Content-Type': 'application/json'
              }
            }).then(function successCallback(response) {
              self.response = response.data;
              $scope.message = self.response;


            }, function errorCallback(response){
                self.response = response.data;
                $scope.message = self.response;

            }
            );


      };
    }]
  });
