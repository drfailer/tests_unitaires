<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

#header("Access-Control-Allow-Origin: *");
#header("Content-Type:application/json");

$myPDO = new PDO('sqlite:../db/sql/tests_unitaires.db');
$rep = $myPDO->query("SELECT resultat,id_utilisateur FROM retour;");
 while($cd = $rep->fetch()) {
 echo $cd['resultat']," ::: ",$cd['id_utilisateur'],"\r\n","<br>";
 }
?>