import React, {useContext} from 'react';
import {QuackNavBar} from '../components/QuackNavBar';
import QuackContext from '../context';
import styled from 'styled-components';
import {QuackCard} from '../components/QuackCard';

const ResultWrapper = styled.div`
    display: flex;
    flex-flow: row wrap;
    justify-content: center;
`
const Content = styled.div`
    padding-top:5rem;
`


const QuackResults = () => {
    const {state, dispatch} = useContext(QuackContext);

    return (
        <div>
            <QuackNavBar happyCount={state.happyCount}/>
            <Content>
                <ResultWrapper>
                    {state.results.map((ele) => {
                        console.log("ELE", ele)
                        return (<QuackCard data={ele[1]}/>)
                    })}
                </ResultWrapper>
            </Content>
        </div>
    );
};

export default QuackResults;