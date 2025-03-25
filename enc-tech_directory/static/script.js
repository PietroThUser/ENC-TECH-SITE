document.addEventListener('DOMContentLoaded', function() {
    var element = document.getElementById('main');

    element.innerHTML = element.innerHTML.replace(/\*\*(.*?)\*\*/g, '<strong style="margin:5px">$1</strong>');
    element.innerHTML = element.innerHTML.replace(/-XX-(.*?)-XX-/g, '<h1 class="title">$1</h1><hr class="title_border">');
    element.innerHTML = element.innerHTML.replace(/####/g, "");
});