angular.module('demo', [])
.controller('Hello', function($scope, $http) {
    $http.get('http://c4b301d7d229.ant.amazon.com:5000/packlist_creator/api/v1.0/get_order').
        then(function(response) {
            $scope.greeting = response.data;
        });
});