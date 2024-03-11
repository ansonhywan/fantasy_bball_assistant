import React from 'react'
import './navbar.css'
import { Link } from 'react-scroll';

const Navbar = () => {

    return (
        <nav className='navbar'>
            <div className='navOptions'>
                <Link className='navOptionsListItem'>Home</Link>
                <Link className='navOptionsListItem'>About Me</Link>
                <Link className='navOptionsListItem'>Teams</Link>
                <Link className='navOptionsListItem'>Temp</Link>
            </div>
            <button className='navbarButton'>Contact Me</button>
        </nav>
    )
}

export default Navbar;