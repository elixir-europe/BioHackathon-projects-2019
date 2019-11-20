import React,{useContext} from 'react';
import QuackNavBarLogo from './QuackNavBarLogo';
import styled from 'styled-components';
import QuackBasket from './QuackBasket';
import QuackContext from "../../context";

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
    display: flex;
    justify-content: flex-start;
`

const Middle = styled.div`
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Montserrat;
`
const End = styled.div`
    justify-content: End;
    margin-right: 1rem;
    margin-top: 0.5rem;
`


const QuackNavBar = () => {
    const {state} = useContext(QuackContext);

    return (
        <NavBar>
            <Start>
                <QuackNavBarLogo/>
            </Start>
            <Middle>
                <b>your query:</b>
                <em>{state.query}</em>
            </Middle>
            <End>
                <QuackBasket/>
            </End>
        </NavBar>
    );
};

export default QuackNavBar;