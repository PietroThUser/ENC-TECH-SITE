document.addEventListener('DOMContentLoaded', function() {
    var element = document.getElementById('main');
    // Regex para encontrar texto entre **
    element.innerHTML = element.innerHTML.replace(/\*\*(.*?)\*\*/g, '<strong style="margin:5px">$1</strong>');
    element.innerHTML = element.innerHTML.replace(/-XX-(.*?)-XX-/g, '<h1 style="font-size=xx-larger">$1</h1>');
    element.innerHTML = element.innerHTML.replace(/####/g, "");
});