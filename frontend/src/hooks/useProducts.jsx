import { useState, useEffect } from 'react'
import { getProducts } from '../api/productsApi.jsx'

export default function useProducts() {
  const [products, setProducts] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchProducts = async () => {
      setLoading(true)
      try {
        const data = await getProducts()
        setProducts(data)
      } catch (error) {
        setError(error)
      } finally {
        setLoading(false)
      }
    }
    fetchProducts()
  }, [])

  return { products, loading, error }
}