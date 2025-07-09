import { loginUser, getToken, logoutUser } from "./model.js";
import { showLogin, showDashboard } from "./view.js";

const app = document.getElementById("card");

async function onLogin(event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const token = await loginUser(username, password);
    try {
        if (token) {
            renderDashboard();
        } else {
            throw new Error("Invalid credentials");
        }
    } catch (error) {
        alert("Login failed: " + error.message);
    }
    
}

async function onLogout() {
    try {
        await logoutUser();
        renderLogin();
    } catch (error) {
        alert("Logout failed: " + error.message);
    }
}

function renderLogin() {
    showLogin(app, onLogin);
}

function renderDashboard() {
    showDashboard(app, onLogout);
}

if (getToken()) {
    renderDashboard();
} else {
    renderLogin();
}