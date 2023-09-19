from flask import Flask, request, jsonify
import string

app = Flask(__name__)

# Function to find the highest alphabet in the input array of alphabets
def find_highest_alphabet(alphabets):
    return max(alphabets, key=lambda x: ord(x))

@app.route('/api/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        data = request.json  # Assuming JSON input
        user_id = data.get('user_id')
        college_email = data.get('college_email')
        college_roll_number = data.get('college_roll_number')
        numbers = data.get('numbers', [])
        alphabets = data.get('alphabets', [])

        if not alphabets:
            highest_alphabet = None
        else:
            highest_alphabet = find_highest_alphabet(alphabets)

        result = {
            "Status": "Success",
            "User ID": "mansi_sahu_13122001",
            "College Email ID": "mansi.sahu2020@vitbhopal.ac.in",
            "College Roll Number": "20BAI10158",
            "Array for numbers": numbers,
            "Array for alphabets": alphabets,
            "Highest Alphabet": highest_alphabet,
        }
        return jsonify(result), 200

    elif request.method == 'GET':
        return jsonify({"operation_code": "Your-Operation-Code"}), 200

if __name__ == '__main__':
    app.run(debug=True)

#20BAI10158
#MANSI SAHU