'use strict'


angular.
    module('register').
    component('register', {
    // templateUrl: 'register.template.html',
    template: 'Testing 123 = <span>{{$ctrl.testStr}}</span>',
    controller: ['$routeParams',
        function RegisterUser($routeParams,$scope, $http) {
            this.testStr = "123"

            // var name = $scope.name;
            // var password = $scope.password
            //
            //
            // $scope.submit = function() {
            // var req_data = { "name":$scope.email, "password":$scope.password};
            // var response;
            // $http({
            //       method: 'POST',
            //       url: 'newable.w3stsheff8.eu-west-1.elasticbeanstalk.com/api/user',
            //       data: req_data,
            //       headers: {
            //         'Content-Type': 'application/json'
            //       }
            //     }).then(function (response) {
            //       self.response = response.data;
            //
            //       $timeout(function () {
            //         self.response = "BAD";
            //       }, 500);
            //     });
            // };
        }
    ]



});

