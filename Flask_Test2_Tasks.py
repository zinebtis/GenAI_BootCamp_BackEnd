from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database (liste f RAM)
tasks = [
    {"id": 1, "title": "Ta9ra Flask", "done": False},
    {"id": 2, "title": "Testi f Postman", "done": True}
]

# 🟢 1. GET كلشي tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

# 🟢 2. GET task ب id
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

# 🟢 3. POST: إضافة task جديدة
@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    new_task = {
        "id": len(tasks) + 1,
        "title": data.get("title"),
        "done": False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# 🟢 4. PUT: تعديل task موجودة
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    data = request.get_json()
    task["title"] = data.get("title", task["title"])
    task["done"] = data.get("done", task["done"])
    return jsonify(task)

# 🟢 5. DELETE: مسح task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "Task deleted"})

if __name__ == "__main__":
    app.run(debug=True)


