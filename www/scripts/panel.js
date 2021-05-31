let text_pos = document.getElementById("compt-pos");
let code = document.getElementById('code-input');
let partieDroite = document.getElementById("right-panel");
let tabContent = document.getElementsByClassName("tabContent");

// Fonction pour indiquer le nbr de ligne,mot,lettre.
code.addEventListener('input', function (e) {
    e.stopPropagation();
    let compt_line = code.value.substr(0, code.selectionStart).split("\n").length;
    let compt_word = compt_line + code.value.substr(0, code.selectionStart).split(" ").length - 1;
    text_pos.value = "line :" + compt_line + "\nword :" + compt_word + "\nchar :" + code.value.length;
});


// Fonction qui va afficher/cacher les onglets.
function changementPanel(panel)
{

   for (let g of tabContent) {
        g.style.display = "none";
    }

    document.getElementById(panel).style.display = "block";
}
document.getElementsByClassName("defaultOpen")[0].click();
