// toggles the edit form visibility
function toggleEditForm(todoId) {
    const taskText = document.getElementById("taskText" + todoId); // element
    const taskInput = document.getElementById("taskInput" + todoId); // input
    const editButton = document.getElementById("editButton" + todoId); // edit button
    
    if (taskText.style.display === "none") { // checks if text is hidden
        taskText.style.display = "block"; // shows if hidden
        taskInput.style.display = "none"; // hides element
        editButton.innerText = "Edit Task"; // changes text
    } else {
        taskText.style.display = "none"; // if visible hides it
        taskInput.style.display = "block"; // shows it
        editButton.innerText = "Cancel"; // changes text
    }
}