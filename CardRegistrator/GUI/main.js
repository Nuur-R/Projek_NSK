eel.expose(rfidData);
function rfidData(rfid_data) {
    document.getElementById("rfid_data").innerHTML = "RFID :" + rfid_data;
    console.log(rfid_data);
}