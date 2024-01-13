const button = document.querySelector(".rotate");
const element = document.querySelector(".element-rotate");
const on = document.querySelector(".first-2");
const off = document.querySelector(".off");
const hidden = document.querySelector(".hidden");
const btn = document.querySelector(".second-part1")
const range = document.querySelector('.in')


btn.addEventListener("click", () => {
    button.classList.toggle("rotate-acting");
    element.classList.toggle("element-acting");


})
on.addEventListener("click", () => {
    on.classList.toggle("first-acting");
    hidden.style.display = "block";
    off.style.display = "block";
    range.style.display = "block";

})
off.addEventListener("click", () => {
    on.classList.toggle("first-acting");
    hidden.style.display = "none";
    off.style.display = "none";
    range.style.display = "none";
    
    
})

