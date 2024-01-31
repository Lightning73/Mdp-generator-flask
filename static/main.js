function onSubmit(){
    let min=document.querySelector('#minn').checked,
        maj=document.querySelector('#majj').checked, 
        chiffres=document.querySelector('#chiff').checked,
        caracteres=document.querySelector('#caract').checked,
        long=document.querySelector('#longueur').value

    fetch("http://localhost:8080/generate", {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            minn: min,
            majj: maj,
            chiff: chiffres,
            caract: caracteres,
            longueur: long
        })
    }).then((response) => {
        response.json().then((json) => {
            document.querySelector('#output').innerHTML = json['mdp']
        })
    })
}
