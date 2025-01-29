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
