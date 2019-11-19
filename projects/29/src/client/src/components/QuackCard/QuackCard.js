import React from 'react';
import styled from 'styled-components';
import {QuackVote} from '../QuackVote';

const Card = styled.div`
    height: 400px;
    width: 400px;
    margin: 1rem;
    border-radius: 5px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background-color: #eee;
`
const TitleContentWrapper = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
`
const CardTitle = styled.h1`
    padding-left: 1rem;
    padding-right: 1rem;
    padding-bottom: 0.5rem;
    font-style: bold;
    font-size: 1.5rem;
    font-family: Dosis;
    padding-bottom: 0px;
`

const CardContent = styled.div`
    border-radius: 5px;
    padding-left: 1rem;
    padding-right: 1rem;

`
const CardBottom = styled.div`
      background-color: #dedede;
      padding-bottom: 0.5rem;
`

const QuackCard = ({data}) => {
    return (
        <Card>
            <TitleContentWrapper>
                <CardTitle>{data.title}</CardTitle>
                <CardContent>
                    {data.abstract}
                </CardContent>
            </TitleContentWrapper>
            <CardBottom>
                <QuackVote/>
            </CardBottom>
        </Card>
    );
};

export default QuackCard;