import React from 'react';

export default function Astuce({children}) {
  return (
    <div style={{
      border: '1px solid #f5c518',
      background: '#fffbe6',
      padding: '1em',
      borderRadius: '8px',
      margin: '1em 0'
    }}>
      <strong>Astuce :</strong> {children}
    </div>
  );
}
