import json
from datetime import datetime

# Input data
input_data = [
    {
        "componentInfo": {"name": "Cholesterol, Total", "units": "mg/dL"},
        "componentResultInfo": {"numericValue": 157, "referenceRange": {"low": None, "high": 200}}
    },
    {
        "componentInfo": {"name": "HDL Cholesterol", "units": "mg/dL"},
        "componentResultInfo": {"numericValue": 50, "referenceRange": {"low": 40, "high": None}}
    },
    {
        "componentInfo": {"name": "Triglycerides", "units": "mg/dL"},
        "componentResultInfo": {"numericValue": 68, "referenceRange": {"low": None, "high": 150}}
    },
    {
        "componentInfo": {"name": "LDL Cholesterol", "units": "mg/dL (calc)"},
        "componentResultInfo": {"numericValue": 92, "referenceRange": {"low": None, "high": 100}}
    },
    {
        "componentInfo": {"name": "CHOL/HDLC RATIO", "units": "(calc)"},
        "componentResultInfo": {"numericValue": 3.1, "referenceRange": {"low": None, "high": 5.0}}
    },
    {
        "componentInfo": {"name": "Non-HDL Cholesterol", "units": "mg/dL (calc)"},
        "componentResultInfo": {"numericValue": 107, "referenceRange": {"low": None, "high": 130}}
    }
]

# Convert input data to desired structure
converted_results = [
    {
        "componentInfo": {"name": item["componentInfo"]["name"], "units": item["componentInfo"]["units"]},
        "componentResultInfo": {
            "numericValue": item["componentResultInfo"]["numericValue"],
            "referenceRange": {
                "low": item["componentResultInfo"]["referenceRange"].get("low"),
                "high": item["componentResultInfo"]["referenceRange"].get("high")
            }
        }
    }
    for item in input_data
]

# Convert input data to JSON format required for the project file
def convert_to_project_json(data, date_ms):
    result = []
    for entry in data:
        test_name = entry["componentInfo"]["name"]
        value = entry["componentResultInfo"]["numericValue"]
        unit = entry["componentInfo"]["units"]
        lower_normal = entry["componentResultInfo"]["referenceRange"]["low"]
        upper_normal = entry["componentResultInfo"]["referenceRange"]["high"]
        
        result.append({
            "Test Name": test_name,
            "Value": value,
            "Unit": unit,
            "Date": date_ms,
            "Lower Normal": lower_normal,
            "Upper Normal": upper_normal,
            "Range Type": "Numeric" if lower_normal is not None and upper_normal is not None else "Non-Numeric"
        })
    return result

# Assume today's date for this batch of results
specific_date = datetime(2024, 12, 29)
today_date_ms = int(specific_date.timestamp() * 1000)

# Convert and store results
converted_results = convert_to_project_json(converted_results, today_date_ms)

# Your output data (converted_results)
output_path = r"C:\\Users\\gates\\OneDrive\\Desktop\\Health Records\\new_results.json"

# Save the JSON data to the specified file path
with open(output_path, "w", encoding="utf-8") as json_file:
    json.dump(converted_results, json_file, indent=4)

print(f"Results successfully saved to: {output_path}")
