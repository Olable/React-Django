import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add JWT token to requests
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle token refresh on 401
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      const refreshToken = localStorage.getItem('refresh_token');

      if (refreshToken) {
        try {
          const response = await axios.post(`${API_URL}/auth/token/refresh/`, {
            refresh: refreshToken,
          });
          const newAccessToken = response.data.access;
          localStorage.setItem('access_token', newAccessToken);
          originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
          return apiClient(originalRequest);
        } catch (refreshError) {
          localStorage.removeItem('access_token');
          localStorage.removeItem('refresh_token');
          window.location.href = '/login';
        }
      }
    }
    return Promise.reject(error);
  }
);

export const authAPI = {
  signup: (data) => apiClient.post('/auth/signup/', data),
  login: (data) => apiClient.post('/auth/login/', data),
};

export const serverAPI = {
  list: (categoryId = null) =>
    apiClient.get('/server/', {
      params: categoryId ? { category: categoryId } : {},
    }),
  create: (data) => apiClient.post('/server/', data),
  retrieve: (id) => apiClient.get(`/server/${id}/`),
  update: (id, data) => apiClient.patch(`/server/${id}/`, data),
  delete: (id) => apiClient.delete(`/server/${id}/`),
  channels: (id) => apiClient.get(`/server/${id}/channels/`),
};

export const channelAPI = {
  list: (serverId = null) =>
    apiClient.get('/channel/', {
      params: serverId ? { server: serverId } : {},
    }),
  create: (data) => apiClient.post('/channel/', data),
  retrieve: (id) => apiClient.get(`/channel/${id}/`),
  update: (id, data) => apiClient.patch(`/channel/${id}/`, data),
  delete: (id) => apiClient.delete(`/channel/${id}/`),
  messages: (id) => apiClient.get(`/channel/${id}/messages/`),
};

export const messageAPI = {
  list: (channelId = null) =>
    apiClient.get('/message/', {
      params: channelId ? { channel: channelId } : {},
    }),
  create: (data) => apiClient.post('/message/', data),
  update: (id, data) => apiClient.patch(`/message/${id}/`, data),
  delete: (id) => apiClient.delete(`/message/${id}/`),
};

export default apiClient;
