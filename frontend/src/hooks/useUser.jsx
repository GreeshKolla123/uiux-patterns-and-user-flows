import { useState, useEffect } from 'react'
import { getUser } from '../api/usersApi.jsx'

export default function useUser(id) {
  const [user, setUser] = useState({})
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  useEffect(() => {
    const fetchUser = async () => {
      setLoading(true)
      try {
        const data = await getUser(id)
        setUser(data)
      } catch (error) {
        setError(error)
      } finally {
        setLoading(false)
      }
    }
    fetchUser()
  }, [id])

  return { user, loading, error }
}