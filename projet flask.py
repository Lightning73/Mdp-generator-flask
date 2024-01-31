# installing dependencies : `pip install -r requirements.txt`

from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_cors import CORS
import datetime
import random

app = Flask(__name__, static_folder="static")
#pour régler le proglème d'accès à la page à cause de la securité
cors = CORS(app, resources={'/generate': {"origins": "*"}})

@app.route("/")
def test():
    return render_template("Presentation.html")


@app.route("/generate" , methods=['POST'])
def gen():
    """
    Fonction qui génère un mot de passe en fonction des caractéristiques
    choisies dans le formulaire

    Entrées: on récupère les valeurs min, maj, ch, et car du 
            formulaire sous forme de booléen grace à la methode post

    Sortie : si au moins une case est cochée, on renvoie le mot de passe créé
            sinon on renvoie un message pour que l'utilisateur renseigne les informations
    """
    reqBody = request.get_json()
    
    longueur=int(reqBody['longueur'])
    min=bool(reqBody['minn'])
    maj=bool(reqBody['majj'])
    ch=bool(reqBody['chiff'])
    car=bool(reqBody['caract'])

    #dictionnaire de toutes les valeurs possibles- du mot de passe
    valeurs={"majuscules": [ chr(i) for i in range(65,91) ], 
             "minuscules": [chr(i) for i in range(97,123)] , 
             "chiffres":[str(i) for i in range(0, 10)], 
             "caracteres_spe": [ '%' , '_' , '-' , '!' , '$' , '^' , '&' , '#' , '(' , ')' , '[' , ']' , '=' , '@']}
    val_mdp=[]
    mdp = ""
    # verifier qu'il y a au moins une valeur de définie, sinon renvoyer 'veuillez saisir une case svp'
    if min or maj or ch or car:
        #on ajoute les valeurs cochées du formulaire à une liste vide
        if min:
            val_mdp.extend(valeurs['minuscules'])
        if maj:
            val_mdp.extend(valeurs['majuscules'])
        if ch:
            val_mdp.extend(valeurs['chiffres'])
        if car:
            val_mdp.extend(valeurs['caracteres_spe'])
        
        for i in range (longueur):
            #on choisit au hasard des valeurs de la liste créée
            mdp+=(val_mdp[random.randint(0, len(val_mdp) -1)])

        return jsonify({'mdp': mdp})
    else:
        return jsonify({'mdp': "Veuillez renseigner les champs ci-dessus"})


@app.get('/generator')
def gen_view():
    #renvoie la page du formulaire, indépendament du mot de passe pour que la page ne se rafraichisse
    #pas à chaque fois qu'on génère un mot de passe
    return render_template("generator.html")
    
if __name__ == "__main__":
    app.run(debug=True, port=8080)

