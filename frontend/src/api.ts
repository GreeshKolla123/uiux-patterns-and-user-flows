import axios from 'axios';
const api = axios.create({
  baseURL: 'https://api.example.com'
});
export const registerUser = async (username: string, email: string, password: string) => {
  const response = await api.post('/auth/register', { username, email, password });
  return response.data;
};
export const loginUser = async (username: string, password: string) => {
  const response = await api.post('/auth/login', { username, password });
  return response.data;
};
export const getProducts = async () => {
  const response = await api.get('/products');
  return response.data;
};
export const getProduct = async (id: number) => {
  const response = await api.get(`/products/${id}`);
  return response.data;
};
export const addProductToCart = async (productId: number, quantity: number) => {
  const response = await api.post('/cart/add', { productId, quantity });
  return response.data;
};
export const getCart = async () => {
  const response = await api.get('/cart');
  return response.data;
};
export const createOrder = async (shippingAddress: string) => {
  const response = await api.post('/orders', { shippingAddress });
  return response.data;
};