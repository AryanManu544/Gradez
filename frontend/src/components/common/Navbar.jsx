import React from 'react';
import '../../styles/Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-left">
        <div className="navbar-brand">
          <img src="/assets/images/logo.png" alt="Logo" />
          <span>WebName</span>
        </div>
      </div>
      <div className="navbar-menu">
        <a href="/login">Login</a>
        <a href="/register">Register</a>
      </div>
    </nav>
  );
};

export default Navbar;
