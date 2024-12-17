# HealthRecordConverter

This repository contains a Python script to convert health record data into a structured JSON format. It is designed to process lab test results and export them in a project-specific JSON file.

---

## Features
- Converts raw health record data into a consistent JSON structure.
- Supports reference ranges for numeric values.
- Handles both numeric and non-numeric test ranges.

---

## Prerequisites
- **Python 3.x**
- **Git** (optional for version control)

---

## Usage

### 1. Clone the Repository
Use the following command to clone this repository to your local machine:

```bash
git clone https://github.com/stozo04/HealthRecordConverter.git
cd HealthRecordConverter
```

### 2. Run the Script
Make sure Python is installed on your machine, and run the script:

```bash
python health_record_converter.py
```

### 3. Output
The results are saved as a JSON file to the following path:
```
C:\Users\gates\OneDrive\Desktop\Health Records\new_results.json
```

---

## Code Example

Here is an example of the input and output JSON structure:

### Input
```json
{
    "componentInfo": {"name": "Cholesterol, Total", "units": "mg/dL"},
    "componentResultInfo": {"numericValue": 157, "referenceRange": {"low": null, "high": 200}}
}
```

### Output
```json
{
    "Test Name": "Cholesterol, Total",
    "Value": 157,
    "Unit": "mg/dL",
    "Date": 1703804400000,
    "Lower Normal": null,
    "Upper Normal": 200,
    "Range Type": "Non-Numeric"
}
```

---

## Contributing
Feel free to open issues or submit pull requests to improve this script.

---

## License
This project is licensed under the MIT License.

---

## Author
[stozo04](https://github.com/stozo04)
