let roadmap_id = 1

addEventListener('DOMContentLoaded', () => {
    home_content = document.getElementById(roadmap_id)
    home_content.style.display = "flex"
})

function next_id(){
    roadmap_previous_id = roadmap_id
    actual_roadmap_id = roadmap_previous_id + 1

    home_content = document.getElementById(actual_roadmap_id)
    home_content.style.display = "flex"

    previous_home_content = document.getElementById(roadmap_previous_id)
    previous_home_content.style.display = "none"

    roadmap_id = actual_roadmap_id
}

function previous_id(){
    previous_roadmap_id = roadmap_id - 1

    previous_home_content = document.getElementById(previous_roadmap_id)
    previous_home_content.style.display = "flex"

    home_content = document.getElementById(roadmap_id)
    home_content.style.display = "none"
    
    roadmap_id = previous_roadmap_id
}