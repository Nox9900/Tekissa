const prev = document.querySelector('.prev');
const next = document.querySelector('.next');
const link = document.querySelector('.link');
const carte = document.querySelector('.carte');


next.addEventListener('click', () => {
    console.log('ok');
    carte.style.transform = 'translate (100%, 0%)';
});