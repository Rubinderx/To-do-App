function toggleEditForm(todoId) {
    const taskText = document.getElementById("taskText" + todoId);
    const taskInput = document.getElementById("taskInput" + todoId);
    const editButton = document.getElementById("editButton" + todoId);
    
    if (taskText.style.display === "none") {
        taskText.style.display = "block";
        taskInput.style.display = "none";
        editButton.innerText = "Edit Task";
    } else {
        taskText.style.display = "none";
        taskInput.style.display = "block";
        editButton.innerText = "Cancel";
    }
}