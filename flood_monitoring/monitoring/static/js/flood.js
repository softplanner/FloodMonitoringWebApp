
window.onload = function() {
    getStation();  // Call the function on page load
};

// The function to make the API call
async function getStation() {
        fetch('/monitoring/stations/')
            .then(response => response.json())
            .then(data => {
                // console.log("API Response:", data); 
                let dropdown = document.getElementById("stationSelect");
                dropdown.innerHTML = ''; // Clear existing options              
                data.data.items.forEach(item => {
                    // console.log(item.stationReference)
                    // console.log(item.town)    
                    let option = document.createElement("option");
                    option.value = item.stationReference;
                    option.textContent = item.stationReference + ' - ' + item.town;
                    dropdown.appendChild(option);
                });
            })
            .catch(error => console.error("Error loading data:", error));
}

// Function to fetch readings for a selected station
async function loadReadings() {
    let dropdown  = document.getElementById("stationSelect");
    let stationId = dropdown.value; // Get selected station ID

    // console.log('in loadReadings UI')
    // console.log('station id: ', stationId)

    if (!stationId) {
        console.warn("No station selected.");
        return; // Exit if no station is selected
    }

    try {
            const response = await fetch(`/monitoring/readings/${stationId}/`); // Fetch readings based on station ID
            const data     = await response.json(); // Parse response JSON

        if (!response.ok || data.error) {
            throw new Error(data.error || "Failed to fetch readings.");
        }
        
        console.log("Readings Data:", data);
            
        // Prepare data for the chart
        timeStamps = []
        values     = []
        i          = 0
        data.data.items.forEach(item => {
            timeStamps[i] = item.dateTime
            values[i]     = item.value    
            ++i
        });

        // // Dummy timestamps (e.g., hourly data)
        // const timeStamps = [
        //     "2025-03-09T10:00:00",
        //     "2025-03-09T11:00:00",
        //     "2025-03-09T12:00:00",
        //     "2025-03-09T13:00:00",
        //     "2025-03-09T14:00:00"
        // ];

        // // Dummy values (e.g., sensor readings)
        // const values = [5.2, 6.1, 4.8, 5.5, 6.3];

        // Update chart with new data
        updateChart(timeStamps, values); 
       
        // data.data.items.forEach(item => {
        //     console.log(item.dateTime)
        //     console.log(item.value)    
        // });


    } catch (error) {
        document.getElementById("errorMessage").style.display = "block";  // Show error message
        console.error("Error fetching readings:", error);
    }
}

// Attach event listener to the dropdown to load readings on change
document.getElementById("stationSelect").addEventListener("change", loadReadings);



// Function to update the chart
function updateChart(timestamps, values) {
    const ctx = document.getElementById('floodChart').getContext('2d');
    
    // Create chart if it doesn't exist or update if it does
    if (window.myChart) {
        window.myChart.data.labels = timestamps;
        window.myChart.data.datasets[0].data = values;
        window.myChart.update();
    } else {
        window.myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: timestamps,
                datasets: [{
                    label: 'Flood Levels',
                    data: values,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                    fill: false
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: false
                    }
                }
            }
        });
    }
}