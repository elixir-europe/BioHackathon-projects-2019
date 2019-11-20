import React,{useContext} from 'react';
import logo from './quack_small_logo.png'; // Tell Webpack this JS file uses this image
import styled from 'styled-components';
import QuackContext from "../../context";
import quack2 from "./quack2_text.png";

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

const Img = styled.img`
    height: 3rem;
    margin-left: 0.2rem;
    margin-bottom: 1.5rem;
`

const QuackNavBarLogo = () => {
    const {state, dispatch} = useContext(QuackContext);
    const onClick = () => {
        dispatch({type: 'DELETE_ALL'})
    }
    return (
        <VerticalWrapper onClick={() => onClick()}>
            <Logo  src={logo}/>
            <Img src={quack2} />
        </VerticalWrapper>
    );
};

export default QuackNavBarLogo;