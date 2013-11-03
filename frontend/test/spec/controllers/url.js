'use strict';

describe('Controller: UrlCtrl', function () {

  // load the controller's module
  beforeEach(module('frontendApp'));

  var UrlCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    UrlCtrl = $controller('UrlCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
