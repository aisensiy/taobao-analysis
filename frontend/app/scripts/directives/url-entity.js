'use strict';

// parse url to json structure include:
// - host
// - path
// - query (json)
// - hash
var parse_url = function (url) {
  // decode url query or search to json structure
  function _parse_query(query) {
    var result = {};
    var kvs = query.slice(1).split('&');
    var i;
    for (i = 0; i < kvs.length; i++) {
      var kv = kvs[i].split('=');
      if (kv[1] == '') continue;
      result[decodeURIComponent(kv[0])] = decodeURIComponent(kv[1]);
    }
    return result;
  }

  var elem = document.createElement('a');
  elem.href = url;
  return {
    domain: elem.host,
    path: elem.pathname,
    query: _parse_query(elem.search),
    hash: elem.hash
  };
};

angular.module('frontendApp')
  .directive('urlEntity', function () {
    return {
      template: '<div><span class="label label-default">path:</span> {{domain}}{{path}}</div>' +
                '<div><span class="label label-default">query:</span> <ul><li ng-repeat="(key, value) in query">{{key}}: {{value}}</li></ul></div>',
      scope: {
        url: '@'
      },
      link: function (scope, element, attrs) {
        setTimeout(function() {
          var json = parse_url(scope.url);
          scope.domain = json.domain;
          scope.path = json.path;
          scope.query = json.query;
          scope.$apply();
        }, 0);
      }
    };
  });
