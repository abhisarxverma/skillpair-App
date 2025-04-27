function showAlert() {
    let alertBox = document.getElementById("topAlert");
    alertBox.style.display = "block";  // Show the alert

    setTimeout(() => {
        alertBox.style.transition = "top 0.5s ease-out, opacity 0.5s";
        alertBox.style.top = "-60px";  // Move up
        alertBox.style.opacity = "0"; // Fade out

        setTimeout(() => {
            alertBox.style.display = "none"; // Hide completely
            alertBox.style.top = "0"; // Reset position
            alertBox.style.opacity = "1"; // Reset opacity
        }, 500);
    }, 2000);  // Alert disappears in 2 seconds
}