import React from 'react';
import happyDuck from './happy_duck.png';
import sadDuck from './sad_duck.png';
import styled from 'styled-components';

const Wrapper = styled.div`
   display: flex;
   flex-direction: row;
   justify-content: space-around;
   padding-top: 0.5rem;
   border-top: 1px dashed black;
   padding-left: 2rem;
   padding-right: 2rem;
`
const Tiler = styled.div`
    border-right: 1px solid black;
    
`
const cursor = process.env.PUBLIC_URL+"/sign_of_horns.png";
const Img = styled.img`
    cursor: pointer;
`

const Button = styled.button`
    border-radius:50%;

    border-width: 0px;
    background-color: transparent;
    :active{
        outline: 0;
        background-color: yellow;
    }
    :focus{
        outline: 0
    }
`

const QuackVote = () => {
    return (
        <Wrapper>
            <Button><Img src={happyDuck}/></Button>
            <Tiler />
            <Button><Img src={sadDuck}/></Button>
        </Wrapper>
    );
};

export default QuackVote;