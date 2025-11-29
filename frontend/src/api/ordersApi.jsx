import axios from 'axios'

const api = axios.create({
  baseURL: 'https://api.example.com/orders'
})

export const getOrders = async () => {
  const response = await api.get('/orders')
  return response.data
}

export const getOrder = async (id) => {
  const response = await api.get(`/orders/${id}`)
  return response.data
}

export const createOrder = async (order) => {
  const response = await api.post('/orders', order)
  return response.data
}

export const updateOrder = async (id, order) => {
  const response = await api.put(`/orders/${id}`, order)
  return response.data
}

export const deleteOrder = async (id) => {
  await api.delete(`/orders/${id}`)
}