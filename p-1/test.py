from flask import Flask, request, jsonify
import pandas as pd
import json

app = Flask(__name__)

@app.route('/receive-data', methods=['POST'])
def receive_data():
    # Get the JSON data from the request
    json_data = request.get_json()

    # Convert the JSON data to a DataFrame
    table_data = []
    for table_name, rows in json_data.items():
        for row in rows:
            row['tableName'] = table_name
            table_data.append(row)

    # Create DataFrame
    df = pd.DataFrame(table_data)

    # Print or return the DataFrame for debugging
    print(df)

    return jsonify({"message": "Data received and converted to DataFrame"})

if __name__ == '__main__':
    app.run(debug=True)
