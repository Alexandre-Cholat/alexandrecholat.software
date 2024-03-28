function toggleMenu() {
    //adds or removes "open" class of menu or icon element, "open" class has styling
    const menu= document.querySelector(".menu-links");
    const icon= document.querySelector(".hamburger-icon");
    menu.classList.toggle("open");
    icon.classList.toggle("open");

}