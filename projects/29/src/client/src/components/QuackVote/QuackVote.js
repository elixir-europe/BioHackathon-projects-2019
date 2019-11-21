import React, {useContext} from 'react';
import happyDuck from './happy_duck.svg';
import sadDuck from './sad_duck.svg';
import styled from 'styled-components';
import QuackContext from "../../context";
import classNames from 'classnames/bind';
import testdata from '../../testdata/testdata.json';

const Wrapper = styled.div`
    display: flex;
    justify-content: space-around;
`

const Img = styled.img`
    cursor: pointer;
`


const HappyButton = styled.button`
    border-radius:50%;

    border-width: 0px;
    background-color: transparent;
    :active{
        outline: 0;
          box-shadow: inset 0 5px 5px rgba(0, 0, 0, 0), 0 0 100px green;

    }
    :focus{
        outline: 0
    }
       z-index:10000;
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
          box-shadow: inset 0 5px 5px rgba(0, 0, 0, 0), 0 0 100px red;

    }
    z-index:10000;
    :focus{
        outline: 0
    }

`

const QuackVote = () => {
    const {state, dispatch} = useContext(QuackContext);
    const addToList = (listType) => {
        document.getElementById(state.index).style.visibility = "hidden";

        dispatch({type: listType, data: state.results[state.index]})
        if (state.index === 0) {
            dispatch({type: 'SET_RESULTS', data: testdata.slice(0, 9)})
            let eles = document.getElementsByClassName('outerCard');
            for (let i = 0; i < eles.length; i++) {
                eles[i].style.visibility = 'visible';
            }
        }
    }
    const sadClasses = classNames({
        'sadShine': state.sadState
    });
    const happyClasses = classNames({
        'happyShine': state.happyState
    });


    return (
        <Wrapper>
            <SadButton className={sadClasses} onClick={() => addToList('ADD_SAD')}>
                <Img src={sadDuck}/>
            </SadButton>
            <HappyButton className={happyClasses} onClick={() => addToList('ADD_HAPPY')}>
                <Img src={happyDuck}/>
            </HappyButton>
        </Wrapper>
    );
};

export default QuackVote;