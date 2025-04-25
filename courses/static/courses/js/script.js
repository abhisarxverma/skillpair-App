document.addEventListener("DOMContentLoaded", () => {
    get_all_courses();
});

function get_all_courses() {
    fetch("/courses/get_all_courses")
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        const courseView = document.querySelector("#home-courses-view");
        courseView.innerHTML = ``;

        data.courses.forEach(element => {
            const courseDiv = document.createElement("div");
            courseDiv.className = "col-7";

            const courseTitle = document.createElement("h3");
            courseTitle.innerHTML = element.title;
            courseDiv.appendChild(courseTitle);

            const courseDescription = document.createElement("p");
            courseDescription.innerHTML = element.description;
            courseDiv.appendChild(courseDescription);  

            const courseProducer = document.createElement("p");
            courseProducer.innerHTML = `By ${element.producer}`;
            courseDiv.appendChild(courseProducer); 

            courseView.appendChild(courseDiv);
        });
    })
    .catch(error => console.error("Fetch error:", error));
}
