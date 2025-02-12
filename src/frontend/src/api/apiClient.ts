import axios from "axios";

const apiClient = axios.create({
    baseURL: 'http://localhost:8000/',
    withCredentials: true,
    headers: {
        'Content-Type': 'application/json',
    }
})

export default apiClient
