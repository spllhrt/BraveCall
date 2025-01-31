// scripts.js
document.addEventListener('DOMContentLoaded', () => {
    const signupForm = document.querySelector('form');
    
    signupForm.addEventListener('submit', function(e) {
        const email = document.querySelector('input[name="email"]').value;
        const password = document.querySelector('input[name="password"]').value;
        
        if (email === "" || password === "") {
            alert("Please fill in all fields!");
            e.preventDefault();
        }
    });
});

// scripts.js
document.addEventListener('DOMContentLoaded', () => {
    const signupForm = document.querySelector('form');
    
    signupForm.addEventListener('submit', function(e) {
        const name = document.querySelector('input[name="name"]').value;
        const email = document.querySelector('input[name="email"]').value;
        const password = document.querySelector('input[name="password"]').value;
        const dob = document.querySelector('input[name="dob"]').value;
        
        if (name === "" || email === "" || password === "" || dob === "") {
            alert("Please fill in all fields!");
            e.preventDefault();
        }
    });
});
