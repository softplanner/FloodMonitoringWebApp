# Flood Monitoring Web App

A web-based flood monitoring system that provides real-time flood data visualization and alerts.

## Features
- **Real-time flood data**: Fetch and display real-time flood-related data from APIs.
- **Interactive Map**: Visualize affected areas using interactive maps.

## Technologies Used
- **Frontend**: HTML, JavaScript
- **Backend**: Python, Django
- **APIs**: Weather data APIs
- **Machine Learning**: Python
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
2. Install dependencies:
- VSCode
- python
- Django
- Git

example commands to run on Windows, open folder in the VSCode (FloodMonitoringWebApp)

```bash
D:\FloodMonitoringWebApp> cd flood_monitoring
D:\FloodMonitoringWebApp\flood_monitoring> python -m venv env
D:\FloodMonitoringWebApp\flood_monitoring> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
D:\FloodMonitoringWebApp\flood_monitoring> .\env\Scripts\activate
D:\FloodMonitoringWebApp\flood_monitoring> pip install django
D:\FloodMonitoringWebApp\flood_monitoring> pip install requests
D:\FloodMonitoringWebApp\flood_monitoring> python manage.py runserver
```

Running the Project in VS Code
Open the project in VS Code:

```bash
code .
```

Select the Python interpreter:

```bash
Press Ctrl+Shift+P (or Cmd+Shift+P on macOS) and type Python: Select Interpreter.
```

Choose the virtual environment you created (e.g., venv).

Run the server:

```bash
Open the integrated terminal in VS Code (`Ctrl+``).
```

Activate the virtual environment (if not already activated):

```bash
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
Start the Django development server:
```

```bash
python manage.py runserver
```
## Usage
- Open the web application in your browser.
- View real-time flood data on the map.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Add feature"`
4. Push to your branch: `git push origin feature-name`
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For questions or support, contact **Muhammad Jawad**:
- Email: softplanner@gmail.com
- LinkedIn: [linkedin.com/in/mjawadpk](https://linkedin.com/in/mjawadpk)
