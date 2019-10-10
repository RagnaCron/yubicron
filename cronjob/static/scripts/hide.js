function displayHidden() {
    if (getComputedStyle(document.getElementById("optionalLogin"), null).display == "none"){
        document.getElementById("optionalLogin").style.display = "block";
    }
    else{
        document.getElementById("optionalLogin").style.display = "none";
    }
}