// Object to store data for server request

var serverData = {
    buffer: [], // Buffer array to store arrays of x, y, z values
    lat: null,
    long: null,
};

const thresholdMin = 10;
const thresholdMax = 12;
const bufferSize = 1000; 

const serverUrl = '<REPLACE WITH SERVER URL>/recvData/'; // Server URL

var bufferFlag = false; 
var updateGeoLoc = false;
function handleMotion(event) {
    const acceleration = event.acceleration;
    if (acceleration) {
        const x = acceleration.x.toFixed(2); // Round to 2 decimal places
        const y = acceleration.y.toFixed(2);
        const z = acceleration.z.toFixed(2);
        const timestamp = new Date(event.timeStamp).toLocaleTimeString(); // Convert timestamp to readable format

        const amplitude = Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2) + Math.pow(z, 2));

        // Add data to buffer as an array [x, y, z]
        serverData.buffer.push([x, y, z, amplitude]);

        if (amplitude >= thresholdMin && amplitude <= thresholdMax) {
            bufferFlag = true; 
            updateGeoLoc =  true;
            console.log(true)
        }

        const data = `Timestamp: ${timestamp}<br>X: ${x} m/s²<br>Y: ${y} m/s²<br>Z: ${z} m/s²<br>Amplitude: ${amplitude}<br><hr>`;
        document.getElementById('accelerationData').innerHTML = data;
        console.log(serverData.buffer.length )

        if(serverData.buffer.length == 1000){
        if ( bufferFlag) {

           fetch(serverUrl, {
               method: 'POST',
               headers: {
                   'Content-Type': 'application/json',
               },
               body: JSON.stringify(serverData), 
           })
           .then(response => {
               if (response.ok) {
                   console.log('Data sent to server successfully:', serverData.buffer);

               } else {
                   console.error('Failed to send data to server:', response.statusText);
               }
           })
           .catch(error => {
               console.error('Error sending data to server:', error);
           });

       }
       serverData.buffer = []
       bufferFlag = false; 
    }
        
    }
}


document.getElementById('startButton').addEventListener('click', startDataCollection);

// Function to start data collection
function startDataCollection() {
    if (window.DeviceMotionEvent && window.navigator.geolocation) {
        startAccelerometer();
        startGeolocation();
    } else {
        alert('Accelerometer sensor or geolocation not supported on this device.');
    }
}

function startAccelerometer() {
    window.addEventListener('devicemotion', handleMotion);
}


function startGeolocation() {
    navigator.geolocation.watchPosition(updateGeolocation, handleLocationError, { enableHighAccuracy: true });
}

function updateGeolocation(position) {
    if(updateGeoLoc){
    const latitude = parseFloat(position.coords.latitude.toFixed(6)); // Round latitude to 6 decimal places
    const longitude = parseFloat(position.coords.longitude.toFixed(6)); // Round longitude to 6 decimal places

    // Update geolocation data
    serverData.lat = latitude;
    serverData.long = longitude;
    updateGeoLoc = false;
    }

}

// Handle geolocation error
function handleLocationError(error) {
    console.error('Error getting geolocation:', error);
}