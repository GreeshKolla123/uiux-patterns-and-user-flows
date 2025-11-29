import { useState, useEffect } from 'react'
import { getOrder } from '../api/ordersApi.jsx'

export default function useOrder(id) {
  const [order, setOrder] = useState({})
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchOrder = async () => {
      setLoading(true)
      try {
        const data = await getOrder(id)
        setOrder(data)
      } catch (error) {
        setError(error)
      } finally {
        setLoading(false)
      }
    }
    fetchOrder()
  }, [id])

  return { order, loading, error }
}