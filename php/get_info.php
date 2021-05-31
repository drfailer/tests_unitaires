<?php

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

header("Access-Control-Allow-Origin: *");
header("Content-Type:application/json");

$exerciseID = $_GET['id_exercise'];

$myPDO = new PDO('sqlite:../db/sql/tests_unitaires.db');
$request = $myPDO->prepare("SELECT info_test FROM tests WHERE id_test = ?;");
$request->execute(array($exerciseID));

while($inf = $request->fetch()) {
   echo json_encode($inf["info_test"]);
}
   
?>
