document.addEventListener('DOMContentLoaded', function () {
    loadTasks();
});

function addTask() {
    const newTaskInput = document.getElementById('newTask');
    const taskReminderInput = document.getElementById('taskReminder');
    
    if (newTaskInput.value === '') {
        alert('Please enter a task.');
        return;
    }

    const task = {
        text: newTaskInput.value,
        reminder: taskReminderInput.value,
    };

    let tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    tasks.push(task);
    localStorage.setItem('tasks', JSON.stringify(tasks));

    loadTasks();

    newTaskInput.value = '';
    taskReminderInput.value = '';
}

function deleteTask(index) {
    let tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    tasks.splice(index, 1);
    localStorage.setItem('tasks', JSON.stringify(tasks));
    loadTasks();
}

function loadTasks() {
    const taskList = document.getElementById('taskList');
    taskList.innerHTML = '';

    let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

    tasks.forEach((task, index) => {
        const taskElement = document.createElement('div');
        taskElement.className = 'task';
        taskElement.innerHTML = `
            <span>${task.text}</span>
            <span>${task.reminder}</span>
            <button onclick="deleteTask(${index})">Delete</button>
        `;
        taskList.appendChild(taskElement);
    });
}
