document.addEventListener("DOMContentLoaded", function() {
    const getFlagBtn = document.getElementById("get-flag-btn");
    const message = document.getElementById("message");
    const flag = document.getElementById("flag");

    function getCookie(name) {
        let cookieArr = document.cookie.split(";");
        for (let i = 0; i < cookieArr.length; i++) {
            let cookiePair = cookieArr[i].split("=");
            if (name === cookiePair[0].trim()) {
                return decodeURIComponent(cookiePair[1]);
            }
        }
        return null;
    }

    const isAdminCookie = getCookie("isAdmin");

    if (isAdminCookie) {
        const isAdmin = atob(isAdminCookie).split(":")[1].trim();
        if (isAdmin === "true") {
            message.textContent = "Welcome, Admin! You can now get the flag.";
            getFlagBtn.disabled = false;
            getFlagBtn.classList.remove("disabled");
            getFlagBtn.addEventListener("click", function() {
                fetch('/admin', {
                    method: 'POST',
                    credentials: 'include'
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.flag) {
                            flag.textContent = data.flag;
                            flag.style.display = "block";
                        } else {
                            message.textContent = "Error retrieving flag.";
                        }
                    })
                    .catch(() => {
                        message.textContent = "Error retrieving flag.";
                    });
            });
        } else {
            message.textContent = "Sorry, this feature is only available for admins.";
            getFlagBtn.classList.add("disabled");
        }
    } else {
        message.textContent = "No access detected. Please log in first.";
        getFlagBtn.classList.add("disabled");
    }
});
