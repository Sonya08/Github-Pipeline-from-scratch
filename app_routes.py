from flask import Blueprint, jsonify, request
import subprocess

deployment_blueprint = Blueprint('deployment', __name__)
testing_blueprint = Blueprint('testing', __name__)

# Paths to your scripts
PATH_TO_TEST_SCRIPT = r"C:\Users\SONYA\Desktop\Github-Pipeline-from-scratch\test.sh"
PATH_TO_LAUNCH_SCRIPT = r"C:\Users\SONYA\Desktop\Github-Pipeline-from-scratch\launch.sh"

@deployment_blueprint.route("", methods=['POST'])
def deployment():
    try:
        data = request.json

        if 'ref' not in data:
            return jsonify({'success': False, 'message': "'ref' key not found in the data"}), 400

        branch_name = data['ref'].split('/')[-1]

        if branch_name == "main":
            subprocess.run([PATH_TO_LAUNCH_SCRIPT, branch_name], check=True)
            return jsonify({'success': True, 'message': 'Deployment started.'}), 200
        return jsonify({'success': False, 'message': 'Deployment not required for this branch.'}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@testing_blueprint.route("", methods=['POST'])
def testing():
    try:
        data = request.json

        if 'ref' not in data:
            return jsonify({'success': False, 'message': "'ref' key not found in the data"}), 400

        branch_name = data['ref'].split('/')[-1]

        if branch_name == "staging":
            subprocess.run([PATH_TO_TEST_SCRIPT, branch_name], check=True)
            return jsonify({'success': True, 'message': 'Testing started.'}), 200
        return jsonify({'success': False, 'message': 'Testing not required for this branch.'}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'message': str(e)}), 500
