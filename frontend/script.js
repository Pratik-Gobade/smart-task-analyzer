let tasks = [];

// Add Task
function addTask() {
    const t = {
        title: document.getElementById("title").value,
        due_date: document.getElementById("due").value || null,
        estimated_hours: parseFloat(document.getElementById("hours").value || "1"),
        importance: parseInt(document.getElementById("importance").value || "5"),
        id: document.getElementById("taskid").value,
        dependencies: document.getElementById("deps").value
            ? document.getElementById("deps").value.split(",").map(s => s.trim())
            : []
    };

    tasks.push(t);
    document.getElementById("status").innerText = `Added (${tasks.length})`;

    // Reset Inputs
    document.getElementById("title").value = "";
    document.getElementById("due").value = "";
    document.getElementById("hours").value = "";
    document.getElementById("importance").value = "";
    document.getElementById("taskid").value = "";
    document.getElementById("deps").value = "";
}

// Analyze All Tasks
async function analyze() {
    const strategy = document.getElementById("strategy").value;

    const res = await fetch("http://127.0.0.1:8000/api/tasks/analyze/", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({tasks, strategy})
    });

    const data = await res.json();
    render(data.results);
}

// Suggest Top 3
async function suggest() {
    const strategy = document.getElementById("strategy").value;

    const res = await fetch("http://127.0.0.1:8000/api/tasks/suggest/", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({tasks, strategy})
    });

    const data = await res.json();
    render(data.top_3);
}

// Render Results
function render(list) {
    const resBox = document.getElementById("results");
    resBox.innerHTML = "";

    list.forEach(t => {
        const box = document.createElement("div");
        box.className = "task-box";

        box.innerHTML = `
            <h2>${t.title}</h2>
            <p><b>Score:</b> ${t.score}</p>
            <p><b>Priority:</b> ${t.priority}</p>
            <p>${t.explanation}</p>
        `;

        resBox.appendChild(box);
    });
}