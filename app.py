from flask import Flask, request, jsonify ,render_template

app = Flask(__name__)

# สร้าง dictionary เก็บข้อมูลนักศึกษา
students = {}
# API endpoint สำหรับเรียกหน้า HTML
@app.route('/')
def index():
    return render_template('index.html')

# สำหรับเพิ่มข้อมูลนักศึกษา
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    id = data['id']
    name = data['name']
    surname = data['surname']
    gpax = data['gpax']
    flag = data['flag']
    students[id] = {'name': name, 'surname': surname, 'gpax': gpax, 'flag': flag}
    return jsonify({'message': 'Student added successfully'})

# สำหรับเเก้ไขข้อมูลนักศึกษา
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    if id in students:
        data = request.get_json()
        students[id]['name'] = data['name']
        students[id]['surname'] = data['surname']
        students[id]['gpax'] = data['gpax']
        students[id]['flag'] = data['flag']
        return jsonify({'message': 'Student updated successfully'})
    else:
        return jsonify({'error': 'Student not found'})

# สำหรับลบข้อมูลนักศึกษา
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    if id in students:
        del students[id]
        return jsonify({'message': 'Student deleted successfully'})
    else:
        return jsonify({'error': 'Student not found'})

# สำหรับดึงข้อมูลนักศึกษาโดยใช้ ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student_by_id(id):
    if id in students:
        return jsonify(students[id])
    else:
        return jsonify({'error': 'Student not found'})

# สำหรับดึงข้อมูลนักศึกษาทั้งหมด
@app.route('/students', methods=['GET'])
def get_all_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)
