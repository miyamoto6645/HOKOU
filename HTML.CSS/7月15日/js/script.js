function changeColoerHeader(){
    const item = document.getElementById("iHeader");
    item.style.backgroundColor="red";
}
function changeColoerAside(){
    const item = document.getElementById("iAside");
    item.style.backgroundColor="red";
}
function changeColoerMain(){
    const item = document.getElementById("iMain");
    item.style.backgroundColor="red";
}
function changeColoerReset(){
    const item = document.getElementById("iHeader");
    item.style.backgroundColor="white";
    const item2 = document.getElementById("iAside");
    item2.style.backgroundColor="white";
    const item3 = document.getElementById("iMain");
    item3.style.backgroundColor="white";
}
const item = document.querySelector("#btnChangeColorHeader");
item.onclick=changeColoerHeader;
const item2 = document.querySelector("#btnChangeColorAside");
item2.onclick=changeColoerAside;
const item3 =document.querySelector("#btnChangeColorMain");
item3.onclick=changeColoerMain
const item4 =document.querySelector("#btnChangeColorReset");
item4.onclick=changeColoerReset;