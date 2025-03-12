actual_text = 1

document.addEventListener('DOMContentLoaded', function() {
    var element = document.getElementById('main');
    // Regex para encontrar texto entre **
    element.innerHTML = element.innerHTML.replace(/\*\*(.*?)\*\*/g, '<strong style="margin:5px">$1</strong>');
    element.innerHTML = element.innerHTML.replace(/-XX-(.*?)-XX-/g, '<h1 style="background-color: #0a0a0a; border: 1px solid hsla(0,0%,100%,.14); padding: 20px; border-radius: 25px;">$1</h1>');
    element.innerHTML = element.innerHTML.replace(/####/g, "");
});
