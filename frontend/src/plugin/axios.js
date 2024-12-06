import axios from 'axios';

const apiAxios = axios.create({
  timeout: 5000,
});

apiAxios.interceptors.request.use(
  (config) => {
    // 例: Authorizationヘッダーを追加
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
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
