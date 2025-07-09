export async function loginUser(username, password) {
    const response = await fetch(`http://localhost:3000/users?username=${username}&password=${password}`);
    const users = await response.json();
    if (users.length > 0){
        const token = btoa(users[0].token);
        localStorage.setItem("token", token);
        return token;
    }
    return null;
}

export function getToken(){
    return localStorage.getItem("token");
}

export function logoutUser() {
    localStorage.removeItem("token")
}