const toggle = document.getElementById("toggle-dark");

toggle.addEventListener("change", ()=>{
    document.body.classList.toggle("dark",toggle.checked);
    localStorage.setItem("darkMode",toggle.checked);
});

if (localStorage.getItem("darkMode")==="true"){
    toggle.checked = true;
    document.body.classList.add("dark");
}