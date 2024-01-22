from flask import Flask, render_template, redirect, url_for, request, jsonify
from app_routes import deployment_blueprint, testing_blueprint

app = Flask(__name__)

# Register blueprints with prefixes to avoid route conflicts
app.register_blueprint(deployment_blueprint, url_prefix='/deployment')
app.register_blueprint(testing_blueprint, url_prefix='/testing')

# In-memory database
items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        items.append(item)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_item(index):
    if index < len(items):
        items.pop(index)
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['POST'])
def update_item(index):
    if index < len(items):
        items[index] = request.form.get('new_item')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
