'use strict';

angular.module('frontendApp')
  .controller('SessionCtrl', function ($scope, User, $routeParams) {
    $scope.user = User.get({id: $routeParams.id})
    var set_data = function(scope, data, cur_page) {
      scope.records = data.results;
      scope.paging = {
        total: data.count,
        current_page: cur_page,
        max_size: 10
      };
    };

    User.session({subid: $routeParams.sessionid, page: 1}, function(data) {
      set_data($scope, data, 1);
    });

    $scope.pageChanged = function(page) {
      User.records({id: $routeParams.id, page: page}, function(data) {
        set_data($scope, data, page);
      });
    };
  });
