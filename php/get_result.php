<?php

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$userID = $_GET['user_id'];
$myPDO = new PDO('sqlite:../db/sql/tests_unitaires.db');

$request = $myPDO->prepare("SELECT resultat FROM retour WHERE id_utilisateur = :id");
$request->execute(['id' => $userID]);

while($res = $request->fetch())
{
    echo str_replace("\\n","\n",$res["resultat"]);
}

$request = $myPDO->prepare("DELETE FROM retour WHERE id_utilisateur = :userID;");
$result = $request->execute(['userID' => $userID]);
?>
