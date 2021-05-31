CREATE TABLE programme_utilisateur
(
  id_programme TEXT,
  code TEXT,
  test TEXT,
  PRIMARY KEY(id_programme),
  FOREIGN KEY(test) REFERENCES tests(id_test)
);



CREATE TABLE tests
(
  id_test TEXT,
  langage TEXT,
  command_compilation TEXT,
  command_execution TEXT,
  nom_compilation TEXT,
  nom_execution TEXT,
  path_to_file TEXT,
  info_test TEXT,
  PRIMARY KEY(id_test)
);

CREATE TABLE retour
(
  id_retour TEXT,
  resultat TEXT,
  id_utilisateur TEXT,
  PRIMARY KEY(id_retour),
  FOREIGN KEY(id_utilisateur) REFERENCES Utilisateur(id_utilisateur)
);

