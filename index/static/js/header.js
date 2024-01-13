const deconnexion = document.querySelector(".deconnexion");
const ajouter = document.querySelector(".ajouter");
const accueil = document.querySelector('.accueil');
const categorie = document.querySelector('.categorie_header');
const la_une = document.querySelector('.la_une');
const connecter = document.querySelector('.connecter');

get = window.location.pathname;
if (get == '/') {
    deconnexion.style.display = 'none'
    ajouter.style.display = 'none'

}else if (get == '/account/profil/' || get == get) {  
    accueil.style.display = 'none'
    categorie.style.display = 'none'
    la_une.style.display = 'none'
    connecter.style.display = 'none'
}
else if (get == '/shop/create-article/') {
    accueil.style.display = 'none'
    categorie.style.display = 'none'
    la_une.style.display = 'none'
    connecter.style.display = 'none'
    ajouter.style.display = 'none'
    
}





