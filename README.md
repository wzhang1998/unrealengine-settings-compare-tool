# Unreal Engine Settings Compare Tool

This project is a Streamlit application designed to compare configuration settings between two files. It allows users to upload files, view changes, and save logs of the comparisons.

## Project Structure

```
unrealengine-settings-compare-tool
├── app
│   ├── streamlit_app.py       # Main entry point for the Streamlit application
│   ├── compare_settings.py    # Logic for comparing settings between two files
├── README.md              # Documentation for the project
├── requirements.txt       # Project dependencies
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd unrealengine-settings-compare-tool
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:
   ```
   streamlit run app/streamlit_app.py
   ```

## Usage

- Upload two configuration files to compare their settings.
- The application will display any changed, added, or removed settings.
- You can save the comparison results as logs for future reference.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.