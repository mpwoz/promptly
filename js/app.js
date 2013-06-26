
function MainCtrl($scope) {
  $scope.escape_sequences = escape_sequences;
  $scope.colors = colors;

  $scope.currentText = "";

  $scope.addSequence = function() {
    $scope.currentText += $scope.chosenDesc.seq;
  };

  $scope.changeColor = function() {
    $scope.currentText += "\\[\\033[" + $scope.chosenColor.code + "m\\]";
  };

  $scope.clearText = function() {
    $scope.currentText = "";
  };

  $scope.addCustomText = function() {
    if (!$scope.customText || $scope.customText === "") {
      $scope.currentText += " ";
    }
    else {
      $scope.currentText += $scope.customText;
    }
    $scope.customText = "";
  };

  $scope.testSelection = function() {
    console.log(window.getSelection());
  };
}
