import React from 'react';
import QuackNavBarLogo from './QuackNavBarLogo';

import styled from 'styled-components';
import QuackNavbarSearch from "./QuackNavbarSearch";

const Style = styled.div`
    height: 4rem;
    font-size:2rem;
    border-bottom: solid 4px;
    border-color: black;
    font-family: Dosis;
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
`


const QuackNavBar = ({query}) => {
    return (
        <Style>
            <QuackNavBarLogo/>
            <QuackNavbarSearch/>
        </Style>
    );
};

export default QuackNavBar;