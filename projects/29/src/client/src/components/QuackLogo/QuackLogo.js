import React from 'react';
import logo from './quack_logo.png'; // Tell Webpack this JS file uses this image
import styled from 'styled-components';

const Logo = styled.img`
    margin-top: 4rem;
`


function QuackLogo() {
    // Import result is the URL of your image
    return <Logo src={logo} alt="Logo"/>;
}

export default QuackLogo;