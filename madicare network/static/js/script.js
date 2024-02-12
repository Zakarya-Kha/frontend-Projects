// let menu = document.querySelector('#menu-btn');
// let navbar = document.querySelector('.navbar');

// menu.onclick = () =>{
//     // menu.clickList.toggle('#menu-btn');
//     menu.clickList.toggle('fa-times');
//     navbar.clickList.toggle('active');
// }
// window.onscroll = () =>{
//     // menu.clickList.toggle('#menu-btn');
//     menu.clickList.remove('fa-times');
//     navbar.clickList.remove('active');
// }




// document.querySelector("#menu-btn").onclick = () =>{
//     document.querySelector(".navbar").classList.toggle('.active');
//     document.querySelector("#menu-btn").classList.toggle('#menu-btn');
//     document.querySelector("#menu-btn").classList.toggle('fa-times');
// };








// document.querySelector("#menu-btn").onclick = () => {
//     document.querySelector(".navbar").classList.toggle('active'); // Remove the dot before 'active'
//     document.querySelector("#menu-btn").classList.toggle('fa-times');
// };


const menuButton = document.querySelector("#menu-btn");
const navbar = document.querySelector(".navbar");

menuButton.onclick = () => {
    navbar.classList.toggle('active');
    menuButton.classList.toggle('fa-times');
};
// Add a click event listener to the document
document.addEventListener("click", (event) => {
    // Check if the clicked element is NOT part of the navbar and NOT the menu button
    if (!navbar.contains(event.target) && event.target !== menuButton) {
        navbar.classList.remove('active');
        menuButton.classList.remove('fa-times');
    }
});






// const profile = document.querySelector("#profile");
// const navbar1 = document.querySelector(".navbar1");

// profile.onclick = () => {
//     navbar1.classList.toggle('active');
//     profile.classList.toggle('fa-times');
// };
// document.addEventListener("click", (event) => {
//     if (!navbar1.contains(event.target) && event.target !== profile) {
//         navbar1.classList.remove('active');
//         menuButton.classList.remove('fa-times');
//     }
// });








// hide and show for btn =================================================


function toggleHide(){
    let pera = document.getElementById('pera');
    if(pera.style.display === 'none'){
      pera.style.display = 'block';
    }
    else{
      pera.style.display = 'none';
    }
  }


  
  function toggle1(){
    let care1 = document.getElementById('care1');
    if(care1.style.display === 'none'){
      care1.style.display = 'block';
    }
    else{
      care1.style.display = 'none';
    }
  }

  function toggle2(){
    let care2 = document.getElementById('care2');
    if(care2.style.display === 'none'){
      care2.style.display = 'block';
    }
    else{
      care2.style.display = 'none';
    }
  }

  function toggle3(){
    let care3 = document.getElementById('care3');
    if(care3.style.display === 'none'){
      care3.style.display = 'block';
    }
    else{
      care3.style.display = 'none';
    }
  }
  function toggle4(){
    let care4 = document.getElementById('care4');
    if(care4.style.display === 'none'){
      care4.style.display = 'block';
    }
    else{
      care4.style.display = 'none';
    }
  }
  function toggle5(){
    let care5 = document.getElementById('care5');
    if(care5.style.display === 'none'){
      care5.style.display = 'block';
    }
    else{
      care5.style.display = 'none';
    }
  }
  function toggle6(){
    let care6 = document.getElementById('care6');
    if(care6.style.display === 'none'){
      care6.style.display = 'block';
    }
    else{
      care6.style.display = 'none';
    }
  }



// for blogs button js here ==============================================

  function hideme(){
    let hideme = document.getElementById('hideme');
    if(hideme.style.display === 'none'){
      hideme.style.display = 'block';
      document.querySelector("#hideme").classList.toggle('fa-times');
    }
    else{
      hideme.style.display = 'none';
    }
  }

  function hideme1(){
    let hideme1 = document.getElementById('hideme1');
    if(hideme1.style.display === 'none'){
      hideme1.style.display = 'block';
      document.querySelector("#hideme1").classList.toggle('fa-times');
    }
    else{
      hideme1.style.display = 'none';
    }
  }

  function hideme2(){
    let hideme2 = document.getElementById('hideme2');
    if(hideme2.style.display === 'none'){
      hideme2.style.display = 'block';
      document.querySelector("#hideme2").classList.toggle('fa-times');
    }
    else{
      hideme2.style.display = 'none';
    }
  }


  



  // search btn js is here ============================================
//   document.addEventListener('DOMContentLoaded', function() {
//     const searchInput = document.getElementById('searchInput');
//     const searchButton = document.getElementById('searchButton');

//     searchButton.addEventListener('click', function() {
//         const searchTerm = searchInput.value.toLowerCase();
//         const departments = document.querySelectorAll('.department');

//         departments.forEach(department => {
//             const departmentName = department.getAttribute('data-name').toLowerCase();
//             if (departmentName.includes(searchTerm)) {
//                 department.style.display = 'block';
//             } else {
//                 department.style.display = 'none';
//             }
//         });
//     });
// });
