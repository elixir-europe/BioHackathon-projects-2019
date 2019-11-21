import React, {useContext} from 'react';
import happyDuck from './happy_duck.png';
import sadDuck from './sad_duck.png';
import styled from 'styled-components';
import QuackContext from "../../context";

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
const cursor = process.env.PUBLIC_URL + "/sign_of_horns.png";
const Img = styled.img`
    cursor: pointer;
`


const HappyButton = styled.button`
    border-radius:50%;

    border-width: 0px;
    background-color: transparent;
    :active{
        outline: 0;
          box-shadow: inset 0 5px 5px rgba(0, 0, 0, 0), 0 0 100px #93C5FF;

    }
    :focus{
        outline: 0
    }
`
const SadButton = styled.button`
    border-radius:100%;

    border-width: 0px;
    background-color: transparent;
    :active{
        outline: 0;
          box-shadow: inset 0 5px 5px rgba(0, 0, 0, 0), 0 0 100px #F6560D;

    }
    :focus{
        outline: 0
    }
`

const QuackVote = ({id}) => {
    const {state, dispatch} = useContext(QuackContext);
    const addToList = (listType) => {
        console.log('Add to list', listType)
        dispatch({type:listType, data: {id}}) // remove from result, add to happy
    }
    return (
        <Wrapper>
            <HappyButton onClick={()=>addToList('ADD_HAPPY')}><Img src={happyDuck}/></HappyButton>
            <Tiler/>
            <SadButton onClick={()=>addToList('ADD_SAD')}><Img src={sadDuck}/></SadButton>
        </Wrapper>
    );
};

export default QuackVote;