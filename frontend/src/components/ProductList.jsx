import React from 'react'
import ProductCard from './ProductCard.jsx'

export default function ProductList() {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Products</h1>
      <div className="flex flex-wrap justify-center">
        <ProductCard />
        <ProductCard />
        <ProductCard />
      </div>
    </div>
  )
}