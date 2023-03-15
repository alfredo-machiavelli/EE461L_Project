import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import Popup from 'react-popup'

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Popup />
    <App />
  </React.StrictMode>
);