import React from 'react'
import { Link } from 'react-router-dom'

export default function Navigation() {
  return (
    <nav className="bg-white py-4">
      <div className="container mx-auto px-4">
        <ul className="flex justify-between items-center">
          <li className="mr-6">
            <Link to="/" className="text-gray-600 hover:text-gray-900">Home</Link>
          </li>
          <li className="mr-6">
            <Link to="/about" className="text-gray-600 hover:text-gray-900">About</Link>
          </li>
          <li className="mr-6">
            <Link to="/blog" className="text-gray-600 hover:text-gray-900">Blog</Link>
          </li>
          <li>
            <Link to="/contact" className="text-gray-600 hover:text-gray-900">Contact</Link>
          </li>
        </ul>
      </div>
    </nav>
  )
}