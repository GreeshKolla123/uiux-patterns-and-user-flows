import React from 'react'

export default function ProductCard() {
  return (
    <div className="bg-white rounded shadow-md p-4">
      <h2 className="text-lg font-bold mb-2">Product Name</h2>
      <p className="text-sm text-gray-600 mb-4">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
      <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Add to Cart</button>
    </div>
  )
}