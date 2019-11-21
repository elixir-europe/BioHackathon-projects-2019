import React,{useContext} from 'react';
import QuackNavBarLogo from './QuackNavBarLogo';
import styled from 'styled-components';
import QuackBasket from './QuackBasket';
import QuackSadBasket from './QuackSadBasket';

import QuackContext from "../../context";
import { TiDelete } from "react-icons/ti";

const NavBar = styled.div`
    height: 5rem;
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
    justify-content: End;
    margin-left: 1rem;
    margin-top: 0.5rem;
`

const Middle = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Montserrat;
    color: black;
`
const End = styled.div`
    justify-content: End;
    margin-right: 1rem;
    margin-top: 0.5rem;
`


const QuackNavBar = () => {
    const {state,dispatch} = useContext(QuackContext);
    const removeResults = () => {
        dispatch({type:'DELETE_ALL'})
    }
    return (
        <NavBar>
            <Start>
                            <QuackSadBasket/>

            </Start>
            <Middle>
                <QuackNavBarLogo />
            </Middle>
            <End>
                <QuackBasket/>
            </End>

        </NavBar>
    );
};

export default QuackNavBar;