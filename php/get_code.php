<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

header("Access-Control-Allow-Origin: *");
header("Content-Type:application/json");

$personalPost = json_decode(file_get_contents('php://input'),true);

$userID = $personalPost['user_id'];
$exerciseID = $personalPost['id_exercise'];
$code = $personalPost['code'];

$myPDO = new PDO('sqlite:../db/sql/tests_unitaires.db');
$request = $myPDO->prepare("UPDATE programme_utilisateur SET code = ?, test
  = ? WHERE id_programme = ?;");

$request->execute(array($code,$exerciseID,$userID));
?>
