'use strict';

angular.module('frontendApp')
  .controller('UrlCtrl', function ($scope, Url, $routeParams) {
    $scope.uid = $routeParams.uid
    $scope.urlobj = Url.get({id: $routeParams.id});
  });
