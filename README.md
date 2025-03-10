# Flood Monitoring Web App

A web-based flood monitoring system that provides real-time flood data visualization and alerts.

## Features
- **Real-time flood data**: Fetch and display real-time flood-related data from APIs.
- **Interactive Map**: Visualize affected areas using interactive maps.
- **Alert System**: Notify users of potential flood risks.
- **Historical Data Analysis**: View past flood trends for better decision-making.
- **User Authentication**: Secure login and user-specific settings.

## Technologies Used
- **Frontend**: React, Leaflet.js (for maps)
- **Backend**: Node.js, Express.js
- **Database**: MongoDB
- **APIs**: OpenWeatherMap, Government Flood Data APIs
- **Hosting**: AWS / Firebase

## Installation
### Prerequisites
- Node.js (v14 or higher)
- MongoDB
- Git

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/softplanner/FloodMonitoringWebApp.git
   cd FloodMonitoringWebApp
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Set up environment variables in a `.env` file:
   ```
   MONGO_URI=your_mongodb_connection_string
   API_KEY=your_api_key
   ```
4. Start the backend server:
   ```bash
   npm run server
   ```
5. Start the frontend development server:
   ```bash
   cd client
   npm start
   ```

## Usage
- Open the web application in your browser.
- Register/Login to access customized flood alerts.
- View real-time flood data on the map.
- Configure alerts based on location.

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
