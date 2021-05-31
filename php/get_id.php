<?php
#header("Access-Control-Allow-Origin: *");
#header("Content-Type:application/json");

function isIN($newID, $ids) {
  while($id = $ids->fetch()) {
    if ($newID == $id['idProgramme']) {
    return true;
    }
  }
  return false;
}

# Getting current used id list
$myPDO = new PDO("sqlite:../db/sql/tests_unitaires.db");
$newID;

# Generating new id
do {
$ids = $myPDO->query("SELECT id_programme FROM programme_utilisateur;");
  $newID = random_int(0, 10000);
} while (isIN($newID, $ids));

# Adding newID to db:

$request = $myPDO->prepare("INSERT INTO programme_utilisateur(id_programme,
  code, test) VALUES (?, NULL, NULL)");
  $request->execute(array($newID));
echo $newID;
?>
