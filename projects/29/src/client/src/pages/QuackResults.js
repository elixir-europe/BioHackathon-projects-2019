import React, {useContext} from 'react';
import {QuackNavBar} from '../components/QuackNavBar';
import QuackContext from '../context';
import styled from 'styled-components';
import {QuackQuinder} from "../components/QuackQuinder";
import {QuackVote} from "../components/QuackVote";

const ResultWrapper = styled.div`

    
`
const Content = styled.div`
    padding-top:10rem;
    display: flex;
    flex-direction: column;
    color: black;
    align-items:center;
`


const Bottom = styled.div`
   position: absolute;
   bottom: 10px;
   width: 100%;
`


const QuackResults = () => {
    const {state, dispatch} = useContext(QuackContext);

    return (
        <div>
            <QuackNavBar happyCount={state.happyCount}/>
            <Content>
                <QuackQuinder results={state.results}/>
                {(state.results.length === 0)? <h1><em>no further papers</em></h1>   : null}
            </Content>
            <Bottom>
                <QuackVote/>
            </Bottom>
        </div>
    );
};

export default QuackResults;

/*
                    {state.results.map((ele) => {
                        return (<QuackCard data={ele}/>)
                    })}
 */