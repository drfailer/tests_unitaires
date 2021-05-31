# TODO:  CHEMIN ABSOLUE

import sqlite3
from sqlite3 import Error
import subprocess
import time

# Acessor #####################################################################

def path_file(t):
    return t[3]


def language(t):
    return t[0]


def command_compilation(t):
    return t[1]


def command_execution(t):
    return t[2]


def name_comp(t):
    return t[4]


def name_exec(t):
    return t[5]


# End Acessor #################################################################

# Function ####################################################################

# take the path to the data base and return the connection to it:
def create_connection():
    """ Return a connection to the db corresponding to the path given as
    parameter """
    connection = None
    try:
        connection = sqlite3.connect("./sql/tests_unitaires.db")
        print("connection to SQLite DB successful")
    except Error as err:
        print(f"Connection to DB failed: {err}")

    return connection


# generate user file
def generateUserFile(path_file,code,language,n_comp):
    with open(f"../data/{path_file}{n_comp}.{language}", "w", encoding="utf8") as code_file:
        code_file.write(code)


# do the test and return the result of the compilation/run.    
def make_test(code, id_user, id_exercice, path_file, language, command_compilation,command_execution,n_comp,n_exec):
    generateUserFile(path_file,code,language,n_comp)

    # compilation / execution
    retourCompilation = subprocess.run(f"cd ../data/{path_file} && {command_compilation}",
                                      stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell = True,text=True)
    retourExecution = subprocess.run(f"cd ../data/{path_file} && {command_execution}",
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell = True,text=True)

    #delete all tmp file.
    if n_comp != "":
        subprocess.run(f"rm ~/serveur/www/tests_unitaires/data/{path_file}{n_comp}.{language}",shell = True)
    if n_exec != "":
        subprocess.run(f"rm ~/serveur/www/tests_unitaires/data/{path_file}{n_exec}",shell = True)
    return retourCompilation,retourExecution


# withdraw the information in the tests table
def withdrawInformation(id_exercice):
    if id_exercice != None:
        ids = cur.execute("""SELECT id_test FROM tests;""").fetchall()
        
        l = [i[0] for i in ids]
        if id_exercice in l:
            sql_test = f"""SELECT langage, command_compilation,command_execution, path_to_file, nom_compilation,nom_execution FROM tests WHERE id_test='{id_exercice}';"""
            return cur.execute(sql_test).fetchone()
    return None




#
def update_db_result(id_result, result, id_user):
    """ Update the table 'retour' of the db with id_result, result and id_user,
    which are string given as parameter. """
    update_db(id_result,parseResult(result),id_user)

def update_db(id_result, result, id_user):
    """ Update the table 'retour' of the db with id_result, result and id_user,
    which are string given as parameter. """
    cur.execute("INSERT INTO retour(id_retour, resultat, id_utilisateur) values (?,?,?)", (id_result,result,id_user))
    connection.commit()

    
#
def parseResult(res):
    return f"""compilateur erreur :
    {res[0].stderr}
    execution erreur :
    {res[1].stderr}
    execution sortie :
    {res[1].stdout}"""
    
    
# End Function ################################################################
        
connection = create_connection()
cur = connection.cursor()

while True:
    count_rows = cur.execute(
        "SELECT * FROM programme_utilisateur;").fetchall()
    if len(count_rows) > 0:
        sql_select = """SELECT * FROM programme_utilisateur;"""
        for id_user, code, id_exercice in cur.execute(sql_select).fetchall():
            print(id_user,code,id_exercice)

            
            information =  withdrawInformation(id_exercice)
            if information != None:
                
                result= make_test(code, id_user, id_exercice,
                                  path_file(information), language(information), command_compilation(information),command_execution(information),name_comp(information),name_exec(information))

                update_db_result("r"+id_user,result,id_user)
                
                sql_supr = f"""DELETE FROM programme_utilisateur
                WHERE id_programme='{id_user}';"""
                cur.execute(sql_supr)
                

            elif code != None:
                update_db("r"+id_user,"Error : Pas la bonne ID",id_user)
                sql_supr = f"""DELETE FROM programme_utilisateur
                WHERE id_programme='{id_user}';"""
                cur.execute(sql_supr)

            connection.commit()       
