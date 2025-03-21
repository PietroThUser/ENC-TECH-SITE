actual_text = "actual_text"

if (!localStorage.getItem(actual_text)){
    localStorage.setItem(actual_text, 1)
}

document.addEventListener('DOMContentLoaded', function() {
    var element = document.getElementById('main');

    element.innerHTML = element.innerHTML.replace(/\*\*(.*?)\*\*/g, '<strong style="margin:5px">$1</strong>');
    element.innerHTML = element.innerHTML.replace(/-XX-(.*?)-XX-/g, '<h1 style="background-color: #0a0a0a; border: 1px solid hsla(0,0%,100%,.14); padding: 20px; border-radius: 25px;">$1</h1>');
    element.innerHTML = element.innerHTML.replace(/####/g, "");
});

function next_page(){
    actual_page = localStorage.getItem(actual_text)
    localStorage.setItem(actual_text, parseInt(actual_page) + 1)

    window.location.href = actual_page = localStorage.getItem(actual_text)
}

function back_page(){
    actual_page = localStorage.getItem(actual_text)
    localStorage.setItem(actual_text, parseInt(actual_page) - 1)

    window.location.href = actual_page = localStorage.getItem(actual_text)
}
