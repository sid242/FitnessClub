
    let burger = document.querySelector('.burger');
    let left = document.querySelector('.left');
    let right = document.querySelector('.right');
    let nav = document.querySelector('nav');

    burger.addEventListener('click',() =>{
        // console.log("hdi");
        left.classList.toggle('v-class');
        right.classList.toggle('v-class');
        nav.classList.toggle('h-nav');
    });