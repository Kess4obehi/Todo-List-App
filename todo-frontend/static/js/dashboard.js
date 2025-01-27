const listEl = document.getElementById("list");
const createBtn = document.getElementById("create-btn");
const searchBar = document.getElementById("search-bar");

let todos = [];

// Add new task
createBtn.addEventListener("click", () => {
  const newTask = {
    id: Date.now(),
    text: "",
    complete: false,
    startDate: "",
    finishDate: "",
    priority: "low",
    category: "work",
    notes: "",
    reminder: ""
  };
  todos.unshift(newTask);
  renderTodos();
});

// Render all tasks
function renderTodos(filter = "") {
  listEl.innerHTML = "";

  todos
    .filter(todo => todo.text.toLowerCase().includes(filter.toLowerCase()))
    .forEach(todo => {
      const taskEl = document.createElement("div");
      taskEl.className =
        "bg-gray-50 border border-gray-200 rounded-lg p-4 shadow-md flex flex-col space-y-2";

      // Header
      const headerEl = document.createElement("div");
      headerEl.className = "flex justify-between items-center";
      headerEl.innerHTML = `
        <div class="flex items-center space-x-3">
          <input type="checkbox" ${todo.complete ? "checked" : ""} class="rounded">
          <input type="text" value="${todo.text}" class="text-lg font-medium w-full focus:outline-none focus:ring-2 focus:ring-blue-500 border-none">
        </div>
        <div>
          <button class="text-red-500 hover:text-red-700">Delete</button>
        </div>
      `;
      taskEl.appendChild(headerEl);

      // Details
      const detailsEl = document.createElement("div");
      detailsEl.className = "grid grid-cols-2 gap-4 pt-2";

      detailsEl.innerHTML = `
        <div>
          <label class="block text-sm text-gray-600">Start Date</label>
          <input name='start_date' type="date" value="${todo.startDate}" class="w-full border-gray-300 rounded-lg">
        </div>
        <div>
          <label class="block text-sm text-gray-600">Finish Date</label>
          <input name='finish_date' type="date" value="${todo.finishDate}" class="w-full border-gray-300 rounded-lg">
        </div>
        <div>
          <label class="block text-sm text-gray-600">Priority</label>
          <select name='priority' class="w-full border-gray-300 rounded-lg">
            <option value="low" ${todo.priority === "low" ? "selected" : ""}>Low</option>
            <option value="medium" ${todo.priority === "medium" ? "selected" : ""}>Medium</option>
            <option value="high" ${todo.priority === "high" ? "selected" : ""}>High</option>
          </select>
        </div>
        <div>
          <label class="block text-sm text-gray-600">Category</label>
          <select name='category' class="w-full border-gray-300 rounded-lg">
            <option value="work" ${todo.category === "work" ? "selected" : ""}>Work</option>
            <option value="personal" ${todo.category === "personal" ? "selected" : ""}>Personal</option>
            <option value="home" ${todo.category === "home" ? "selected" : ""}>Home</option>
          </select>
        </div>
        <div class="col-span-2">
          <label class="block text-sm text-gray-600">Notes</label>
          <textarea name='notes' class="w-full border-gray-300 rounded-lg" rows="3">${todo.notes}</textarea>
        </div>
      `;
      taskEl.appendChild(detailsEl);

      listEl.appendChild(taskEl);

      // Event Listeners
      headerEl.querySelector("input[type='checkbox']").addEventListener("change", e => {
        todo.complete = e.target.checked;
        saveTodos();
      });

      headerEl.querySelector("input[type='text']").addEventListener("input", e => {
        todo.text = e.target.value;
        saveTodos();
      });

      headerEl.querySelector("button").addEventListener("click", () => {
        todos = todos.filter(t => t.id !== todo.id);
        saveTodos();
        renderTodos();
      });

      detailsEl.querySelectorAll("input, select, textarea").forEach(input => {
        input.addEventListener("input", e => {
          const key = e.target.type === "textarea" ? "notes" : e.target.type === "select-one" ? "priority" : e.target.getAttribute("value") ? e.target.value : e.target.name;
          todo[key] = e.target.value;
          // saveTodos();
        });
      });
    });
}

// Search
searchBar.addEventListener("input", e => {
  renderTodos(e.target.value);
});

// Save and Load Todos
function saveTodos() {
  localStorage.setItem("todos", JSON.stringify(todos));
}

function loadTodos() {
  const saved = localStorage.getItem("todos");
  if (saved) todos = JSON.parse(saved);
}

loadTodos();
renderTodos();
