export function showLogin(continer, onLogin) {
    continer.innerHTML = `
        <h2>Log In</h2>
        <form id="loginForm">
            <input type="text" id="username" placeholder="User" required>
            <input type="password" id="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
    `;

    document.getElementById("loginForm").addEventListener("submit", onLogin);
}

export function showDashboard(continer, onLogout) {
    continer.innerHTML = `
        <h2>Welcome</h2>
        <p>You Login Successfull</p>
        <button id="logoutBtn">Sign out</button>
    `;

    document.getElementById("logoutBtn").addEventListener("click", onLogout);
}