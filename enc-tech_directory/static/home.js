let roadmap_id = 1

addEventListener('DOMContentLoaded', () => {
    home_content = document.getElementById(roadmap_id)
    home_content.style.display = "flex"
})

function next_id(){
    roadmap_id += 1
}

function previous_id(){
    roadmap_id -= 1
}
