const pathname = location.pathname;

const handleNavDisplaying = () => {
  let menu = document.querySelector(".icon");
  let header = document.querySelector(".nav-side-lt");

  menu.onclick = () => {
    menu.classList.toggle("fa-times");
    header.classList.toggle("active");
    document.body.classList.toggle("active");
  };

  window.addEventListener("scroll", () => {
    if (window.innerWidth > 1200) {
      menu.classList.remove("fa-times");
      header.classList.remove("active");
      document.body.classList.remove("active");
    }
  });
};
const handleShowingPassword = () => {
  const chexboxLabel = document.querySelector(".checkbox-text");
  const passwordInput = document.getElementById("id_password");
  const showPassword = document.getElementById("show_password");

  showPassword.addEventListener("change", (e) => {
    if (showPassword.checked) {
      passwordInput.type = "text";
    } else {
      passwordInput.type = "password";
    }
  });
};

/**
 * @param {string} tagName 
 * @param {object} attributes
 * 
 * @return {HTMLElement}
 */

function createElement(tagName, attributes = {}){
  const element = document.createElement(tagName);
  for ( const [attribute , value ] of Object.entries(attributes)){
       if(value !== null){
            element.setAttribute(attribute, value);
       }


  }
   return element; 
}



const createArticleScript =() => {
  const fileInput = document.querySelector('input[type="file"]'); 
  const fileButton = document.getElementById('file-submission');
  const fileContainer = document.querySelector('.upload-container');
  const imageContainer = document.querySelector('.uploaded-img'); 

  const handleFiles = ()  =>{
    let fileSelect = fileInput.files;
    
    for(let i = 0; i < fileInput.files.length; i++) {
      const div = createElement('div',{class: 'output'});
      const img = createElement('img'); 
      img.src = URL.createObjectURL(fileInput.files[i]);
      div.appendChild(img);
      console.log(div);
      console.log(img)
      imageContainer.appendChild(div);
    }
    console.log(fileInput.files);
    console.log(fileSelect); 

  }

  fileButton.onclick = () => {
    fileInput.click()
    
  }
  fileInput.addEventListener('change', handleFiles, false);

}

console.log(pathname);
switch (pathname) {
  case "/account/profil/":
    handleNavDisplaying();
    break;

  case "/account/connexion/":
    handleShowingPassword();
    break;
  case "/shop/create-article/": 
     createArticleScript(); 
    break; 

}
