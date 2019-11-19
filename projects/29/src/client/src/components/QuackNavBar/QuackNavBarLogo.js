import React from 'react';
import logo from './quack_small_logo.png'; // Tell Webpack this JS file uses this image
import styled from 'styled-components';

const Logo = styled.img`
    height: 3rem;
    padding-left: 1rem;
`
const VerticalWrapper = styled.div`
    display: flex;
    padding-top: 0.5rem;
    flex-direction: row;
    align-items: center;
`

const QuackNavBarLogo = () => {
    return (
        <VerticalWrapper>
            <Logo src={logo} />
        </VerticalWrapper>
    );
};

export default QuackNavBarLogo;