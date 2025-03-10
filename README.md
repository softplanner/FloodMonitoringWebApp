# Flood Monitoring Web App

A web-based flood monitoring system that provides real-time flood data visualization and alerts.

## Features
- **Real-time flood data**: Fetch and display real-time flood-related data from APIs.
- **Interactive Map**: Visualize affected areas using interactive maps.

## Technologies Used
- **Frontend**: HTML, JavaScript
- **Backend**: Python, Django
- **APIs**: Weather data APIs
- **Development Tools**: VS Code, Virtual Environment (`venv`)
- 
## Installation
### Prerequisites
- python
- VSCode
- Django
- Git

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/softplanner/FloodMonitoringWebApp.git
   cd FloodMonitoringWebApp
   ```
2. Open the project in VS Code:
   
```bash
code .
```

3. Select the Python interpreter:

```bash
Press Ctrl+Shift+P (or Cmd+Shift+P on macOS) and type Python: Select Interpreter.
```

4. Choose the virtual environment you created (e.g., venv):

```bash
Open the integrated terminal in VS Code (`Ctrl+``).
```

5. Activate the virtual environment (if not already activated):

```bash
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

6. Install dependencies:

```bash
pip install django, requests
```

7. Run application:
   
```bash
python manage.py runserver
```

## Usage
- Open the web application in your browser.
- View real-time flood data for the past 24 hours on the line graph for the selected station.
