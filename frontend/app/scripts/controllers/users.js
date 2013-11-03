'use strict';

angular.module('frontendApp')
  .controller('UsersCtrl', function ($scope, User) {
    var set_data = function(scope, data, cur_page) {
      scope.users = data.results;
      scope.paging = {
        total: data.count,
        current_page: cur_page,
        max_size: 10
      };
    };

    User.query({page: 1}, function(data) {
      set_data($scope, data, 1);
    });

    $scope.pageChanged = function(page) {
      User.query({page: page}, function(data) {
        set_data($scope, data, page);
      });
    };

  });
