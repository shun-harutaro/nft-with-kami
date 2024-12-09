import axios from 'axios';

const apiAxios = axios.create({
  timeout: 5000,
  withCredentials: true
});

apiAxios.interceptors.request.use(
  (config) => {
    return config;
  },
  (error) => Promise.reject(error)
);

apiAxios.interceptors.response.use(
  (response) => response,
  (error) => {
    // エラーハンドリングの共通化
    if (error.response?.status === 401) {
      console.error('認証エラー。再ログインしてください。');
    }
    return Promise.reject(error);
  }
);

export default apiAxios;
