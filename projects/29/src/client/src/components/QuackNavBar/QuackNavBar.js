import React from 'react';
import QuackNavBarLogo from './QuackNavBarLogo';
import styled from 'styled-components';
import QuackNavbarSearch from "./QuackNavbarSearch";
import basket from './basket.svg';


const NavBar = styled.div`
    height: 4rem;
    border-bottom: solid 4px;
    border-color: black;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    position: fixed;
    top: 0;
    width: 100%;
    background-color: white;
`

const Start = styled.div`
    display: flex;
    justify-content: flex-start;
`

const End = styled.div`
    justify-content: End;
    margin-right: 1rem;
`

const Img = styled.img`
    height: 2.5rem;
    padding-top:0.5rem;
`


const QuackNavBar = ({query}) => {
    return (
        <NavBar>
            <Start>
                <QuackNavBarLogo/>
                <QuackNavbarSearch/>
            </Start>
            <End>
                <Img src={basket}/>
            </End>
        </NavBar>
    );
};

export default QuackNavBar;