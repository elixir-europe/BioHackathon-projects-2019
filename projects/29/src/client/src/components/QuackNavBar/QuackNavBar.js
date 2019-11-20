import React,{useContext} from 'react';
import QuackNavBarLogo from './QuackNavBarLogo';
import styled from 'styled-components';
import QuackBasket from './QuackBasket';
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
    const {state,dispatch} = useContext(QuackContext);
    const removeResults = () => {
        dispatch({type:'DELETE_ALL'})
    }
    return (
        <NavBar>
            <Start>
                <QuackNavBarLogo/>
            </Start>
            <Middle>
                <b>your query:</b>
               &nbsp;<em>{state.query}</em>
                <TiDelete onClick={()=>removeResults()} style={{fontSize: "1.5rem", cursor: 'pointer'}}/>
            </Middle>
            <End>
                <QuackBasket/>
            </End>
        </NavBar>
    );
};

export default QuackNavBar;